# base class for predator, herbivore, and prey
class Entity:
    def __init__(self, density, max_recruitment_rate):
        self.density = density
        self.max_recruitment_rate = max_recruitment_rate

