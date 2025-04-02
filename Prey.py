from entities import Entity
from GlobalVariables import periodic_func_summer, periodic_func_winter

class Prey(Entity):
    def __init__(self, density, max_recruitment_rate, starvation_mortality_rate, cond_dependence_mortality, half_sat):
        Entity.__init__(self, density)
        self.max_recruitment_rate = max_recruitment_rate
        self.starvation_mortality_rate = starvation_mortality_rate
        self.cond_dep_mortality = cond_dependence_mortality
        self.half_saturation = half_sat

    def prey_derivative(self, plant, predator):
        growth = self.max_recruitment_rate*periodic_func_summer()*plant.density*self.density/(self.half_saturation + plant.density)
        starvation = self.starvation_mortality_rate * (1 - self.cond_dep_mortality*plant.density/(self.half_saturation + plant.density))
        consumed = predator.max_kill_rate*self.density*predator.density/(predator.half_saturation + self.density)
        return growth - starvation - consumed
