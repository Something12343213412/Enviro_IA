from entities import Entity
#Makes herbivore class
class Plants(Entity):
    def __init__(self, density, growth_rate, equilibrium_density, max_rate_removal, half_saturation, cond_growth, cond_consumption):
        Entity.__init__(self, density)
        self.growth_rate = growth_rate
        self.equilibrium_density = equilibrium_density
        self.max_rate_removal = max_rate_removal
        self.half_saturation = half_saturation
        self.cond_growth = cond_growth
        self.cond_consumption = cond_consumption

    # gets the growth rate accounting for time differences, kg / (km^2 * yr)
    def find_effective_growth(self, browse_density, time):

