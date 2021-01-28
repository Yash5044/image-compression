from PIL import Image
img = Image.open('compressed_image.bmp')
img.save( 'finalimage.jpeg', 'jpeg')