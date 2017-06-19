import numpy as np
import cv2

def hueMask (pixels, hueRange) :
    hsv = [[hueRange[0],0,0],[hueRange[1],255,255]]
    lower = np.array(hsv[0], dtype = "uint8")
    upper = np.array(hsv[1], dtype = "uint8")
    return cv2.inRange(pixels, lower, upper)
