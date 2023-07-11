import sys
from config import * # get settings from config file

# TODO: implement augmentation functions

# TODO: implement combinatorics function to go over all combinations of augmentations or a random selection

# TODO: calculate amount of files created based on amount of settings combinations used
files_created = 101 # placeholder value larger than default setting for now

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