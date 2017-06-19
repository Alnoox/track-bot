import numpy as np
from PIL import ImageGrab
import cv2
import time
from pixelshue import hueMask 

last_time = time.time()
while(True):
    ##color to catch (R:53,G:255,B:255)
    screenBGR = np.array(ImageGrab.grab(bbox=(0,40,800,640)))
    screenRGB = cv2.cvtColor(screenBGR, cv2.COLOR_BGR2RGB)
    screenHSV = cv2.cvtColor(screenBGR, cv2.COLOR_BGR2HSV)
    ##printscreen_numpy = np.array(printscreen_pil.getdata(),dtype='uint8')

    mask = hueMask(screenHSV, [20,40])

    output = cv2.bitwise_and(screenRGB, screenRGB, mask = mask)
    #masked_screen = np.hstack([screen, output])
    
    print('Loop took {} seconds'.format(time.time()-last_time))
    last_time = time.time()
    
    cv2.imshow('window', output)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
