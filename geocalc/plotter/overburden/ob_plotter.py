"""import matplotlib pyplot module"""
import matplotlib.pyplot as plt

figure_count = 0

def parse_soils(soils, stress_limits, hor_buffer):
    """this function parses the soil layers elevations and name"""
    soils_data_set = []
    for soil in soils:
        soil_data = {}
        soil_data["hor"] = [
            stress_limits["min"] - hor_buffer,
            stress_limits["max"] + hor_buffer
        ]
        soil_data["ver_top"] = [soil.top_elev, soil.top_elev]
        soil_data["ver_bot"] = [soil.bottom_elev, soil.bottom_elev]
        soil_data["text_hor"] = stress_limits["min"]
        soil_data["text_ver"] = soil.top_elev - 0.5
        soil_data["name"] = soil.name
        soils_data_set.append(soil_data)
    return soils_data_set


def parse_water(water, stress_limits, hor_buffer):
    """this function parses the ground water level"""
    water_data_set = {}
    water_data_set["hor"] = [
        stress_limits["min"] - hor_buffer, stress_limits["max"] + hor_buffer
    ]
    water_data_set["ver_top"] = [water["elev"], water["elev"]]
    return water_data_set


def parse_elevs(stresses):
    """this function parses the elevations of the stresses"""
    elevs = []
    for item in stresses:
        elevs.append(item["elev"])
    return elevs


def parse_total_stress(stresses):
    """this function parses the values of total stresses"""
    # parsed_total_stresses = {}
    stress_values = []
    for item in stresses:
        stress_values.append(item["total_stress"])
    return stress_values


def parse_water_press(stresses):
    """this function parses the values of water pressure"""
    stress_values = []
    for item in stresses:
        stress_values.append(item["water_press"])
    return stress_values


def parse_eff_stress(stresses):
    """this function parses the values of effective stresses into list"""
    stress_values = []
    for item in stresses:
        stress_values.append(item["eff_stress"])
    return stress_values


def plot_soils_water(soils_data_set, water_data_set):
    plt.plot(water_data_set["hor"], water_data_set["ver_top"], 'b-')
    for data in soils_data_set:
        plt.plot(data["hor"], data["ver_top"], 'k--')
        plt.plot(data["hor"], data["ver_bot"], 'k--')
        plt.text(data["text_hor"], data["text_ver"], data["name"])


def plot_stresses(soils, water, stresses):
    """this function plots the overburden stresses"""
    total_stress = parse_total_stress(stresses)
    water_press = parse_water_press(stresses)
    eff_stress = parse_eff_stress(stresses)
    elevs = parse_elevs(stresses)
    #find max and min values of stresses
    stress_limits = {
        "min": min(total_stress + water_press + eff_stress),
        "max": max(total_stress + water_press + eff_stress)
    }
    hor_buffer = 10
    water_data_set = parse_water(water, stress_limits, hor_buffer)
    soils_data_set = parse_soils(soils, stress_limits, hor_buffer)
    #plot the data sets
    global figure_count
    figure_count += 1
    plt.figure(figure_count)
    #plot total stress
    plt.subplot(131)
    plot_soils_water(soils_data_set, water_data_set)
    plt.plot(total_stress, elevs)
    plt.ylabel('Elevation (m)')
    plt.xlabel('Total Stress (kPa)')
    #plot water press
    plt.subplot(132)
    plot_soils_water(soils_data_set, water_data_set)
    plt.plot(water_press, elevs)
    plt.xlabel('Water Press. (kPa)')
    #plot eff stress
    plt.subplot(133)
    plot_soils_water(soils_data_set, water_data_set)
    plt.plot(eff_stress, elevs)
    plt.xlabel('Eff. Stress (kPa)')
    # print("Close the plotter to continue")
    plt.ion()
    plt.show()




# elevs = [0, -2, -5, -10]
# total_stresses = [0, 10, 30, 90]
# water_press = [0, 10, 25, 50]
# ground_elev = 0

# min_x = min(total_stresses + water_press)
# max_x = max(total_stresses + water_press)
# min_y = min(elevs)
# max_y = max(elevs)

# ground_x = [min_x, max_x]
# ground_y = [ground_elev, ground_elev]

# plt.figure(1)

# plt.subplot(121)
# plt.plot(total_stresses, elevs, 'r-')
# plt.plot(ground_x, ground_y, 'k--')
# plt.text(10, ground_elev, 'ground')
# plt.ylabel('Elevation (m)')
# plt.xlabel('Total Stress (kPa)')

# plt.subplot(122)
# plt.plot(water_press, elevs, 'g-')
# # plt.ylabel('Elevation (m)')
# plt.xlabel('Water Pressure (kPa)')

# plt.show()