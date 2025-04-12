from Plants import Plants
from Predator import Predator
from Prey import Prey
from math import pow
import GlobalVariables

browse = Plants(10000, 1.1, 2*pow(10, 5), 700, 1, .7)
hare = Prey(500, 1.2, 1.8, .98, 2 * pow(10, 4))
predators = Predator(.05, 1.2, 600, 90, .9)

browse_array = []
hare_array = []
predator_array = []

def cause_disruption_hare(time_start, time_trapped, dt_btwn_trials, percentage_trapped, trials, mortality_rate, time_interval, num_ran):
    update(time_interval)

    ts = time_start
    # tracks the time until a release
    time_release = 9999999
    amt_trapped = 0
    # number that the hare array is on
    num_on = 0

    for x in range(1, num_ran):
        # trapping hares
        if GlobalVariables.time >= ts:
            time_release = time_trapped
            amt_trapped = hare.density * percentage_trapped
            hare.density -= amt_trapped
            ts = 999999

        #print(f"t {GlobalVariables.time} - ts {ts}")

        # letting Hares free
        if time_release <= 0:
            amt_trapped -= amt_trapped*mortality_rate
            print(hare.density, amt_trapped)
            hare.density += amt_trapped
            # set to one bc it doesn't check when the if starts
            if trials > 1:
                # setting the next start time to be the next time we sample
                print(trials)
                ts = GlobalVariables.time + dt_btwn_trials
                time_release = 99999
                trials -= 1
            else:
                time_release = 999999

        if time_release > 0:
            time_release -= time_interval

        num_on += 1
        update(time_interval)

def update(time_interval):
    GlobalVariables.time += time_interval
    plant_der = browse.plant_derivative(hare) * time_interval
    hare_der = hare.prey_derivative(browse, predators) * time_interval
    pred_der = predators.find_predator_derivative(hare) * time_interval
    browse.density += plant_der
    hare.density += hare_der
    predators.density += pred_der

    try:

        browse_array.append(browse.density)
        hare_array.append(hare.density)
        predator_array.append(predators.density)

        #browse_array.append(plant_der)
        #hare_array.append(hare_der)
        #predator_array.append(pred_der)
        #hare_array[b] = hare.prey_derivative(browse, predators)
        #predator_array[b] = predators.find_predator_derivative(hare)

    except:
        pass

def get_browse():
    return browse_array

def get_hare():
    return hare_array

def get_pred():
    return predator_array

def empty_array():
    global browse_array, hare_array, predator_array
    browse_array = []
    hare_array = []
    predator_array = []
