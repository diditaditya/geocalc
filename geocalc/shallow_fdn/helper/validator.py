import re

def is_input_valid(input, menu):
    pattern = r"[0-9]+"
    if re.match(pattern, str(input)):
        if int(input) > 0 and int(input) <= len(menu):
            return True
        return False
    return False


def is_value_valid(value):
    pattern = r"[0-9]+"
    if re.match(pattern, str(value)):
        return True
    return False


def is_all_params_filled(soil, fdn):
    cohesion_ok = soil["cohesion"]["value"] != None
    friction_ok = soil["friction_angle"]["value"] != None
    weight_ok = soil["soil_weight"]["value"] != None
    if not (cohesion_ok and friction_ok and weight_ok):
        return {"status": False, "error": "Soil parameters are incomplete"}
    width_ok = fdn["width"]["value"] != None
    length_ok = fdn["length"]["value"] != None
    depth_ok = fdn["depth"]["value"] != None
    if not (width_ok and length_ok and depth_ok):
        return {
            "status": False,
            "error": "Foundation parameters are incomplete"
        }
    return {"status": True}