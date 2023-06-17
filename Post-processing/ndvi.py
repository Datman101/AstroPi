import cv2
from fastiecm import fastiecm
import numpy as np

def calc_ndvi(image, i):
    image = image.astype(np.uint8)
    image = cv2.applyColorMap(image, fastiecm)
    b, g, r = cv2.split(image)
    bottom = (r.astype(float) + b.astype(float))
    bottom[bottom==0] = 0.01
    ndvi = (r.astype(float) - b) / bottom
    return image


for i in range(0, 991):
  print(f"C:/Users/datis/Downloads/Asteria/Asteria/asteria_image_{i:03d}.jpg")
  original = cv2.imread(f"C:/Users/datis/Downloads/Asteria/Asteria/asteria_image_{i:03d}.jpg")
  cv2.imwrite('NDVI-ed_image_' + str(i) + '.png', calc_ndvi(original, i))
  
  