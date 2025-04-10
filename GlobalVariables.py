from math import sin, pi

time = 0


def periodic_func_summer(seasonality_herb_growth=1):
    global time
    #return 1 + seasonality_herb_growth * sin(time*2*pi)
    return 1

def periodic_func_winter(seasonality_prey_consumption=.7):
    global time
    #return 1 - seasonality_prey_consumption * sin(time*2*pi)
    return 1
