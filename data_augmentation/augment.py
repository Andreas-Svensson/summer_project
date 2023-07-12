from config import * # get settings from config file

import soundfile as sf

import itertools
import math
import os
import random
import sys


# TODO: implement augmentation functions
def placeholder_aug_one(setting, audio_data):
    # TODO: perform some augmentation with setting here
    return audio_data


def placeholder_aug_two(setting, audio_data):
    # TODO: perform some augmentation with setting here
    return audio_data


def create_combinations(combination_limit, settings):
    possible_combinations = math.prod([len(setting) for setting in settings]) # unique combinations possible

    if combination_limit: # if a limit was set in config file
        if possible_combinations > combination_limit: # if all combinations exceeds that limit:
            # create a random subset of unique combinations to use
            combinations = random.sample(list(itertools.product(*settings)), combination_limit)
            return combinations

    # limit does not exist or is not exceeded -> use all possible combinations
    combinations = list(itertools.product(*settings))
    return combinations


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


    # initial setup

    settings = [setting_one, setting_two] # store all config settings in one list
    combinations = create_combinations(combination_limit, settings) # get all combinations to use (random if exceeding combination_limit)

    files_to_create = len(combinations) # amount of files that will be created if the code continues

    exceeds_warning_limit(files_to_create, warning_limit) # display a warning if a large amount of files will be created



    # augment files and save to target directory

    os.makedirs(target_path, exist_ok = True) # create target directory if it does not exist

    # TODO: itertools product loop this to avoid nested loops
    for file_name in os.listdir(source_path):

        if not file_name.endswith(source_filetype): # if wrong extension:
            continue # skip this file
        
        # perform data augmentations on file
        for combination in combinations: # for each combination of augmentation settings

            # read file
            file_path = os.path.join(source_path, file_name)
            audio_data, sample_rate = sf.read(file_path) # read source file to ndarray

            # get new file name from old file name (will be extended to match augmentations made)
            new_file_name = file_name[:-len(source_filetype):] # get name of file without extension (i.e. "file.mp3" -> "file")

            # perform augmentation 1
            audio_data = placeholder_aug_one(combination[0], audio_data)
            new_file_name += f"_{combination[0]}" # update file name

            # perform augmentation 2
            audio_data = placeholder_aug_two(combination[1], audio_data)
            new_file_name += f"_{combination[1]}" # update file name
        
            # save file
            new_file_name += source_filetype # add file extension
            output_path = os.path.join(target_path, new_file_name) # set up path to target / new_file_name
            sf.write(output_path, audio_data, sample_rate) # write file to output path

            print(f"Augmented file saved: {output_path}")
