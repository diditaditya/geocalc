"""import regex and copy"""
import re, copy

"""import soil and ground water data template"""
from overburden.data.ground_water_data import ground_water
from overburden.data.ground_water_data import units as gw_units
from overburden.data.units import stresses_units
from overburden.data.soil_data import Soil_unit, Soil_all

"""import overburden stresses calculation model"""
from overburden.model.overburden import total_all, water_pressure, effective, stresses_arbitrary


def get_water_data():
    return ground_water


def get_water_units():
    return gw_units


def get_stresses_units():
    return stresses_units


def update_water_data(new_water_data):
    is_elev_ok = new_water_data["elev"] is not None
    is_weight_ok = re.match(r"\d+\.?\d*",str(new_water_data["unit_weight"]))
    if is_elev_ok and is_weight_ok:
        ground_water["elev"] = new_water_data["elev"]
        ground_water["unit_weight"] = new_water_data["unit_weight"]
        return ground_water


def load_soil_data(saved_soils):
    soils = []
    for saved_soil in saved_soils:
        soil_id = saved_soil["id"]
        name = saved_soil["name"]
        top_elev = saved_soil["top_elev"]
        bottom_elev = saved_soil["bottom_elev"]
        sat_weight = saved_soil["sat_unit_weight"]
        moist_weight = saved_soil["moist_unit_weight"]
        soil = Soil_unit(soil_id, name, top_elev, bottom_elev, sat_weight, moist_weight)
        soils.append(soil)
    return soils


def calculate_overburden(soils, water_data):
    all_stresses = []
    total_stress = total_all(soils, water_data)
    water_press = water_pressure(soils, water_data)
    all_stresses = effective(soils, total_stress, water_press)
    return all_stresses


# # driver code
# soil_layers = Soil_all()
# soil_1 = Soil_unit(1, "soil a", 0, -2, 20, 10)
# soil_2 = Soil_unit(2, "soil b", -2, -4, 18, 16)
# soil_3 = Soil_unit(3, "soil c", -4, -5, 19, 17)
# soil_layers.add_new_soil(soil_1)
# soil_layers.add_new_soil(soil_2)
# soil_layers.add_new_soil(soil_3)
# # print(soil_layers)

# ground_water["elev"] = 1
# # print(ground_water)

# surcharge = 0
# if ground_water["elev"] > soil_layers.get_soil_data()[0].top_elev:
#     surcharge = (ground_water["elev"] - soil_layers.get_soil_data()[0].top_elev) * ground_water["unit_weight"]
# total = total_all(soil_layers.get_soil_data(), ground_water, surcharge)
# print("total stresses")
# for index, item in enumerate(total):
#     print(index, item)

# hydrostatic = water_pressure(soil_layers.get_soil_data(), ground_water)
# print("\nhydrostatic")
# for index, item in enumerate(hydrostatic):
#     print(index, item)

# eff_stress = effective(total, hydrostatic)
# print("\neffective stresses")
# for index, item in enumerate(eff_stress):
#     print(index, item)

# arb_elev = -3.5
# print("\nstresses at elev {}".format(arb_elev))
# try:
#     stresses_arb = stresses_arbitrary(eff_stress, arb_elev)
#     print(stresses_arb)
# except Exception as e:
#     print(str(e))

# print("\nchange moist unit weight of soil 1 to 18")
# soil_1.moist_unit_weight = 18
# # total = total_all(soil_layers.get_soil_data(), ground_water, surcharge)
# print("soil layers")
# new_soil_layers = soil_layers.get_soil_data()
# for index, soil in enumerate(new_soil_layers):
#     print(index, soil)

# total_2 = total_all(new_soil_layers, ground_water, surcharge, [])
# print("\ntotal stresses")
# for index, item in enumerate(total_2):
#     print(index, item)
