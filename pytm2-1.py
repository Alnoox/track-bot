import numpy as np
from PIL import ImageGrab
import cv2
import time
from pixelshue import hueMask
from roi import roi

def processImg(originalImage) :
    processedImg = cv2.cvtColor(originalImage, cv2.COLOR_BGR2HSV)
    mask = hueMask(processedImg, hsvRange)
    processedImg = cv2.bitwise_and(processedImg, processedImg, mask = mask)
    processedImg = cv2.Canny(processedImg, threshold1=200, threshold2=300)
    vertices = np.array([[0,225],[0,600],[800,600],[800,225],], np.int32)
    processedImg = roi(processedImg,[vertices])
    return processedImg

hsvRange = [[22,150,150],[38,255,255]]

last_time = time.time()
while(True):
    #Capture screen
    screenBGR = np.array(ImageGrab.grab(bbox=(0,40,800,640)))
    #screenRGB = cv2.cvtColor(screenBGR, cv2.COLOR_BGR2RGB)
    output = processImg(screenBGR)
    
    print('Loop took {} seconds'.format(time.time()-last_time))
    last_time = time.time()
    
    cv2.imshow('window', output)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

