from config import * # get settings from config file

import itertools
import math
import random
import sys

settings = [setting_one, setting_two] # store all config settings in one list

# TODO: implement augmentation functions

def create_combinations(combination_limit, settings):
    possible_combinations = math.prod([len(setting) for setting in settings]) # unique combinations possible

    if combination_limit: # if a limit was set in config file
        if possible_combinations > combination_limit: # if all combinations exceeds that limit:
            # create a random subset of unique combinations to use
            combinations = random.sample(list(itertools.product(*settings)), combination_limit)
            return combinations
        
    # limit does not exist or is not exceeded -> use all possible combinations
    combinations = list(itertools.product(setting_one, setting_two))
    return combinations


# TODO: calculate amount of files created based on amount of settings combinations used
files_created = len(setting_one) * len(setting_two) # amount of files that will be created if ALL combinations are used


def exceeds_warning_limit(files_created, warning_limit):
    if warning_limit: # if a limit was set in config file
        if files_created > warning_limit: # if that limit is exceeded
            proceed = input(f"Running the script will create {files_created} files, do you want to continue? Y/N")
            if proceed.upper() == "Y": # script will continue to run
                print("Creating augmented files...")
            else: # any other input -> script stops running so settings can be changed
                print("Script stopped!")
                sys.exit()


if __name__ == "__main__":
    exceeds_warning_limit(files_created, warning_limit)

    combinations = create_combinations(combination_limit, settings)
    [print(combination) for combination in combinations]
