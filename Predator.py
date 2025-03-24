from entities import Entity
class Predator(Entity):
    def __init__(self, density, recruitment_rate, max_kill_rate, half_saturation, cond_dep_mortality):
        Entity.__init__(self, density)
        self.recruitment_rate = recruitment_rate
        self.max_kill_rate = max_kill_rate
        self.half_saturation = half_saturation
        self.cond_dep_mortality = cond_dep_mortality

