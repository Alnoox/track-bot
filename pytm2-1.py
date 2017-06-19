import numpy as np
from PIL import ImageGrab
import cv2
import time
from pixelshue import hueMask

hsvRange = [[22,150,150],[38,255,255]]

last_time = time.time()
while(True):
    screenBGR = np.array(ImageGrab.grab(bbox=(0,40,800,640)))
    #screenRGB = cv2.cvtColor(screenBGR, cv2.COLOR_BGR2RGB)
    screenHSV = cv2.cvtColor(screenBGR, cv2.COLOR_BGR2HSV)

    mask = hueMask(screenHSV, hsvRange)

    output = cv2.bitwise_and(screenBGR, screenBGR, mask = mask)
    
    print('Loop took {} seconds'.format(time.time()-last_time))
    last_time = time.time()
    
    cv2.imshow('window', output)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
