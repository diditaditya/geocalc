import copy, re
import file_browser.file_browser_controller as fb
import user_interface.ui_controller as view
from overburden import overburden_controller as ob
from overburden.data.soil_data import Soil_all, Soil_unit
from overburden.data.units import soil_params_units, stresses_units
import plotter.plotter_controller as plotter

soil_layers = Soil_all()

def soil_show_main_menu():
    while True:
        soils = soil_layers.get_soil_data()
        ground_water = ob.get_water_data()
        water_units = ob.get_water_units()
        view.show_soil_main_menu(soils, ground_water, water_units)
        user_input = input("Select menu number: ")
        if len(user_input) > 0:
            if int(user_input) == 8:
                break
            elif int(user_input) == 1:
                soil_show_add_new()
            elif int(user_input) == 2:
                soil_pick_layer_to_edit()
            elif int(user_input) == 3:
                soil_pick_layer_to_delete()
            elif int(user_input) == 4:
                soil_show_ground_water()
            elif int(user_input) == 5:
                soil_show_result()
            elif int(user_input) == 6:
                soil_save_data()
            elif int(user_input) == 7:
                soil_load_data()


def reset_temp_soil(new_soil_temp):
    new_soil_temp.id = None
    new_soil_temp.name = None
    new_soil_temp.top_elev = None
    new_soil_temp.bottom_elev = None
    new_soil_temp.sat_unit_weight = None
    new_soil_temp.moist_unit_weight = None


def soil_show_add_new():
    new_soil_temp = Soil_unit(None, None, None, None, None, None)
    while True:
        view.show_soil_add_new_menu(new_soil_temp, soil_layers.get_soil_data())
        user_input = input("Select menu number: ")
        pattern = r"-?[0-9]+"
        if len(user_input) > 0 and re.match(pattern, user_input):
            if int(user_input) == 7:
                reset_temp_soil(new_soil_temp)
                break
            elif int(user_input) == 1:
                soil_adjust_param(new_soil_temp, "name", "Soil Name", soil_params_units)
            elif int(user_input) == 2:
                soil_adjust_param(new_soil_temp, "top_elev", "Top Elevation",
                                soil_params_units)
            elif int(user_input) == 3:
                soil_adjust_param(new_soil_temp, "bottom_elev", "Bottom Elevation",
                                soil_params_units)
            elif int(user_input) == 4:
                soil_adjust_param(new_soil_temp, "sat_unit_weight", "Saturated Weight",
                                soil_params_units)
            elif int(user_input) == 5:
                soil_adjust_param(new_soil_temp, "moist_unit_weight", "Moist Unit Weight",
                                soil_params_units)
            elif int(user_input) == 6:
                name = new_soil_temp.name is not None
                top_elev = new_soil_temp.top_elev is not None
                bottom_elev = new_soil_temp.bottom_elev is not None
                sat_unit_weight = new_soil_temp.sat_unit_weight is not None
                moist_unit_weight = new_soil_temp.moist_unit_weight is not None
                if name and top_elev and bottom_elev and sat_unit_weight and moist_unit_weight:
                    new_soil = copy.deepcopy(new_soil_temp)
                    result = soil_submit_new_layer(new_soil)
                    if result["status"] == "success":
                        print("\n")
                        del new_soil_temp
                        break
                    else:
                        print("\n")
                        print(result["error"])
                else:
                    print("\n")
                    print("Soil layer data must not be empty")



def soil_adjust_param(soil, param, text, units):
    while True:
        view.show_soil_adjust_param(soil, param, text, units)
        user_input = input("Enter new value: ")
        pattern_elev = r"-?[0-9]+"
        pattern_param = r"[0-9]+"
        if len(user_input) > 0: #validation is required
            if param == "name":
                soil.name = user_input
            elif param == "top_elev":
                if re.match(pattern_elev, user_input):
                    soil.top_elev = float(user_input)
            elif param == "bottom_elev":
                if re.match(pattern_elev, user_input):
                    soil.bottom_elev = float(user_input)
            elif param == "sat_unit_weight":
                if re.match(pattern_param, user_input):
                    soil.sat_unit_weight = float(user_input)
            elif param == "moist_unit_weight":
                if re.match(pattern_param, user_input):
                    soil.moist_unit_weight = float(user_input)
        break

def soil_submit_new_layer(new_soil):
    # validation here prior to adding the soil
    new_soil.id = soil_layers.generate_new_id()
    return soil_layers.add_new_soil(new_soil)


def soil_pick_layer_to_edit():
    if len(soil_layers.get_soil_data()) > 0:
        while True:
            soils = soil_layers.get_soil_data()
            view.show_soil_pick_to_edit(soils)
            user_input = input("Choose soil layer to edit: ")
            #validate, here simple length check is used
            pattern = r"[0-9]+"
            layer_amount = len(soils)
            if len(user_input) > 0 and re.match(pattern, user_input):
                if int(user_input) <= layer_amount:
                    soil = soils[int(user_input) - 1]
                    soil_show_edit_layer(soil, soils)
                    break
    else:
        print("No soil data")

def soil_sumbit_editted_layer(editted_soil):
    return soil_layers.edit_soil(editted_soil)

