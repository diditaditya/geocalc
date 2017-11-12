"""Import mathematical functionality from math module."""
from math import pi, sin, cos, tan, atan, radians, sqrt, exp


class Factors:
    """The bearing capacity factors are based on Meyerhof (1963) recommendation."""

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
        self.Ngamma = (self.Nq - 1)*tan(1.4*self.phi)
        self.Fcs = 1 + 0.2*(self.Bf/self.Lf)
        self.Fqs = 1
        if (eff_friction_angle >= 10):
            self.Fcs = 1 + 0.2 * (
                self.Bf/self.Lf) * ((tan(radians(45)+(self.phi/2)))**2)
            self.Fqs = 1 + 0.1 * (self.Bf / self.Lf) * (
                (tan(radians(45) + (self.phi / 2)))**2)
        self.Fgammas = self.Fqs
        self.Fcd = 1 + 0.2 * (self.Df / self.Bf)
        self.Fqd = 1
        if (eff_friction_angle >= 10):
            self.Fcd = 1 + 0.2 * (
                self.Df / self.Bf)*tan(radians(45)+(self.phi/2))
            self.Fqd = 1 + 0.1 * (
                self.Df / self.Bf) * tan(radians(45) + (self.phi / 2))
        self.Fgammad = self.Fqd
        self.Fci = (1 - self.beta / 90)**2
        self.Fqi = self.Fci
        self.Fgammai = 1.0
        if (eff_friction_angle > 0):
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