import numpy as np # importing numpy property
import imageio # importing imageio property
import scipy.ndimage # importing scipy property
import cv2 # importing cv2

image = "mario.jpg"

# Declaring imgscale function to set the scale
def imgscale(rgb):
    return np.dot(rgb[..., :3], [0.298, 0.589, 0.118])

# Declaring the size function to set the front end size
def size(f,b):
	res = f*255/(255-b)
	res[res>255]=255
	res[b==255]=255
	return res.astype('uint8')

x = imageio.imread(image)
y = imgscale(x)
z = 255 - y

var = scipy.ndimage.filters.gaussian_filter(z,sigma=10)
t = size(var,y)

cv2.imwrite('1.png',t)











