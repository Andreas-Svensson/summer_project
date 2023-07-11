# config file for data augmentation script
# change any values here to alter how augmented data is generated



########################
# WARNING NOTIFICATION #
########################

# should the script show a warning notifying the user of how many files will be created before running?
# set to an integer value to show warning when amount of files created exceeds the value
# setting no None will never display a warning, setting to 0 will always display a warning

# should the script show a warning before running?
# valid settings: None, value
warning_limit = 100 # will show a warning if creating more than 100 files



########################
# COMBINATION SETTINGS #
########################

# should the file create augmentations with random combinations of settings instead of every single one?
# using random combinations will create less files and take up less file size, while allowing for a broader range of variations over all

# should the script use random combinations?
# valid settings: True, False
use_random_combinations = False

# which random combination to use?
# valid settings: None added yet
random_type = None



######################
# VARIATION SETTINGS #
######################

# values for setting_one
setting_one = [1, 2, 3, 4, 5]

# values for setting_two
setting_two = [1, 2, 3, 4, 5]

