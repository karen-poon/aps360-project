# Old Model's Code

Our group originally uses the IMDB-WIKI dataset (https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/) to train our model.
We have created different models and have done trainings with it. However, later we realized that this dataset contains too 
many mislabelled images. Our group has made a decision to abandon this dataset and the models that we have trained.

### AgeClassificationCNN.ipynb
Basically all our training code is here.

### dataProcess.py
This file crops and resizes the images, as well as turning them into grayscale.

### split_process.py
This file splits the data into training, validation, and test folders.

### generate_alexnet.py
This file creates AlexNet features. We originally wanted to try transfer learning with AlexNet, but the accuracy was too low.
