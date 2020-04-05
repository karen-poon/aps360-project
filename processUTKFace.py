import cv2
import os
import matplotlib.pyplot as plt
import random

def create_chart(orig_path):
    chart = [0 for x in range(11)]
    file_list = os.listdir(orig_path)
    
    for f in file_list:
        split_f = f.split('_')
        index = int(split_f[0],10)
        if index >= 0 and index <= 2:
            index = 0 # use 0 to represent 0-2
        elif index >= 3 and index <= 12:
            index = 1 # use 1 to represent 3-12
        elif index >= 13 and index <= 19:
            index = 2 # use 2 to represent 13-19
        elif index >= 20 and index <= 29:
            index = 3 # use 3 to represent 20-29
        elif index >= 30 and index <= 39:
            index = 4 # use 4 to represent 30-39
        if index >= 40 and index <= 49:
            index = 5 # use 5 to represent 40-49
        elif index >= 50 and index <= 59:
            index = 6 # use 6 to represent 50-59
        elif index >= 60 and index <= 69:
            index = 7
        elif index >= 70 and index <= 79:
            index = 8
        elif index >= 80 and index <= 89:
            index = 9
        elif index >= 90:
            index = 10
        
        chart[index] += 1

    # # display number of image we have for each age
    # for i in range(len(chart)):
    #     print(i, ":", chart[i])
    return chart

def save_as_gray(file_name, index_string, data_type):
    orig_path = os.getcwd() + "/UTKFace/" + file_name
    image = cv2.imread(orig_path)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized_image = cv2.resize(image_gray, (128, 128))

    new_path = os.getcwd() + "/new_UTKFace/" + data_type + "/" + index_string

    if not os.path.exists(new_path):
        os.makedirs(new_path)

    new_file_name = new_path + "/" + file_name
    cv2.imwrite(new_file_name, image_gray)

def split_data(image_list):
    random.shuffle(image_list) # ***it will randomly shuffle the list***
    new_path = os.getcwd() + "/new_UTKFace"
    chart = create_chart(orig_path) # total number of images for each age
    counter = [0 for x in range(11)] # count how many images we have processed for each age

    for f in image_list:
        split_f = f.split('_') # ['1', '0', '0', 'y.jpg']
        index = int(split_f[0],10) # convert to int with base 10

        split_f = f.split('_')
        index = int(split_f[0],10)
        if index >= 0 and index <= 2:
            index = 0 # use 0 to represent 0-2
            index_string = "0-2"
        elif index >= 3 and index <= 12:
            index = 1 # use 1 to represent 3-12
            index_string = "3-12"
        elif index >= 13 and index <= 19:
            index = 2 # use 2 to represent 13-19
            index_string = "13-19"
        elif index >= 20 and index <= 29:
            index = 3 # use 3 to represent 20-29
            index_string = "20-29"
        elif index >= 30 and index <= 39:
            index = 4 # use 4 to represent 30-39
            index_string = "30-39"
        if index >= 40 and index <= 49:
            index = 5 # use 5 to represent 40-49
            index_string = "40-49"
        elif index >= 50 and index <= 59:
            index = 6 # use 6 to represent 50-59
            index_string = "50-59"
        elif index >= 60 and index <= 69:
            index = 7
            index_string = "60-69"
        elif index >= 70 and index <= 79:
            index = 8
            index_string = "70-79"
        elif index >= 80 and index <= 89:
            index = 9
            index_string = "80-89"
        elif index >= 90:
            index = 10
            index_string = "90+"

        if counter[index] > (chart[index]*0.7) and counter[index] <= (chart[index]*0.85):
            save_as_gray(f, index_string, "validation")
        elif counter[index] > (chart[index]*0.85):
            save_as_gray(f, index_string, "test")
        else:
            save_as_gray(f, index_string, "train")

        counter[index] += 1



if __name__ == '__main__':
    
    orig_path = os.getcwd() + "/UTKFace"
    if not os.path.exists(orig_path):
        print("Cannot find the UTKFace folder. Please make sure it is in the current directory.")
        exit()
    
    new_path = os.getcwd() + "/new_UTKFace"
    print("Creating a new folder called new_UTKFace...")
    if os.path.exists(new_path):
        print("Please delete the new_UTKFace folder before proceeding.")
        exit()
    
    print("Creating directories...")
    os.makedirs(new_path)
    os.makedirs(new_path+"/train")
    os.makedirs(new_path+"/validation")
    os.makedirs(new_path+"/test")

    print("Separating files now...")
    image_list = os.listdir(orig_path)
    split_data(image_list)

    print("All done :) Please check the new_UTKFace folder.")

