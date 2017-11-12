"""import soil and ground water data template"""
from data.ground_water_data import ground_water
from data.soil_data import Soil_unit, Soil_all

"""import overburden stresses calculation model"""
from model.overburden import total_all, water_pressure, effective, stresses_arbitrary


# driver code
soil_layers = Soil_all()
soil_1 = Soil_unit(1, "soil a", 0, -2, 20, 10)
soil_2 = Soil_unit(2, "soil b", -2, -4, 18, 16)
soil_3 = Soil_unit(3, "soil c", -4, -5, 19, 17)
soil_layers.add_new_soil(soil_1)
soil_layers.add_new_soil(soil_2)
soil_layers.add_new_soil(soil_3)
# print(soil_layers)

ground_water["elev"] = 1
# print(ground_water)

surcharge = 0
if ground_water["elev"] > soil_layers.get_soil_data()[0].top_elev:
    surcharge = (ground_water["elev"] - soil_layers.get_soil_data()[0].top_elev) * ground_water["unit_weight"]
total = total_all(soil_layers.get_soil_data(), ground_water, surcharge)
print("total stresses")
for index, item in enumerate(total):
    print(index, item)

hydrostatic = water_pressure(soil_layers.get_soil_data(), ground_water)
print("\nhydrostatic")
for index, item in enumerate(hydrostatic):
    print(index, item)

eff_stress = effective(total, hydrostatic)
print("\neffective stresses")
for index, item in enumerate(eff_stress):
    print(index, item)

arb_elev = -7
print("\nstresses at elev {}".format(arb_elev))
stresses_arb = stresses_arbitrary(eff_stress, arb_elev)
print(stresses_arb)