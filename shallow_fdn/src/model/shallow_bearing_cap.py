import math
# import general_fdn_factors
# import meyerhof_factors

def bearing_capacity(cohesion, friction_angle, soil_weight, fdn_width, fdn_length, fdn_depth, factors, load_inclination=0):
    q = soil_weight*fdn_depth
    cohesion_contribution = cohesion*factors.Nc*factors.Fcs*factors.Fcd*factors.Fci
    weight_contribution = q*factors.Nq*factors.Fqs*factors.Fqd*factors.Fqi
    friction_contribution = 0.5*soil_weight*fdn_width*factors.Ngamma*factors.Fgammas*factors.Fgammad*factors.Fgammai
    return cohesion_contribution+weight_contribution+friction_contribution


# cohesion = 15.2
# friction_angle = 20
# unit_weight = 17.8
# width = 1.5
# length = 1.5
# depth = 1
# SF = 4

# # factors = general_fdn_factors.Factors(friction_angle, width, length, depth)
# factors = meyerhof_factors.Factors(friction_angle, width, length, depth)

# ultimate_capacity = bearing_capacity(cohesion, friction_angle, unit_weight, width, length, depth, factors)
# allowable_capacity = ultimate_capacity/SF

# print("Nc: {}".format(factors.Nc))
# print("Nq: {}".format(factors.Nq))
# print("Ngamma: {}".format(factors.Ngamma))
# print("Ultimate capacity: {} kPa".format(ultimate_capacity))
# print("Allowable capacity: {} kPa".format(allowable_capacity))