from entities import Entity

class Prey(Entity):
    def __init__(self, density, recruitment_rate, starvation_mortality_rate, cond_dependence_mortality, half_sat):
        Entity.__init__(self, density)
        self.recruitment_rate = recruitment_rate
        self.starvation_mortality_rate = starvation_mortality_rate
        self.cond_dep_mortality = cond_dependence_mortality
        self.half_saturation = half_sat

