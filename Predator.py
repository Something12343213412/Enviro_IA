from entities import Entity
from GlobalVariables import periodic_func_summer
class Predator(Entity):
    def __init__(self, density, recruitment_rate, max_kill_rate, half_saturation, cond_dep_mortality):
        Entity.__init__(self, density)
        self.recruitment_rate = recruitment_rate
        self.max_kill_rate = max_kill_rate
        self.half_saturation = half_saturation
        self.cond_dep_mortality = cond_dep_mortality

    def find_predator_derivative(self, prey):
        growth = self.recruitment_rate*periodic_func_summer()*prey.density*self.density / (self.half_saturation + prey.density)
        starvation = self.cond_dep_mortality*periodic_func_summer()*prey.density*self.density/(self.half_saturation + prey.density) * self.density

