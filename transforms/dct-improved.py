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

def local_dct(I, w = 8) :  # w = patch size
    lI = np.zeros(I.shape)
    # Loop over the small (w,w) patches ------------------------------
    for i in range(1,I.shape[0]//w+1):
        for j in range(1,I.shape[1]//w+1):
            lI[(i-1)*w: i*w, (j-1)*w: j*w] = dct2(I[(i-1)*w: i*w, (j-1)*w: j*w])
    return lI


def ilocal_dct(lI, w = 8) :  # w = patch size
    I = np.zeros(lI.shape)
    # Loop over the small (w,w) patches ------------------------------
    for i in range(1,I.shape[0]//w+1):
        for j in range(1,I.shape[1]//w+1):
            I[(i-1)*w: i*w, (j-1)*w: j*w] = idct2(lI[(i-1)*w: i*w, (j-1)*w: j*w])
    return I

def lDCT_threshold(lI, threshold) :
    lI_thresh = lI.copy()                  # Create a copy of the local DCT transform
    lI_thresh[ abs(lI) < threshold ] = 0   # Remove all the small coefficients
    I_thresh = ilocal_dct(lI_thresh)       # Invert the new transform...

    return I_thresh

def DCT(img2d):
    # img = dct2(img2d) # dct
    lI = local_dct(img2d, w = 8)
    lDCT_threshold(lI, .5) 
    # truncated_img = trun.truncate(lI, 0)  # approximate part
    Abs_values = np.sort( abs(lI.ravel()) )
    cutoff = Abs_values[-20000] 
    imgr2d = lDCT_threshold(lI, cutoff) 
    # imgr2d = idct2(truncated_img) # idct to reconstruct the numpy array
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