def show_soils(soils):
    """function to show soil layers."""
    if len(soils) > 0:
        print("No.\tName\t\tTop El.(m)\tBott El.(m)\tysat(kN/m3)\tym(kN/m3)")
        for index, soil in enumerate(soils):
            # print(soil)
            if len(soil.name) > 8:
                print("{0}.\t{1}\t{2}\t\t{3}\t\t{4}\t\t{5}".format(
                    index + 1, soil.name, soil.top_elev, soil.bottom_elev,
                    soil.sat_unit_weight, soil.moist_unit_weight))
            else:
                print("{0}.\t{1}\t\t{2}\t\t{3}\t\t{4}\t\t{5}".format(
                    index + 1, soil.name, soil.top_elev, soil.bottom_elev,
                    soil.sat_unit_weight, soil.moist_unit_weight))
    else:
        print("No soil data")


def main_menu(soils, ground_water, units, menu):
    """function to show the main menu of soil data."""
    print()
    print("=========================================================================================")
    print("                                      Soil Layers")
    print("=========================================================================================")
    show_soils(soils)
    print("=========================================================================================")
    show_ground_water(ground_water, units)
    print("=========================================================================================")
    for x in range(0, len(menu)):
        print("{0}. {1}".format(x + 1, menu[x]))
    print("=========================================================================================")


def show_soil(soil):
    soil_name = "-"
    soil_top_elev = "-"
    soil_bottom_elev = "-"
    soil_sat_unit_weight = "-"
    soil_moist_unit_weight = "-"
    if soil.name != None :
        soil_name = soil.name
    if soil.top_elev != None:
        soil_top_elev = soil.top_elev
    if soil.bottom_elev != None:
        soil_bottom_elev = soil.bottom_elev
    if soil.sat_unit_weight != None:
        soil_sat_unit_weight = soil.sat_unit_weight
    if soil.moist_unit_weight != None:
        soil_moist_unit_weight = soil.moist_unit_weight
    print("Soil Name: {}".format(soil_name))
    print("Top elevation: {} m".format(soil_top_elev))
    print("Bottom elevation: {} m".format(soil_bottom_elev))
    print("Saturated unit weight: {} kN/m3".format(soil_sat_unit_weight))
    print("Moist unit weight: {} kN/m3".format(soil_moist_unit_weight))


def add_new_soil_menu(soil, soils, menu):
    """function to show the add new soil menu."""
    print()
    print("=========================================================================================")
    print("                                 Add New Soil Layer")
    print("=========================================================================================")
    show_soils(soils)
    print("=========================================================================================")
    show_soil(soil)
    print("=========================================================================================")
    for x in range(0, len(menu)):
        print("{0}. {1}".format(x + 1, menu[x]))
    print("=========================================================================================")


def edit_soil_menu(soil, soils, menu):
    """function to show the edit soil menu."""
    print()
    print("=========================================================================================")
    print("                                   Edit Soil Layer")
    print("=========================================================================================")
    show_soils(soils)
    print("=========================================================================================")
    show_soil(soil)
    print("=========================================================================================")
    for x in range(0, len(menu)):
        print("{0}. {1}".format(x + 1, menu[x]))
    print("=========================================================================================")


def pick_soil_to_edit(soils):
    """function to show the screen to select the layer to edit."""
    print()
    print("=========================================================================================")
    print("                                Choose Layer to Edit")
    print("=========================================================================================")
    show_soils(soils)
    print("=========================================================================================")


def pick_soil_to_delete(soils):
    """function to show the screen to select the layer to delete."""
    print()
    print("=========================================================================================")
    print("                                Choose Layer to Delete")
    print("=========================================================================================")
    show_soils(soils)
    print("=========================================================================================")


def adjust_soil_params_screen(soil, param, text, units):
    print()
    print("===============================================")
    print("              Edit {}".format(text))
    print("===============================================")
    soil_data = soil.get_soil_data()
    shown_val = soil_data[param]
    if shown_val == None:
        shown_val = "-"
    print("{0} = {1} {2}".format(text, shown_val, units[param]))
    print("===============================================")


def confirm_soil_to_delete(soil):
    """function to show the confirmation screen to select the layer to delete."""
    print()
    print("=========================================================================================")
    print("                                Delete {}?".format(soil.name))
    print("=========================================================================================")
    show_soil(soil)
    print("=========================================================================================")


def show_ground_water(ground_water, units):
    """function to show ground water data"""
    elev = ground_water["elev"]
    unit_weight = ground_water["unit_weight"]
    if elev is None:
        elev = "-"
    print("Ground water elevation: {0} {1}".format(elev, units["elev"]))
    print("Ground water unit weight: {0} {1}".format(unit_weight, units["unit_weight"]))


def ground_water_menu(ground_water, units, menu):
    """function to show the ground-water menu."""
    print()
    print("=========================================================================================")
    print("                                 Edit Ground Water")
    print("=========================================================================================")
    show_ground_water(ground_water, units)
    print("=========================================================================================")
    for x in range(0, len(menu)):
        print("{0}. {1}".format(x + 1, menu[x]))
    print("=========================================================================================")


def adjust_ground_water_params_screen(ground_water, param, text, units):
    print()
    print("===============================================")
    print("              Edit {}".format(text))
    print("===============================================")
    shown_val = ground_water[param]
    if shown_val is None:
        shown_val = "-"
    print("{0} = {1} {2}".format(text, shown_val, units[param]))
    print("===============================================")


def show_stresses(soils, stresses, units):
    """function to show soil stress calculation result."""
    if len(stresses) > 0:
        print("No.\tEl ({0})\tSoil Layer\tTotal({1})\tWater({1})\tEffective({1})".format(units["elev"], units["stress"]))
        for index, stress in enumerate(stresses):
            soil_id = stress["soil_id"]
            soil_name = None
            for soil in soils:
                if soil.id == soil_id:
                    soil_name = soil.name
            if soil_name is None:
                soil_name = "None"
            if len(soil_name) > 8:
                print("{0}.\t{1}\t{2}\t\t{3}\t\t{4}\t\t{5}".format(
                    index + 1, stress["elev"], soil_name, stress["total_stress"], stress["water_press"], stress["eff_stress"]))
            else:
                print("{0}.\t{1}\t{2}\t\t{3}\t\t{4}\t\t{5}".format(
                    index + 1, stress["elev"], soil_name, stress["total_stress"], stress["water_press"], stress["eff_stress"]))
    else:
        print("No soil data")


def stresses_result(soils, stresses, units):
    """function to show the main menu of soil data."""
    print()
    print("=========================================================================================")
    print("                               Soil Overburden Stresses")
    print("=========================================================================================")
    show_stresses(soils, stresses, units)
    print("=========================================================================================")


def saved_files(file_list):
    """function to show the main menu of soil data."""
    print()
    print("=========================================================================================")
    print("                                       Open File")
    print("=========================================================================================")
    show_files(file_list)
    print("=========================================================================================")


def show_files(file_list):
    if len(file_list) > 0:
        for index, file in enumerate(sorted(file_list)):
            print("{0}. {1}".format(index+1, file))
    else:
        print("Save file is not found")