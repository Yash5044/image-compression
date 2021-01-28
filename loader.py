import numpy as np
import os
import matplotlib.pyplot as plt
import pywt
from PIL import Image

# enter relative path from the file of execution
# returns 3D numpy array of the image 
def load_image(path) :
    try:
        img = np.array(Image.open(path))  
    except IOError:
        print(IOError)
        img = 0
    return img

# enter the channels [R, G, B] to get respective channel images    
def show_image(img, channel = 0):
    if channel == 'R':
        img[:,:,1] *= 0
        img[:,:,2] *= 0
    elif channel == 'G':
        img[:,:,0] *= 0
        img[:,:,2] *= 0
    elif channel == 'B':
        img[:,:,1] *= 0
        img[:,:,0] *= 0
    img = Image.fromarray(img)
    img.show()

    
    
