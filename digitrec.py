import keras as kr
import numpy as np
import gzip
import matplotlib.pyplot as plt
import sklearn.preprocessing as pre
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PIL import Image


def generateModel(inputs,outputs):
    # Start a neural network, building it by layers.
    model3 = kr.models.Sequential()

    # Add a hidden layer with 600 neuros and  with input 784 with activation RELU
    model3.add(kr.layers.Dense(units=600, activation='relu', input_dim=784, kernel_initializer='normal'))
    # Add second hidden layer with 600 neuros and  with input 784 with activation RELU
    model3.add(kr.layers.Dense(units = 400, activation='relu', kernel_initializer='normal'))
    # Add the output layer
    model3.add(kr.layers.Dense(10, kernel_initializer='normal', activation='softmax'))

    # Build the graph.
    model3.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    # Fit the model
    model3.fit(inputs, outputs, epochs=10, batch_size=100)
    return (model3)

def generateInputsAndOutputs():
    # Open the training images
    with gzip.open('data/train-images-idx3-ubyte.gz', 'rb') as f:
        train_img = f.read()

    # Open the training labels
    with gzip.open('data/train-labels-idx1-ubyte.gz', 'rb') as f:
        train_lbl = f.read()

    # Reshape the training images to an array of 60000, of which the picture is 28 by 28 pixels.
    # The pixels are divided by 255 so that the algorithm will be more accurate when taking in numbers from range 
    #  0-1 instead of 0-255
    # The pixels are also flipped around with the ~ symbol so that the foreground will be black and the 
    #  background will be white
    train_img = ~np.array(list(train_img[16:])).reshape(60000, 28, 28).astype(np.uint8) / 255.0

    # The training labels are put into a list, starting from position 8 in the array, ignorning the metadata
    train_lbl =  np.array(list(train_lbl[ 8:])).astype(np.uint8)

    # reshape into one linear input of pixels
    inputs = train_img.reshape(60000, 784)

    encoder = pre.LabelBinarizer()
    encoder.fit(train_lbl)
    outputs = encoder.transform(train_lbl)

    return (inputs,outputs,encoder)

def getFile():
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    return filename

def predictDigit(model,encoder):
    play = True
    while play:
        #get the file from file explorer
        filename = getFile()
        img = ~np.invert(Image.open(filename)).reshape(1,784).astype(np.uint8) / 255.0
        #print results
        print("The model predicts that the digit is: " , encoder.inverse_transform(model.predict(img)))
        print("The actual digit is:",filename[-5:-4] )

        # play again?
        answer = input("Do you want to predict another digit? (yes or no): ")
        while True:
            if answer == 'yes':
                play = True
                break
            elif answer == 'no':
                play = False
                break
            else:
                answer = input('Incorrect option. Type "yes" to try again or "no" to leave": ').lower()
        

def main():
    inputs,outputs,encoder = generateInputsAndOutputs()
    model = generateModel(inputs,outputs)
    predictDigit(model,encoder)

main()
    
    






