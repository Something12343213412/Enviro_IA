class Predator:

    def __init__(self, density, kill_rate, max_predator_recruitment, max_kill_rate, predator_half_sat):
        # changes with time, figure out more later
        self.density = density
        # changes with time, figure out more later
        self.kill_rate = kill_rate
        # 1.2, yr^-1, measures how much new population added
        self.max_predator_recruitment = max_predator_recruitment
        # 600, hares/(predators * year), measures the max of how many hares a predator can kill in a year
        self.max_kill_rate = max_kill_rate
        # 90, hares/km^2, measures 1/2 of what the predators can eat
        self.predator_half_sat = predator_half_sat
        #
        pass
