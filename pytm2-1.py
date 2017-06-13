import numpy as np
from PIL import ImageGrab
import cv2
import time

#with GBR tuple
## most coherent test boundaries = [([200, 200, 40],[255, 255, 60])]
boundaries = [([86, 31, 4], [220, 88, 50])]

last_time = time.time()
while(True):
    ##color to catch (R:53,G:255,B:255)
    screenBGR = np.array(ImageGrab.grab(bbox=(0,40,800,640)))
    screenRGB = cv2.cvtColor(screenBGR, cv2.COLOR_BGR2RGB)
    ##printscreen_numpy = np.array(printscreen_pil.getdata(),dtype='uint8')

    for (lower, upper) in boundaries :
        lower = np.array(lower, dtype = "uint8")
        upper = np.array(upper, dtype = "uint8")

    mask = cv2.inRange(screenRGB, lower, upper)
    output = cv2.bitwise_and(screenRGB, screenRGB, mask = mask)
    #masked_screen = np.hstack([screen, output])
    
    print('Loop took {} seconds'.format(time.time()-last_time))
    last_time = time.time()
    
    cv2.imshow('window', output)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