def soil_show_edit_layer(soil, soils):
    temp_edit_soil = copy.deepcopy(soil)
    while True:
        view.show_soil_edit_menu(temp_edit_soil, soils)
        user_input = input("Select menu number: ")
        if len(user_input) > 0:
            if int(user_input) == 7:
                del temp_edit_soil
                break
            elif int(user_input) == 1:
                soil_adjust_param(temp_edit_soil, "name", "Soil Name", soil_params_units)
            elif int(user_input) == 2:
                soil_adjust_param(temp_edit_soil, "top_elev", "Top Elevation",
                                soil_params_units)
            elif int(user_input) == 3:
                soil_adjust_param(temp_edit_soil, "bottom_elev", "Bottom Elevation",
                                soil_params_units)
            elif int(user_input) == 4:
                soil_adjust_param(temp_edit_soil, "sat_unit_weight", "Saturated Weight",
                                soil_params_units)
            elif int(user_input) == 5:
                soil_adjust_param(temp_edit_soil, "moist_unit_weight", "Moist Unit Weight",
                                soil_params_units)
            elif int(user_input) == 6:
                result = soil_sumbit_editted_layer(temp_edit_soil)
                if result["status"] == "success":
                    del temp_edit_soil
                    break
                else:
                    print("\n")
                    print(result["error"])


def soil_show_confirm_delete_layer(soil):
    view.show_soil_confirm_delete(soil)
    pattern = r"[yn]"
    user_input = input("Are you sure you want to delete the layer? (y/n): ").lower()
    if re.match(pattern, user_input):
        if user_input == 'y':
            soil_layers.delete_soil(soil.id)


def soil_pick_layer_to_delete():
    if len(soil_layers.get_soil_data()) > 0:
        while True:
            soils = soil_layers.get_soil_data()
            view.show_soil_pick_to_delete(soils)
            user_input = input("Choose soil layer to delete (empty to cancel): ")
            #validate, here simple length check is used
            pattern = r"[0-9]+"
            layer_amount = len(soils)
            if len(user_input) > 0 and re.match(pattern, user_input):
                if int(user_input) <= layer_amount:
                    soil = soils[int(user_input) - 1]
                    soil_show_confirm_delete_layer(soil)
                    break
            else:
                break
    else:
        print("No soil data")

def soil_show_ground_water():
    while True:
        ground_water = ob.get_water_data()
        units = ob.get_water_units()
        view.show_soil_ground_water(ground_water, units)
        user_input = input("Enter menu number: ")
        pattern = r"[0-9]+"
        if len(user_input) > 0 and re.match(pattern, user_input):
            if int(user_input) == 3:
                break
            elif int(user_input) == 1:
                soil_show_edit_ground_water_params(ground_water, "elev", "Ground water elevation", units)
            elif int(user_input) == 2:
                soil_show_edit_ground_water_params(ground_water, "unit_weight", "Ground water unit weight", units)


def soil_show_edit_ground_water_params(ground_water, param, text, units):
    while True:
        view.show_soil_adjust_ground_water_params(ground_water, param, text, units)
        pattern = r"[0-9]+"
        if param == "elev":
            pattern = r"^-?[0-9]*"
        user_input = input("Enter new value (enter - for no water): ")
        if len(user_input) > 0 and re.match(pattern, user_input):
            if user_input == "-":
                user_input = None
            else:
                user_input = float(user_input)
            ground_water[param] = user_input
            break
        else:
            print("Wrong input value")


def soil_show_result():
    soils = soil_layers.get_soil_data()
    if len(soils) > 0:
        while True:
            ground_water = ob.get_water_data()
            water_elev = ground_water["elev"]
            if water_elev is None:
                bottom_soil_elev = (soils[len(soils)-1].get_soil_data())["bottom_elev"]
                water_elev = bottom_soil_elev
            new_water_data = copy.deepcopy(ground_water)
            new_water_data["elev"] = water_elev
            units = ob.get_stresses_units()
            stresses = ob.calculate_overburden(soils, new_water_data)
            view.show_soil_stresses(soils, stresses, units)
            plotter.plot_soil_stresses(soils, ground_water, stresses)
            input("Press enter to go back")
            break

    else:
        print("\n")
        print("No soil data")


def soil_save_data():
    user_input = input("Enter file name: ")
    soils = soil_layers.get_soil_data()
    ground_water = ob.get_water_data()
    stringified_data = fb.stringify_soil_data(soils, ground_water)
    fb.save_to_file(user_input, stringified_data)


def soil_load_data():
    files = sorted(fb.get_save_files())
    while True:
        view.show_saved_files(files)
        user_input = input("Enter file number to open (empty to cancel): ")
        if soil_load_data_is_input_valid(user_input, files):
            file_index = int(user_input)
            filename = files[file_index-1]
            try:
                raw_data = fb.open_save_file(filename)
                soil_data = fb.parse_soil_data(raw_data)
                water_data = fb.parse_water_data(raw_data)
                soil_layers.empty_soil_data()
                soil_layers.set_soil_data(ob.load_soil_data(soil_data))
                ob.update_water_data(water_data)
                break
            except:
                print("Not a valid geocalc save file")
        elif len(user_input) == 0:
            break
        else:
            print("Invalid input")


def soil_load_data_is_input_valid(user_input, file_list):
    pattern = r"^[0-9]+$"
    if len(user_input) > 0 and re.match(pattern, user_input):
        if int(user_input) <= len(file_list):
            return True
        else:
            return False
    else:
        return False

soil_show_main_menu()
