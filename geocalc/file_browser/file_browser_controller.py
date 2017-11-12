"""import os and regex module"""
import os, re

current_file = None


def get_dir():
    """this function gets the directory of the app"""
    folder_path = os.getcwd()
    # parent_path = os.path.join(folder_path, os.pardir)
    return str(folder_path) + "/"


def stringify_soil_data(soils, ground_water):
    """this function turns the soil and water data into string"""
    stringified = []
    stringified.append("SOIL LAYERS")
    for soil in soils:
        soil_data = []
        soil_data.append("id={}".format(soil.id))
        soil_data.append("name={}".format(soil.name))
        soil_data.append("top_elev={}".format(soil.top_elev))
        soil_data.append("bottom_elev={}".format(soil.bottom_elev))
        soil_data.append("sat_unit_weight={}".format(soil.sat_unit_weight))
        soil_data.append("moist_unit_weight={}".format(soil.moist_unit_weight))
        stringified_soil_data = "\n".join(soil_data)
        stringified.append(stringified_soil_data)
        stringified.append("-----")
    water_data = [
        "elev={}".format(ground_water["elev"]),
        "unit_weight={}".format(ground_water["unit_weight"])
        ]
    stringified.append("GROUND WATER")
    stringified.append("\n".join(water_data))
    return "\n".join(stringified)


def parse_soil_data(data):
    """this function prepares a dictionary to be used in insantiating soil layers"""
    water_index = data.index("GROUND WATER")
    raw_soils = data[1:water_index]
    separated_soils = []
    for item in raw_soils:
        if item == "-----":
            # print("----- found, creates new list")
            separated_soils.append([])
    index = 0
    for item in raw_soils:
        if item != "-----":
            # print("goes to separared_soils[{}]".format(index))
            separated_soils[index].append(item)
        else:
            # print("increase index")
            index = index + 1
    soils = []
    for item in separated_soils:
        soil = {}
        for param in item:
            separated_params = param.split("=")
            param_key = separated_params[0]
            param_value = separated_params[1]
            if param_key == "id":
                param_value = int(param_value)
            elif param_key == "name":
                param_value = str(param_value)
            else:
                param_value = float(param_value)
            soil[param_key] = param_value
        soils.append(soil)
    return soils

def parse_water_data(data):
    """this function prepares a dictionary to be used as ground water data"""
    water_index = data.index("GROUND WATER")
    raw_water = data[water_index + 1:]
    ground_water = {}
    for param in raw_water:
        separated_params = param.split("=")
        param_key = separated_params[0]
        param_value = separated_params[1]
        if param_value == "None":
            param_value = None
        else:
            param_value = float(param_value)
        ground_water[param_key] = param_value
    return ground_water


def save_to_file(filename, data):
    """this function saves the data to a txt file in the directory where the app is in"""
    parent_dir = get_dir()
    file_path = parent_dir + filename + ".txt"
    try:
        if check_file_exist(file_path):
            print("file already exists")
            while True:
                user_input = input("Do you want to overwrite the file? (y/n)")
                if user_input.lower() == "y":
                    myfile = open(file_path, "w")
                    myfile.write(data)
                    myfile.close()
                    print("soil data has been saved to {}.txt".format(filename))
                    break
                elif user_input.lower() == "n":
                    break
                else:
                    print("wrong input")
        else:
            myfile = open(file_path, "w")
            myfile.write(data)
            myfile.close()
            print("soil data has been saved to {}.txt".format(filename))
    except:
        print("an error occured")
        raise


def check_file_exist(file_path):
    """this functions checks whether the save-file name exists """
    try:
        os.stat(file_path)
        return True
    except:
        print("file is not found, creating new file..")
        return False


def get_save_files():
    """this function list all files -in the directory of the app- which ends with .txt"""
    dir_path = get_dir()
    files = os.listdir(dir_path)
    save_files = []
    for file in files:
        if file.endswith(".txt"):
            save_files.append(file)
    return save_files


def open_save_file(filename):
    """this function open the data from a txt file in the directory where the app is in"""
    parent_dir = get_dir()
    file_path = parent_dir + filename
    try:
        save_file = open(file_path, "r")
        lines = save_file.read().splitlines()
        save_file.close()
        print("data from {} is loaded".format(filename))
        return lines
    except:
        print("an error occured")



# data = "aiueo aiueo\nabcde abcde\nqwerty qwerty"
# save_to_file('save1', data)

# folder_path = get_dir()
# file_list = get_save_files(folder_path)
# print(file_list)

# open_save_file("save1")