import sys
sys.path.insert(1, '../')
import loader
import errors
import truncate as trun
import colormap as cmap
from PIL import ImageOps, Image
import numpy as np

file_name = sys.argv[2] # eg : lena, baboon
threshold = float(sys.argv[1])  # a value between 0 and 1  
path = "../images/" + file_name +  ".png"


def main():
    img = np.array(ImageOps.grayscale(Image.open(path)))
    ft = np.fft.fft2(img)
    # ang = np.angle(ft)
    abst = np.absolute(ft)
    maxv = max(np.max(abst),-np.min(abst))
    val1 = abst < maxv*threshold
    val2 = abst > -maxv*threshold
    ft[val1 & val2] = 0
    img = np.fft.ifft2(ft).astype(int)
    loader.show_image(img)
if __name__ == "__main__" :
    main()