import numpy as np
import cv2

def hueMask (pixels, hsvRange) :
    lower = np.array(hsvRange[0], dtype = "uint8")
    upper = np.array(hsvRange[1], dtype = "uint8")
    return cv2.inRange(pixels, lower, upper)
