import copy

def water_arb_elev(water_data, elev_of_interest):
    water_elev = water_data["elev"]
    unit_weight = water_data["unit_weight"]
    elev = elev_of_interest
    if elev >= water_elev:
        return 0
    return (water_elev - elev)*unit_weight


def total_singular(soil_data, water_data, surcharge):
    water_elev = water_data["elev"]
    total_stress = surcharge
    soil_height = soil_data.top_elev - soil_data.bottom_elev
    if soil_data.bottom_elev >= water_elev:
        total_stress += soil_data.moist_unit_weight * soil_height
    elif soil_data.top_elev <= water_elev:
        total_stress += soil_data.sat_unit_weight * soil_height
    else:
        total_stress += (soil_data.top_elev - water_elev) * soil_data.moist_unit_weight
        total_stress += (water_elev - soil_data.bottom_elev) * soil_data.sat_unit_weight
    # print("elev: {0} ; total stress: {1}".format(soil_data.bottom_elev, total_stress))
    return total_stress


def total_all(soil_data, water_data, surcharge=None, stresses=None, step=0):
    # print("stresses: {}".format(stresses))
    if stresses is None:
        stresses = []
    total_stresses = stresses
    if surcharge is None:
        surcharge = 0
    # print("\n")
    # print("step: {}".format(step))
    # print("total stresses: {}".format(total_stresses))
    # print("data length: {}".format(len(soil_data)))
    if step == 0:
        # for soil in soil_data:
        #     print("soil name: {0} ; soil moist weight: {1}".format(soil.name, soil.moist_unit_weight))
        total_stresses.append({
            "elev": soil_data[0].top_elev,
            "soil_id": soil_data[0].id,
            "total_stress": surcharge})
    if water_data["elev"] < soil_data[0].top_elev and water_data["elev"] > soil_data[0].bottom_elev:
        moist_height = soil_data[0].top_elev - water_data["elev"]
        stress_at_water_level = (moist_height * soil_data[0].moist_unit_weight) + surcharge
        total_stresses.append({
            "elev": water_data["elev"],
            "soil_id": soil_data[0].id,
            "total_stress": stress_at_water_level
        })
    total_stress = total_singular(soil_data[0], water_data, surcharge)
    total_stresses.append({
        "elev": soil_data[0].bottom_elev,
        "soil_id": soil_data[0].id,
        "total_stress": total_stress
    })
    if len(soil_data) == 1:
        return total_stresses
    else:
        step += 1
        new_soil_data = soil_data[1:]
        return total_all(new_soil_data, water_data, total_stress, total_stresses, step)


def water_pressure(soil_data, water_data):
    hydrostatic = []
    if water_data["elev"] >= soil_data[0].top_elev:
        hydrostatic.append({
            "elev": water_data["elev"],
            "soil_id": None,
            "water_press": 0
            })
        water_press = (water_data["elev"] - soil_data[0].top_elev)*water_data["unit_weight"]
        hydrostatic.append({
            "elev": soil_data[0].top_elev,
            "soil_id": None,
            "water_press": water_press
        })
    for soil in soil_data:
        if soil.bottom_elev >= water_data["elev"]:
            hydrostatic.append({
                "elev": soil.bottom_elev,
                "soil_id": soil.id,
                "water_press": 0
                })
        elif soil.top_elev <= water_data["elev"]:
            water_press = (water_data["elev"] - soil.bottom_elev)*water_data["unit_weight"]
            hydrostatic.append({
                "elev": soil.bottom_elev,
                "soil_id": soil.id,
                "water_press": water_press
            })
        elif water_data["elev"] < soil.top_elev and water_data["elev"] > soil.bottom_elev:
            hydrostatic.append({
                "elev": water_data["elev"],
                "soil_id": soil.id,
                "water_press": 0
                })
            water_press = (water_data["elev"] - soil.bottom_elev)*water_data["unit_weight"]
            hydrostatic.append({
                "elev": soil.bottom_elev,
                "soil_id": soil.id,
                "water_press": water_press
            })
    return hydrostatic


def effective(soils, total_stress, water_press):
    """this function calculates effective stress"""
    elev = []
    # print("total stress: {}".format(total_stress))
    # print("water pressure: {}".format(water_press))
    for item in total_stress:
        # print("total_stress elev = {}".format(item["elev"]))
        elev.append(item["elev"])
    for item in water_press:
        # print("water_press elev = {}".format(item["elev"]))
        elev.append(item["elev"])
    # unique_elev = None
    unique_elev = set(elev)
    # print("unique_elev = {}".format(unique_elev))
    eff_stresses = []
    for elevation in unique_elev:
        """creates dictionary template of the stresses at the current elevation."""
        stresses = {
            "elev": elevation,
            "soil_id": None,
            "total_stress": 0,
            "water_press": 0,
            "eff_stress": 0
            }
        """set the total stress at the current elevation."""
        for total in total_stress:
            if total["elev"] == elevation:
                stresses["total_stress"] = total["total_stress"]
        """set the water pressure at the current elevation."""
        for water in water_press:
            # print(water)
            if water["elev"] == elevation:
                stresses["water_press"] = water["water_press"]
                stresses["soil_id"] = water["soil_id"]
        """calculate the effective stress at the current elevation."""
        if stresses["total_stress"] == 0:
            stresses["eff_stress"] = 0
        else:
            stresses["eff_stress"] = stresses["total_stress"] - stresses["water_press"]
        eff_stresses.append(stresses)
    sorted_stresses = sorted(eff_stresses, key=lambda item: item["elev"], reverse=True)
    return sorted_stresses


def stresses_arbitrary(stresses, arb_elev):
    stress_1 = None
    stress_2 = None
    sorted_stresses = sorted(stresses, key=lambda item: item["elev"], reverse=True)
    for index, stress in enumerate(sorted_stresses):
        if stress["elev"] < arb_elev:
            stress_2 = stress
            stress_1 = sorted_stresses[index-1]
            break
    if stress_1 is None or stress_2 is None:
        raise ValueError("Elevation is beyond the available data")
    elev_1 = stress_1["elev"]
    elev_2 = stress_2["elev"]
    total_stress_1 = stress_1["total_stress"]
    total_stress_2 = stress_2["total_stress"]
    water_press_1 = stress_1["water_press"]
    water_press_2 = stress_2["water_press"]
    eff_stress_1 = stress_1["eff_stress"]
    eff_stress_2 = stress_2["eff_stress"]
    stresses_at_arb_elev = {
        "elev":
        arb_elev,
        "total_stress":
        interpolate_stress(elev_1, elev_2, total_stress_1, total_stress_2,
                           arb_elev),
        "water_press":
        interpolate_stress(elev_1, elev_2, water_press_1, water_press_2,
                           arb_elev),
        "eff_stress":
        interpolate_stress(elev_1, elev_2, eff_stress_1, eff_stress_2,
                           arb_elev),
    }
    return stresses_at_arb_elev


def interpolate_stress(elev_1, elev_2, stress_1, stress_2, arb_elev):
    elev_diff = arb_elev - elev_1
    elev_range = elev_2 - elev_1
    stress_range = stress_2 - stress_1
    stress_base = stress_1
    stress_at_arb_elev = stress_base + ((elev_diff / elev_range) *
                                        (stress_range))
    return round(stress_at_arb_elev, 10)
