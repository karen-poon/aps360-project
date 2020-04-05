# APS360 Project
Hi, we are Team 25. Our project is about human age estimation.
### To my lovely team members:
To process our new dataset, do the following:
1. Download the new dataset at https://drive.google.com/drive/folders/0BxYys69jI14kU0I1YUQyY1ZDRUE. *Only download the UTKFace.tar.gz folder*. Unzip the folder with 7-zip if you are using Windows like me.
2. Download processUTKFace.py to your local project directory.
3. Open the terminal and cd to the project directory.
```shell
cd path/to/project/directory
```
4. Run the processUTKFace.py program. It will change the image to grayscale and resize them to 128x128. It will also split them into training, validation, and test folders. It won't take long :)
```shell
python split_processed.py
```
5. You are all set :)
