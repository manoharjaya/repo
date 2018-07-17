Automate extraction of study notes from IPhone Photos

I've trained a CNN model to predict such Quora Screen Shots files and extract them out of photos directory :)



Requirements:

    Numpy
    Keras

Instructions:

Connect your Smartphone to your system, mount Internal Storage and copy the absolute path to the Photos folder, to know the absolute path open a terminal in Photos folder and run pwd command. Run the extract.py script by python extract.py and paste the copied path when asked to. The script will create a new folder named Screen shots in your Image folder and move the study notes images to it.

I've trained the model on about 1200 images and using Keras' data augmentation pipeline. Currently the model is 94% accurate on my dataset. 

Enjoy!
