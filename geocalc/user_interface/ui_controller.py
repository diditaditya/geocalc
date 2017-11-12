"""import views"""
import user_interface.view.menus as menus
import user_interface.view.soil_menus as soil_menus

"""import lists of the menus"""
import user_interface.data.menu_lists as menu_lists

def show_soil_main_menu(soils, ground_water, units):
    soil_menus.main_menu(soils, ground_water, units, menu_lists.soil_main_menu)


def show_soil_add_new_menu(soil, soils):
    soil_menus.add_new_soil_menu(soil, soils, menu_lists.soil_add_new_menu)


def show_soil_edit_menu(soil, soils):
    soil_menus.edit_soil_menu(soil, soils, menu_lists.soil_edit_menu)


def show_soil_pick_to_edit(soils):
    soil_menus.pick_soil_to_edit(soils)


def show_soil_adjust_param(soil, param, text, units):
    soil_menus.adjust_soil_params_screen(soil, param, text, units)


def show_soil_pick_to_delete(soils):
    soil_menus.pick_soil_to_delete(soils)


def show_soil_confirm_delete(soil):
    soil_menus.confirm_soil_to_delete(soil)


def show_soil_ground_water(ground_water, units):
    soil_menus.ground_water_menu(ground_water, units, menu_lists.water_main_menu)


def show_soil_adjust_ground_water_params(ground_water, param, text, units):
    soil_menus.adjust_ground_water_params_screen(ground_water, param, text, units)


def show_soil_stresses(soils, stresses, units):
    soil_menus.stresses_result(soils, stresses, units)


def show_saved_files(file_list):
    soil_menus.saved_files(file_list)