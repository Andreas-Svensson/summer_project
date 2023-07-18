from config import * # get settings from config file

import soundfile as sf
import numpy as np

import itertools
import math
import os
import random
import sys


# TODO: implement more augmentation functions
def reverb(audio_data, layers, scaling, delay):
    echo = np.array(audio_data) # create copy of original sound to be altered and overlayed as echo

    for _ in range(layers): # iterate to add n layers of echo to original sound
        # shift sound to the right (by prepending zeroes and removing same amount of indices from the end)
        # then scale volume down by multiplying with scaling value
        echo = np.concatenate((np.zeros(delay), echo))[:-delay] * scaling
        audio_data += echo # add reverb echo over original sound
    
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

    settings = [
        setting_reverb_layers,
        setting_reverb_scaling,
        setting_reverb_delay,
    ] # store all config settings in one list

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
            audio_data = reverb(audio_data, combination[0], combination[1], combination[2])
            new_file_name += f"_{combination[0]}_{combination[1]}_{combination[2]}" # update file name
        
            # save file
            new_file_name += source_filetype # add file extension
            output_path = os.path.join(target_path, new_file_name) # set up path to target / new_file_name
            sf.write(output_path, audio_data, sample_rate) # write file to output path

            print(f"Augmented file saved: {output_path}")
