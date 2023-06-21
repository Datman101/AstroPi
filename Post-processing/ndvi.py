import cv2
from fastiecm import fastiecm
import numpy as np

def return_ndvi(image, i):
    image = image.astype(np.uint8)
    image = cv2.applyColorMap(image, fastiecm)
    b, g, r = cv2.split(image)
    bottom = (r.astype(float) + b.astype(float))
    bottom[bottom==0] = 0.01
    ndvi = (r.astype(float) - b) / bottom
    return image

def calc_ndvi(image, i):
    image = image.astype(np.uint8)
    image = cv2.applyColorMap(image, fastiecm)
    b, g, r = cv2.split(image)
    bottom = (r.astype(float) + b.astype(float))
    bottom[bottom==0] = 0.01
    ndvi = (r.astype(float) - b) / bottom
    #return image
    ndvi = np.sum(ndvi[0:-1, 0:-1])
    print(ndvi)
    return ndvi/1944


calculatingNDVI = False

if(calculatingNDVI):
  print("Processing images...")
  for i in range(0, 991):
   print(f"C:/Users/datis/Downloads/Asteria/Asteria/asteria_image_{i:03d}.jpg")
   original = cv2.imread(f"C:/Users/datis/Downloads/Asteria/Asteria/asteria_image_{i:03d}.jpg")
   cv2.imwrite('NDVI-ed_image_' + str(i) + '.png', calc_ndvi(original, i))

else:
  print("NDVI values being calculated")
  f = open("ndvi_values.txt", 'w')
  for i in range(0, 991):
    original = cv2.imread(f"C:/Users/datis/Downloads/Asteria/Asteria/asteria_image_{i:03d}.jpg")
    f.write(str(calc_ndvi(original, i)) + "\n")
  
  
