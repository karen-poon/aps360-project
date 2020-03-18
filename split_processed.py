'''
Divide the data into training, validation, and test folders.
note: We will only be randomly selecting 8729 images from each age group since we wanted a balanced dataset.
@karen-poon
'''
import shutil
import os
import random

print("Helu~ starting split_processed.py program now -- by Karen")

########## check if the original processed folder is in your directory ##########
orig_path = os.getcwd() + "/processed"
if not os.path.exists(orig_path):
    print("Cannot find the processed folder. Cancelling split processed.")
    exit()

########## delete bad children data ###########
print("Deleting the bad data...")

path = os.getcwd() + "/processed/Children0-14"
children_to_delete_list = os.listdir(path)

for f in children_to_delete_list:
    if (f[0] >= '0' and f[0] <= '5' and f[1] == 'a') or f[0] == '-':
        os.remove(path + "/"+f)
        # print("Deleted:", f)

print("deletion done.")

########## create new folders data ###########
new_path = os.getcwd() + "/new_processed"
print("Creating a new folder called new_processed...")
if os.path.exists(new_path):
    print("Please delete the new_processed folder before proceeding.")
    exit()

os.makedirs(new_path)
os.makedirs(new_path + "/train/Children0-14")
os.makedirs(new_path + "/validation/Children0-14")
os.makedirs(new_path + "/test/Children0-14")
os.makedirs(new_path + "/train/Youth15-24")
os.makedirs(new_path + "/validation/Youth15-24")
os.makedirs(new_path + "/test/Youth15-24")
os.makedirs(new_path + "/train/Adults25-64")
os.makedirs(new_path + "/validation/Adults25-64")
os.makedirs(new_path + "/test/Adults25-64")
os.makedirs(new_path + "/train/Seniors65+")
os.makedirs(new_path + "/validation/Seniors65+")
os.makedirs(new_path + "/test/Seniors65+")

print("created new_processed folder.")

# function that splits and moves all the images to the correct folder
def split_data(group, group_list, orig_path, new_path):
    group_name = ""
    if group == "children":
        group_name = "/Children0-14"
    elif group == "youth":
        group_name = "/Youth15-24"
    elif group == "adult":
        group_name = "/Adults25-64"
    elif group == "senior":
        group_name = "/Seniors65+"
    else:
        print("Something's wrong with my split_data function... Tell me if you see this")
        exit()
        
    train_split = 6110 # 8729 * 0.7
    val_split = 7419 # 8729 * 0.85
    
    # train: 1 - 6110
    # val: 6111 - 7419
    # test: 7420 - 8729
    # train: 1 - train_split, val: train_split+1 - val_split, test: val_split+1 - len(list)

    n = 1 # iterator for f
    random.shuffle(group_list) # ***it will randomly shuffle the list***
    for f in group_list:
        if n >= 1 and n <= train_split:
            shutil.move(orig_path + group_name + "/" + f, new_path + "/train/" + group_name)
            # print("Moved:", f)
        elif n >= train_split+1 and n <= val_split:
            shutil.move(orig_path + group_name + "/" + f, new_path + "/validation/" + group_name)
            # print("Moved:", f)
        else:
            shutil.move(orig_path + group_name + "/" + f, new_path + "/test/" + group_name)
            # print("Moved:", f)

        if n == 8729:
            break

        n += 1

########## split children data ###########
print("Splitting children data right now...")
children_list = os.listdir(orig_path + "/Children0-14")
split_data("children", children_list, orig_path, new_path)
print("children done.")

########### split youth data ###########
print("Splitting youth data right now...")
youth_list = os.listdir(orig_path + "/Youth15-24")
split_data("youth", youth_list, orig_path, new_path)
print("youth done.")

########### split adult data ###########
print("Splitting adult data right now...")
adult_list = os.listdir(orig_path + "/Adults25-64")
split_data("adult", adult_list, orig_path, new_path)
print("adult done.")

########### split senior data ###########
print("Splitting senior data right now...")
senior_list = os.listdir(orig_path + "/Seniors65+")
split_data("senior", senior_list, orig_path, new_path)
print("senior done.")

print("All done :)")
print("Now use the 'new_processed' folder. We won't be using the 'processed' folder anymore.")
