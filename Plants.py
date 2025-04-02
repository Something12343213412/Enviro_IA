from entities import Entity
from GlobalVariables import periodic_func_summer
#Makes herbivore class
class Plants(Entity):
    def __init__(self, density, growth_rate, equilibrium_density, max_rate_removal, cond_growth, cond_consumption):
        Entity.__init__(self, density)
        self.growth_rate = growth_rate
        self.equilibrium_density = equilibrium_density
        self.max_rate_removal = max_rate_removal
        self.cond_growth = cond_growth
        self.cond_consumption = cond_consumption

    # gets the growth rate accounting for time differences, kg / (km^2 * yr)
    def find_effective_growth(self):
        return self.growth_rate*periodic_func_summer(self.cond_growth)*(self.equilibrium_density - self.density)

    def find_browse_consumption(self, prey):
        return (self.density*self.max_rate_removal) / (prey.half_saturation + self.density) *

