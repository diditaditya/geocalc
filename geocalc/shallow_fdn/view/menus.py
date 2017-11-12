def home_screen(menu):
    print()
    print("===============================================")
    print("Shallow Foundation Bearing Capacity Calculator")
    print("===============================================")
    for x in range(0, len(menu)):
        print("{0}. {1}".format(x + 1, menu[x]))
    print("===============================================")



def show_params(params):
    for index, (key, value) in enumerate(params.items()):
        param_value = "-"
        if value["value"] != None:
            param_value = value["value"]
        print("{0}. {1}: {2} {3}".format(index + 1, value["text"], param_value,
                                         value["unit"]))


def soil_params_menu(params, menu):
    print()
    print("===============================================")
    print("               Soil Parameters")
    print("===============================================")
    show_params(params)
    print("===============================================")
    for x in range(0, len(menu)):
        print("{0}. {1}".format(x + 1, menu[x]))
    print("===============================================")



def fdn_dimensions_menu(params, menu):
    print()
    print("===============================================")
    print("             Foundation Parameters")
    print("===============================================")
    show_params(params)
    print("===============================================")
    for x in range(0, len(menu)):
        print("{0}. {1}".format(x + 1, menu[x]))
    print("===============================================")



def adjust_params_screen(params):
    print()
    print("===============================================")
    print("               {}".format(params["text"]))
    print("===============================================")
    shown_val = params["value"]
    if shown_val == None:
        shown_val = "-"
    print(
        "{0} = {1} {2}".format(params["text"], shown_val, params["unit"]))
    print("===============================================")


def calc_bearing_cap_screen(cap):
    while True:
        print()
        print("===============================================")
        print("              Bearing Capacities")
        print("===============================================")
        print("1. Bearing factors")
        print("   Nc = {}".format(round(cap["factors"].Nc, 3)))
        print("   Nq = {}".format(round(cap["factors"].Nq, 3)))
        print("   Ny = {}".format(round(cap["factors"].Ngamma, 3)))
        print("2. Shape factors")
        print("   Fcs = {}".format(round(cap["factors"].Fcs, 3)))
        print("   Fqs = {}".format(round(cap["factors"].Fqs, 3)))
        print("   Fys = {}".format(round(cap["factors"].Fgammas, 3)))
        print("3. Depth factors")
        print("   Fcd = {}".format(round(cap["factors"].Fcd, 3)))
        print("   Fqd = {}".format(round(cap["factors"].Fqd, 3)))
        print("   Fyd = {}".format(round(cap["factors"].Fgammas, 3)))
        print("4. Inclination factors")
        print("   Fci = {}".format(round(cap["factors"].Fci, 3)))
        print("   Fqi = {}".format(round(cap["factors"].Fqi, 3)))
        print("   Fyi = {}".format(round(cap["factors"].Fgammai, 3)))
        print("5. Bearing capacities")
        print("   qu   = {} kPa".format(round(cap["ultimate"], 3)))
        print("   qall = {} kPa".format(round(cap["allowable"], 3)))
        print("===============================================")
        user_input = input("Enter 1 to go back: ")
        if user_input == "1":
            break
        else:
            print("Wrong input")


def about_screen():
    while True:
        print()
        print("===============================================")
        print("            About This Tiny Program")
        print("===============================================")
        about_text = ("This is a very simple program to calculate\n"
                      "the very basic shallow foundation bearing\n"
                      "capacity. The calculation is based on Meyerhof\n"
                      "general bearing capacity formula.\n\n"
                      "Limitation:\n"
                      "Load inclination is assumed to be vertical in\n"
                      "this calculation and ground water is not taken\n"
                      "into account.\n\n"
                      "This may not replace your already sophisticated\n"
                      "spreadsheet. However, I hope this can still be\n"
                      "useful to some extent.\n"
                      "\ndiditaditya, 2017.")
        print(about_text)
        print("===============================================")
        user_input = input("Enter 1 to go back: ")
        if user_input == "1":
            break
        else:
            print("Wrong input")