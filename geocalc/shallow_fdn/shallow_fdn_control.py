"""import soil, foundation, and safety factor parameters"""
from shallow_fdn.data.soil import soil_params
from shallow_fdn.data.foundation import fdn_dimensions
from shallow_fdn.data.safety_factor import safety_factor

"""import calculation models"""
from shallow_fdn.model.meyerhof_factors import Factors
from shallow_fdn.model.shallow_bearing_cap import bearing_capacity

"""import views"""
import shallow_fdn.view.menus as menus

"""import lists of the menus"""
from shallow_fdn.data.menu_lists import home_screen_menu, soil_screen_menu, fdn_screen_menu

"""import validator from helper"""
from shallow_fdn.helper.validator import is_all_params_filled, is_input_valid, is_value_valid


def show_main_menu():
    menus.home_screen(home_screen_menu)


def main_menu_get_user_input():
    user_input = input("Please enter the menu number: ")
    if is_input_valid(user_input, home_screen_menu):
        return int(user_input)
    else:
        print("\nWrong Input")
        return False


def show_soil_menu():
    while True:
        params = soil_params
        menu = soil_screen_menu
        menus.soil_params_menu(params, menu)
        user_input = input("Please enter the menu number: ")
        if is_input_valid(user_input, menu):
            if int(user_input) == 4:
                break
            elif int(user_input) == 1:
                show_adjust_screen(params["cohesion"])
            elif int(user_input) == 2:
                show_adjust_screen(params["friction_angle"])
            elif int(user_input) == 3:
                show_adjust_screen(params["soil_weight"])
        else:
            print("\nWrong Input")


def show_fdn_menu():
    while True:
        params = fdn_dimensions
        menu = fdn_screen_menu
        menus.fdn_dimensions_menu(params, menu)
        user_input = input("Please enter the menu number: ")
        if is_input_valid(user_input, menu):
            if int(user_input) == 4:
                break
            elif int(user_input) == 1:
                show_adjust_screen(params["width"])
            elif int(user_input) == 2:
                show_adjust_screen(params["length"])
            elif int(user_input) == 3:
                show_adjust_screen(params["depth"])
        else:
            print("\nWrong Input")


def show_sf_screen():
    params = safety_factor
    show_adjust_screen(params)


def show_adjust_screen(params):
    while True:
        menus.adjust_params_screen(params)
        user_input = input("Enter new value: ")
        if is_value_valid(user_input):
            params["value"] = float(user_input)
            break
        else:
            print("\nWrong input")


def show_calculation_result():
    params_check = is_all_params_filled(soil_params, fdn_dimensions)
    if params_check["status"]:
        cap = calc_bearing_cap(soil_params, fdn_dimensions, safety_factor["value"])
        menus.calc_bearing_cap_screen(cap)
    else:
        print("\n")
        print(params_check["error"])


def calc_bearing_cap(soil, fdn, sf):
    cohesion = soil["cohesion"]["value"]
    friction_angle = soil["friction_angle"]["value"]
    unit_weight = soil["soil_weight"]["value"]
    fdn_width = fdn["width"]["value"]
    fdn_length = fdn["length"]["value"]
    fdn_depth = fdn["depth"]["value"]
    factors = Factors(friction_angle, fdn_width, fdn_length,
                                       fdn_depth)
    ult_cap = bearing_capacity(cohesion, friction_angle, unit_weight,
                               fdn_width, fdn_length, fdn_depth, factors)
    capacities = {
        "factors": factors,
        "ultimate": ult_cap,
        "allowable": ult_cap / sf,
    }
    return capacities

def show_about():
    menus.about_screen()
