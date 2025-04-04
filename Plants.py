from GlobalVariables import periodic_func_summer, periodic_func_winter
#Makes herbivore class
class Plants:
    def __init__(self, density, growth_rate, equilibrium_density, max_rate_removal, cond_growth, cond_consumption):
        self.density = density
        self.growth_rate = growth_rate
        self.equilibrium_density = equilibrium_density
        self.max_rate_removal = max_rate_removal
        self.cond_growth = cond_growth
        self.cond_consumption = cond_consumption

    # gets the growth rate accounting for time differences, kg / (km^2 * yr)
    def find_effective_growth(self):
        return self.growth_rate*periodic_func_summer() * (self.equilibrium_density - self.density)

    # % of kg of Browse lost per every hare per year
    def find_plants_consumption(self, prey):
        return periodic_func_winter()*self.max_rate_removal*self.density*prey.density / (prey.half_saturation + self.density)

    def plant_derivative(self, prey):
        return self.find_effective_growth() - self.find_plants_consumption(prey)
