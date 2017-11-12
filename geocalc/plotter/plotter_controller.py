"""import overburden plotter"""
import plotter.overburden.ob_plotter as ob


def plot_soil_stresses(soils, water, stresses):
    ob.plot_stresses(soils, water, stresses)