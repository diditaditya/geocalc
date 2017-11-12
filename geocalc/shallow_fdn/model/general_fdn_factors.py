"""Import mathematical functionality from math module."""
from math import pi, sin, cos, tan, atan, radians, sqrt, exp


class Factors:
    """The bearing capacity factors are based on general bearing capacity equation,
       Nc is as proposed by Prandtl (1921), Nq is by Reissner (1924),
       and Ngamma is by Caquot and Kerisel (1953).
       The shape factors Fcs, Fqs, Fgammas are based on De Beer (1970) recommendation.
       The depth factors Fcd, Fqd, Fgammad are based on Hansen (1970) recommendation.
       The inclination factors Fci, Fqi, Fgammai are based on Meyerhof (1963) and
       Hanna and Meyerhof (1981) recommendation."""

    def __init__(self,
                 eff_friction_angle,
                 width,
                 length,
                 depth,
                 load_inclination=0):
        self.phi = radians(eff_friction_angle)
        self.Bf = min([width, length])
        self.Lf = max([width, length])
        self.Df = depth
        self.beta = load_inclination
        self.Nq = exp(pi * tan(self.phi)) * (
            tan(radians(45) + (self.phi / 2)))**2
        self.Nc = 5.14
        if (eff_friction_angle > 0):
            self.Nc = (self.Nq - 1) * (1 / tan(self.phi))
        self.Ngamma = 2 * (self.Nq + 1) * tan(self.phi)
        self.Fcs = 1 + (self.Bf / self.Lf) * (self.Nq / self.Nc)
        self.Fqs = 1 + (self.Bf / self.Lf) * tan(self.phi)
        self.Fgammas = 1 - 0.4 * (self.Bf / self.Lf)
        self.Fcd = 1 + 0.4 * (self.Df / self.Bf)
        self.Fqd = 1 + 2 * tan(self.phi) * (
            (1 - sin(self.phi))**2) * (self.Df / self.Bf)
        self.Fgammad = 1
        if (self.Df / self.Bf > 1):
            self.Fcd = 1 + 0.4 * atan(self.Df / self.Bf)
            self.Fqd = 1 + 2 * tan(self.phi) * (
                (1 - sin(self.phi))**2) * atan(self.Df / self.Bf)
        self.Fci = (1 - self.beta / 90)**2
        self.Fqi = self.Fci
        self.Fgammai = (1 - self.beta / eff_friction_angle)**2


# friction_angle = float(input("Angle of internal friction: "))
# fdn_width = float(input("Foundation width: "))
# fdn_length = float(input("Foundation length: "))
# fdn_depth = float(input("Foundation depth: "))
# load_incl = float(input("Load inclination with respect to vertical: "))
# factors = Factors(friction_angle, fdn_width, fdn_length, fdn_depth, load_incl)
# print("Nc = {}".format(factors.Nc))
# print("Nq = {}".format(factors.Nq))
# print("Ngamma = {}".format(factors.Ngamma))
# print("Fcs = {}".format(factors.Fcs))
# print("Fqs = {}".format(factors.Fqs))
# print("Fgammas = {}".format(factors.Fgammas))
# print("Fcd = {}".format(factors.Fcd))
# print("Fqd = {}".format(factors.Fqd))
# print("Fgammad = {}".format(factors.Fgammad))
# print("Fci = {}".format(factors.Fci))
# print("Fqi = {}".format(factors.Fqi))
# print("Fgammai = {}".format(factors.Fgammai))