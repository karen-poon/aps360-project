# APS360 Project - Human Age Estimation
Hi, we are Team 25. Our project is about human age estimation.

We utilized the UTKFace dataset (https://susanqq.github.io/UTKFace/) to train our model.

<p align="center">
  <img width="600" src="https://github.com/karen-poon/aps360-project/blob/master/illustration/aps360_project_illustrations.png">
</p>

### SVM.ipynb
This file contains training and testing of our SVM baseline model.

### NewAgeClassification.ipynb
This file contains all the training, testing, and sample output of our classification model.
(Basically all our main code is in this file)

### AgeRegression.ipynb
This file contains training, testing, and sample output of our regression model.

### processUTKFace.py
This file resizes the image to 128x128, turns them to grayscale and splits them into training, validation, and testing folders.

## Sample Processed Data
<p align="center">
  <img width="500" src="https://github.com/karen-poon/aps360-project/blob/master/illustration/sample_processed_data.png">
</p>


## Architecture
<p align="center">
  <img width="700" src="https://github.com/karen-poon/aps360-project/blob/master/illustration/architecture.png">
</p>

## Sample Output
<p align="center">
  <img width="700" src="https://github.com/karen-poon/aps360-project/blob/master/illustration/sample_output.png">
</p>

## To my lovely team members:
To process our new dataset, do the following:
1. Download the new dataset at https://drive.google.com/drive/folders/0BxYys69jI14kU0I1YUQyY1ZDRUE. *Only download the UTKFace.tar.gz folder*. Unzip the folder with 7-zip if you are using Windows like me.
2. Download processUTKFace.py to your local project directory.
3. Open the terminal and cd to the project directory.
```shell
cd path/to/project/directory
```
4. Run the processUTKFace.py program. It will change the image to grayscale and resize them to 128x128. It will also split them into training, validation, and test folders. It won't take long :)
```shell
python processUTKFace.py
```
5. You are all set :)

### Authors
Karen Poon, Stacy Zheng, Sophie Zhang, Jarvis Dai
