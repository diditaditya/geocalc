import copy

class Soil_all:
    """This class will hold all soil unit data, which is basically a list of soil objects"""
    def __init__(self):
        self.soil_data = []

    def get_soil_data(self):
        sorted_data = sorted(
            self.soil_data, key=lambda soil: soil.top_elev, reverse=True)
        return sorted_data

    def generate_new_id(self):
        max_id = len(self.soil_data) + 1
        for soil in self.soil_data:
            if soil.id >= max_id:
                max_id = soil.id + 1
        return max_id

    def add_new_soil(self, new_soil):
        if new_soil.top_elev < new_soil.bottom_elev:
            return {"status": "failed", "error": "Top depth must be higher than bottom depth"}
        depth_check = self.is_depth_ok(new_soil)
        if depth_check["status"]:
            self.soil_data.append(new_soil)
            return {"status": "success", "data": self.soil_data}
        else:
            return {"status": "failed", "error": "Soil depth is conflicting", "conflicts": depth_check["conflicts"]}

    def get_soil_by_id(self, soil_id):
        selected_soil = None
        for soil in self.soil_data:
            if soil.id == soil_id:
                selected_soil = soil
        if selected_soil is None:
            return {"status": "failed", "error": "Soil is not found"}
        else:
            return {"status": "success", "data": selected_soil}

    def edit_soil(self, editted_soil):
        selected_soil = None
        selected_index = None
        for index, soil in enumerate(self.soil_data):
            if soil.id == editted_soil.id:
                selected_soil = soil
                selected_index = index
        if selected_soil is None or selected_index is None:
            return {"status": "failed", "error": "Soil is not found"}
        else:
            self.soil_data[selected_index] = editted_soil
            return {"status": "success", "data": editted_soil}

    def delete_soil(self, soil_id):
        soil_index = None
        for index, soil in enumerate(self.soil_data):
            if soil.id == soil_id:
                soil_index = index
        del self.soil_data[soil_index]
        if soil_index == None:
            return {"status": "failed", "error": "Soil id is not found"}
        return {"status": "success", "data": self.soil_data}
    
    def is_depth_ok(self, new_soil):
        conflicts = []
        if len(self.soil_data) > 0:
            for soil in self.soil_data:
                if new_soil.top_elev > soil.bottom_elev:
                    if new_soil.bottom_elev < soil.top_elev:
                        conflicts.append(soil.id)
                # if new_soil.bottom_elev < soil.top_elev:
                #     conflict.append(soil.id)
        if len(conflicts) == 0:
            return {"status": True}
        else:
            return {"status": False, "conflicts": conflicts}
    
    def set_soil_data(self, saved_soils):
        self.soil_data = saved_soils
        return self.get_soil_data()

    def empty_soil_data(self):
        self.soil_data = []
        return self.get_soil_data()

    def __str__(self):
        presentable_data = []
        sorted_data = sorted(self.soil_data, key=lambda soil: soil.top_elev, reverse=True)
        for soil in sorted_data:
            presentable_data.append(str(soil))
        return str(presentable_data)



class Soil_unit:
    """This class acts as a template for the soil unit data"""
    def __init__(self, soil_id, name, top_elev, bottom_elev, sat_weight, moist_weight):
        self.id = soil_id
        self.name = name
        self.top_elev = top_elev
        self.bottom_elev = bottom_elev
        self.sat_unit_weight = sat_weight
        self.moist_unit_weight = moist_weight

    def get_soil_data(self):
        data = {
            "id": self.id,
            "name": self.name,
            "top_elev": self.top_elev,
            "bottom_elev": self.bottom_elev,
            "sat_unit_weight": self.sat_unit_weight,
            "moist_unit_weight": self.moist_unit_weight
        }
        return data

    def __str__(self):
        data = {
            "id": self.id,
            "name": self.name,
            "top_elev": self.top_elev,
            "bottom_elev": self.bottom_elev,
            "sat_unit_weight": self.sat_unit_weight,
            "moist_unit_weight": self.moist_unit_weight
        }
        return str(data)



# soil_layers = Soil_all()
# soil_1 = Soil_unit(1, "soil a", 0, -2, 20, 18)
# soil_2 = Soil_unit(2, "soil b", -2, -4, 18, 16)
# soil_3 = Soil_unit(3, "soil c", -3, -1, 19, 17)
# # print(soil_1)
# # print(soil_1.id)
# print(soil_layers.add_new_soil(soil_2))
# print(soil_layers.add_new_soil(soil_1))
# print(soil_layers.add_new_soil(soil_3))

# print(soil_layers)
# # print(soil_layers.get_soil_data()[0].name)