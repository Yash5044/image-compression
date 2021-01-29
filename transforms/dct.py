import sys
sys.path.insert(1, '../')
import loader
import pywt
import truncate as trun
import colormap as cmap
import numpy as np
from scipy.fftpack import dct, idct

path = "../images/cat.png"

# implement 2D DCT
def dct2(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')

# implement 2D IDCT
def idct2(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')   


def DCT(img2d):
    img = dct2(img2d) # dct
    truncated_img = trun.truncate(img, 0)  # approximate part
    imgr2d = idct2(truncated_img) # idct to reconstruct the numpy array
    h,w = imgr2d.shape
    return imgr2d[:h,:] 

def main():
    img = loader.load_image(path)
    # loader.show_image(img)
    for i in range(3):   # i=0->R ; i=1->G ; i=2->B
        img[:,:,i] = DCT(img[:,:,i])
    loader.show_image(img)


if __name__ == "__main__":
    main()