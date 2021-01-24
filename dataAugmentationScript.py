#library imports
from numpy import expand_dims
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot
import cv2 
import os 
import constants
import numpy as np

#set directory
os.chdir(constants.OUTPUT_DIRECTORY) 

#creates NUM_WIDTH_SHIFTS amount of pictures that are edited versions of the given image; applies the width shift edit
#returns a string with the name of the first generated image
def widthShift(imageLocation, imageName):
    img = load_img(imageLocation)
    data = img_to_array(img)
    samples = expand_dims(data, 0) 
    baseName = imageName[:len(imageName)-4] + 'WidthShift'
    for i in range(constants.NUM_WIDTH_SHIFTS):
        datagen = ImageDataGenerator(width_shift_range = constants.WIDTH_SHIFT_RANGE)
        it = datagen.flow(samples, batch_size=1)
        batch = it.next()
        image = batch[0].astype('uint8')
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        uniqueFileName = baseName + str(i) + constants.RESULT_IMAGE_TYPE 
        cv2.imwrite(uniqueFileName, image_rgb)
    return baseName + str(0) + constants.RESULT_IMAGE_TYPE


#creates NUM_HEIGHT_SHIFTS amount of pictures that are edited versions of the given image; applies the height shift edit
#returns a string with the name of the first generated image
def heightShift(imageLocation, imageName):
    img = load_img(imageLocation)
    data = img_to_array(img)
    samples = expand_dims(data, 0) 
    baseName = imageName[:len(imageName)-4] + 'HeightShift'
    for i in range(constants.NUM_HEIGHT_SHIFTS):
        datagen = ImageDataGenerator(height_shift_range = constants.HEIGHT_SHIFT_RANGE)
        it = datagen.flow(samples, batch_size=1)
        batch = it.next()
        image = batch[0].astype('uint8')
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        uniqueFileName = baseName + str(i) + constants.RESULT_IMAGE_TYPE 
        cv2.imwrite(uniqueFileName, image_rgb)
    return baseName + str(0) + constants.RESULT_IMAGE_TYPE


#creates NUM_ROTATIONS amount of pictures that are edited versions of the given image; applies the rotation edit
#returns a string with the name of the first generated image
def rotation(imageLocation, imageName):
    img = load_img(imageLocation)
    data = img_to_array(img)
    samples = expand_dims(data, 0) 
    baseName = imageName[:len(imageName)-4] + 'Rotation'
    for i in range(constants.NUM_ROTATIONS):
        datagen = ImageDataGenerator(rotation_range = constants.ROTATION_RANGE)
        it = datagen.flow(samples, batch_size=1)
        batch = it.next()
        image = batch[0].astype('uint8')
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        uniqueFileName = baseName + str(i) + constants.RESULT_IMAGE_TYPE 
        cv2.imwrite(uniqueFileName, image_rgb)
    return baseName + str(0) + constants.RESULT_IMAGE_TYPE

#creates NUM_BRIGHTNESS amount of pictures that are edited versions of the given image; applies the brightness edit
#returns a string with the name of the first generated image
def brightness(imageLocation, imageName):
    img = load_img(imageLocation)
    data = img_to_array(img)
    samples = expand_dims(data, 0) 
    baseName = imageName[:len(imageName)-4] + 'Brightness'
    for i in range(constants.NUM_BRIGHTNESS):
        datagen = ImageDataGenerator(brightness_range=[constants.BRIGHTNESS_MIN,constants.BRIGHTNESS_MAX])
        it = datagen.flow(samples, batch_size=1)
        batch = it.next()
        image = batch[0].astype('uint8')
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        uniqueFileName = baseName + str(i) + constants.RESULT_IMAGE_TYPE 
        cv2.imwrite(uniqueFileName, image_rgb)
    return baseName + str(0) + constants.RESULT_IMAGE_TYPE

