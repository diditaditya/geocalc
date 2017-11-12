"""Import trigonometry functionality from math module."""
from math import sin, cos, radians, sqrt

def at_rest(eff_friction):
    "This function returns at rest pressure based on Jacky, 1944."
    return 1 - sin(radians(eff_friction))

def at_rest_2(eff_friction):
    "This function returns at rest pressure based on Brooker and Ireland, 1965."
    return 0.95 - sin(radians(eff_friction))

def rankine_active(eff_friction, backfill_inclination=0):
    """This function returns active earth pressure based on Rankine for granular soil,
       where the wall is assumed to be vertical. The backfill inclination is taken
       with respect to horizontal."""
    phi = radians(eff_friction) #trigonometry in math module uses radians
    alpha = radians(backfill_inclination)
    reducer = sqrt((cos(alpha))**2 - (cos(phi))**2)
    upper_right = cos(alpha) - reducer
    lower_right = cos(alpha) + reducer
    return cos(alpha) * (upper_right/lower_right)

def rankine_passive(eff_friction, backfill_inclination=0):
    """This function returns passive earth pressure based on Rankine for granular soil,
       where the wall is assumed to be vertical. The backfill inclination is taken
       with respect to horizontal."""
    phi = radians(eff_friction)  #trigonometry in math module uses radians
    alpha = radians(backfill_inclination)
    reducer = sqrt((cos(alpha))**2 - (cos(phi))**2)
    upper_right = cos(alpha) + reducer
    lower_right = cos(alpha) - reducer
    return cos(alpha) * (upper_right / lower_right)

def coulomb_active(eff_friction, wall_angle, backfill_inclination=0, wall_friction_coeff=2/3):
    """This function returns active earth pressure based on Coulomb for granular soil.
       The wall angle is 90 for vertical wall, while the backfill is taken with respect
       to horizontal hence 0 is for horizontal backfill."""
    phi = radians(eff_friction)
    beta = radians(wall_angle)
    alpha = radians(backfill_inclination)
    delta = radians(wall_friction_coeff*eff_friction)
    top_eq = (sin(beta + phi))**2
    bottom_right = (1 + sqrt((sin(phi+delta)*sin(phi-alpha))/(sin(beta-delta)*sin(alpha+beta))))**2
    bottom_eq = (sin(beta))**2 * sin(beta-delta) * bottom_right
    return top_eq/bottom_eq

def coulomb_passive(eff_friction, wall_angle, backfill_inclination=0, wall_friction_coeff=2/3):
    """This function returns passive earth pressure based on Coulomb for granular soil.
       The wall angle is 90 for vertical wall, while the backfill is taken with respect
       to horizontal hence 0 is for horizontal backfill."""
    phi = radians(eff_friction)
    beta = radians(wall_angle)
    alpha = radians(backfill_inclination)
    delta = radians(wall_friction_coeff*eff_friction)
    top_eq = (sin(beta - phi))**2
    bottom_right = (1 - sqrt((sin(phi+delta)*sin(phi+alpha))/(sin(beta+delta)*sin(alpha+beta))))**2
    bottom_eq = (sin(beta))**2 * sin(beta+delta) * bottom_right
    return top_eq/bottom_eq

# friction_angle = float(input("Effective angle of internal friction: "))
# print("Coulomb active coefficient: {}".format(coulomb_active(friction_angle, 90)))
# print("Coulomb passive coefficient: {}".format(coulomb_passive(friction_angle, 90)))