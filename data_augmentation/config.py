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

# amount of files to create, if 0 or a value larger than all possible combinations is used, then all combinations of settings will be created
# else files with a random subset of combinations will be created, allowing for a wide range of settings without creating a huge amount of files

# how many variations to create?
# valid settings: value (0 = all combinations)
combinations = warning_limit # setting to warning limit will create exactly as many files as specified above



######################
# VARIATION SETTINGS #
######################

# values for setting_one
setting_one = [1, 2, 3, 4, 5]

# values for setting_two
setting_two = [1, 2, 3, 4, 5]