#creates NUM_ZOOMS amount of pictures that are edited versions of the given image; applies the zoom edit
#returns a string with the name of the first generated image
def zoom(imageLocation, imageName):
    img = load_img(imageLocation)
    data = img_to_array(img)
    samples = expand_dims(data, 0) 
    baseName = imageName[:len(imageName)-4] + 'Zoom'
    for i in range(constants.NUM_ZOOMS):
        datagen = ImageDataGenerator(zoom_range=[constants.ZOOM_MIN,constants.ZOOM_MAX])
        it = datagen.flow(samples, batch_size=1)
        batch = it.next()
        image = batch[0].astype('uint8')
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        uniqueFileName = baseName + str(i) + constants.RESULT_IMAGE_TYPE 
        cv2.imwrite(uniqueFileName, image_rgb)
    return baseName + str(0) + constants.RESULT_IMAGE_TYPE

#creates NUM_V_FLIPS amount of pictures that are edited versions of the given image; applies the vertical flip edit
#returns a string with the name of the first generated image
def vFlip(imageLocation, imageName):
    img = load_img(imageLocation)
    data = img_to_array(img)
    samples = expand_dims(data, 0) 
    baseName = imageName[:len(imageName)-4] + 'VFlip'
    for i in range(constants.NUM_V_FLIPS):
        datagen = ImageDataGenerator(vertical_flip=True)
        it = datagen.flow(samples, batch_size=1)
        batch = it.next()
        image = batch[0].astype('uint8')
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        uniqueFileName = baseName + str(i) + constants.RESULT_IMAGE_TYPE 
        cv2.imwrite(uniqueFileName, image_rgb)
    return baseName + str(0) + constants.RESULT_IMAGE_TYPE

#creates NUM_H_FLIPS amount of pictures that are edited versions of the given image; applies the horizontal flip edit
#returns a string with the name of the first generated image
def hFlip(imageLocation, imageName):
    img = load_img(imageLocation)
    data = img_to_array(img)
    samples = expand_dims(data, 0) 
    baseName = imageName[:len(imageName)-4] + 'HFlip'
    for i in range(constants.NUM_H_FLIPS):
        datagen = ImageDataGenerator(horizontal_flip=True)
        it = datagen.flow(samples, batch_size=1)
        batch = it.next()
        image = batch[0].astype('uint8')
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        uniqueFileName = baseName + str(i) + constants.RESULT_IMAGE_TYPE 
        cv2.imwrite(uniqueFileName, image_rgb)
    return baseName + str(0) + constants.RESULT_IMAGE_TYPE

#receives user input regarding which augmentations need to be done and in which order/combination they need to be applied
userInput = input('Please enter the order of augmentations. \nOptions include: \nW for width \nH for height \nR for rotation \nB for brightness \nZ for zoom.\n'
'V for vertical flips\nF for horizontal flips\n')

#for loop gets names of all files in the folder INPUT_DIRECTORY
for imageName in os.listdir(constants.INPUT_DIRECTORY):  

    #loads image from the image's location and file name
    imageLocation = constants.INPUT_DIRECTORY + '/' + imageName
    img = load_img(imageLocation)

    #parses through userInput, applies edits, and changes the imageName and imageLocation variables as needed
    for currentLetter in userInput:
        if currentLetter == 'w' or currentLetter == 'W':
            imageName = widthShift(imageLocation,imageName)
            imageLocation = constants.OUTPUT_DIRECTORY + '/' + imageName
        elif currentLetter == 'h' or currentLetter == 'H':
            imageName = heightShift(imageLocation,imageName)
            imageLocation = constants.OUTPUT_DIRECTORY + '/' + imageName
        elif currentLetter == 'r' or currentLetter == 'R':
            imageName = rotation(imageLocation,imageName)
            imageLocation = constants.OUTPUT_DIRECTORY + '/' + imageName
        elif currentLetter == 'b' or currentLetter == 'B':
            imageName = brightness(imageLocation,imageName)
            imageLocation = constants.OUTPUT_DIRECTORY + '/' + imageName
        elif currentLetter == 'z' or currentLetter == 'Z':
            imageName = zoom(imageLocation,imageName)
            imageLocation = constants.OUTPUT_DIRECTORY + '/' + imageName
        elif currentLetter == 'f' or currentLetter == 'F':
            imageName = hFlip(imageLocation,imageName)
            imageLocation = constants.OUTPUT_DIRECTORY + '/' + imageName
        elif currentLetter == 'v' or currentLetter == 'V':
            imageName = vFlip(imageLocation,imageName)
            imageLocation = constants.OUTPUT_DIRECTORY + '/' + imageName
        else:
            print('get gud')

        
    

