# APS360 Project
Hi, we are Team 25. Our project is about human age estimation.
### To my lovely team members:
After downloading the 'processed' folder from google drive, do the following:
1. Make sure you have unzipped the 'processed' folder and do not rename it.
2. Download both split_processed.py and generate_alexnet.py to your local project directory.
3. Open the terminal and cd to the project directory.
```shell
cd path/to/project/directory
```
4. First run the split_processed.py program. It will delete all the bad data for you (negatives, 0-5). 
It will also separate the images into training, validation, and test folders.
Note that we will only randomly select 8729 images from each age group, since children has only 8729 images while other age groups 
have much more. We want a balanced dataset. Moreover, this program will move all selected images to a new folder called 'new_processed'. 
Please don't rename this folder for now.
```shell
python split_processed.py
```
5. Now run the generate_alexnet.py program. It will compute and save the newly computed AlexNet features into a new folder called 'alex'.
This will take some time to run.
```shell
python generate_alexnet.py
```
6. You are all set :) Also you can delete or move the 'processed' folder to somewhere else if you want.
