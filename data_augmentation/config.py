# config file for data augmentation script
# change any values here to alter how augmented data is generated



####################
# SOURCE DIRECTORY #
####################

# path to read existing data from (starts from project root directory)
source_path = "data" # project root -> data folder

# filetype of files to read
source_filetype = ".mp3" # will read all files of this type in source directory



####################
# TARGET DIRECTORY #
####################

# path to output augmented data to (starts from project root directory)
target_path = "data_augmentation\data" # project root -> data_agumentation folder -> data folder



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

# amount of files to create, if None or a value larger than all possible combinations is used, then all combinations of settings will be created
# else files with a random subset of combinations will be created, allowing for a wide range of settings without creating a huge amount of files

# how many variations to create?
# valid settings: value (None = all combinations)
combination_limit = warning_limit # setting to warning limit will create exactly as many files as specified above



###################
# REVERB SETTINGS #
###################

# reverb function adds echo to the original audio

# amount of layers in reverb (setting to 5 will add 5 delayed echos of the original sound at reduced volume)
setting_reverb_layers = [25] # [1, 3, 5]

# amount volume is scaled down for each reverb layer (setting to 0.2 will set volume to 20% of last layer)
setting_reverb_scaling = [0.6] # [0.1, 0.2]

# delay between each reverb layer (setting to 1 at 44100 hz will set delay to 1/44100th of a second)
setting_reverb_delay = [5000] # [100, 500, 1000]
