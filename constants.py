#Change values depending on need

#images will go to this location
OUTPUT_DIRECTORY = 'C:/Users/prath/Desktop/dataAugmentation'

#images are read from this location
INPUT_DIRECTORY = 'C:/Users/prath/Desktop/testImages'

#augmented images will be of this type
RESULT_IMAGE_TYPE = '.jpg'

#number of pictures per augment
NUM_WIDTH_SHIFTS = 5
NUM_HEIGHT_SHIFTS = 5
NUM_ROTATIONS = 5
NUM_BRIGHTNESS = 5
NUM_ZOOMS = 5
NUM_V_FLIPS = 5
NUM_H_FLIPS = 5

#this percentage of the image will shift either right or left randomly
WIDTH_SHIFT_RANGE = 0.6

#this percentage of the image will shift either up or down randomly
HEIGHT_SHIFT_RANGE = 0.6

#the image will be rotated some random number of degrees between 0 and 360
ROTATION_RANGE = 360

#sets the min and max values for the percent brightness change of the image
BRIGHTNESS_MIN = 0.2
BRIGHTNESS_MAX = 1.0

#sets the min and max values for the percent zoom of the image
ZOOM_MIN = 0.5
ZOOM_MAX = 1.0