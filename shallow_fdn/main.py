"""import the program controller"""
import src.shallow_fdn_control as control

while True:
    control.show_main_menu()
    user_input = control.main_menu_get_user_input()
    if user_input:
        if user_input == 6:
            break
        elif user_input == 1:
            control.show_soil_menu()
        elif user_input == 2:
            control.show_fdn_menu()
        elif user_input == 3:
            control.show_sf_screen()
        elif user_input == 4:
            control.show_calculation_result()
        elif user_input == 5:
            control.show_about()