from picamera import PiCamera
from time import sleep
import cv2
import numpy as np
from fastiecm import fastiecm

camera = PiCamera()

import cv2
import numpy as np
from fastiecm import fastiecm
from picamera import PiCamera
import picamera.array

camera = PiCamera()
camera.rotation = 180
camera.resolution = (1920, 1080)



camera.start_preview()

def calc_ndvi(image):
    b, g, r = cv2.split(image)
    bottom = (r.astype(float) + b.astype(float))
    bottom[bottom==0] = 0.01
    ndvi = (r.astype(float) - b) / bottom # THIS IS THE CHANGED LINE
    return ndvi

def contrast(im):
    in_min = np.percentile(im, 5)
    in_max = np.percentile(im, 95)

    out_min = 0.0
    out_max = 255.0

    out = im - in_min
    out *= ((out_min - out_max) / (in_min - in_max))
    out += in_min
    return out

for i in range(0, 17280):
        
    stream = picamera.array.PiRGBArray(camera)
    camera.capture(stream, format='bgr', use_video_port=True)
    original = stream.array
    
    cv2.imwrite('original.png', original)
    
    
#     image = cv2.imread('/home/pi/Desktop/normalImage%s.png' % i)
#     im = np.array(image, dtype=float)/float(255)
    
#     out = contrast(im)

#     cv2.imwrite('ContrastedImage%s.png' % i, out)

#     out = contrast(calc_ndvi(out))

#     cv2.imwrite('NDVI_Image%s.png' % i, out)

#     color_mapped_prep = out.astype(np.uint8)
#     color_mapped_image = cv2.applyColorMap(color_mapped_prep, fastiecm)

#     cv2.imwrite('ColourMapped%s.png' % i, color_mapped_image)


camera.stop_preview()
