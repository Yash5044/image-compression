import numpy as np
from PIL import Image
import sys
path1 = sys.argv[1]
path2 = sys.argv[2]

def mse(path1, path2):
    img1 = np.array(Image.open(path1))
    img2 = np.array(Image.open(path2)) 
    # h,w = img1.shape
    print(np.mean((img1 - img2) ** 2)) 

if __name__ == "__main__":
    mse(path1, path2)

