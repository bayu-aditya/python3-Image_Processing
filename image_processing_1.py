#------------------------------------------------
#            DRAGGING IMAGE (CIRCLE)
# Image Processing : Part 1
#------------------------------------------------
# Author : Bayu Aditya

import numpy as np
import cv2

mode_gambar = False
ix, iy = -1, -1

def gambar_drag(event, x, y, flags, param):
    global mode_gambar, ix, iy
    if event == cv2.EVENT_LBUTTONDOWN:
        mode_gambar = True
        ix, iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if mode_gambar == True:
            cv2.circle(blank, center = (x,y), radius = 50,
                       color = (255,0,0), thickness = -1)
    elif event == cv2.EVENT_LBUTTONUP:
        mode_gambar = False
        
blank = np.zeros((512, 512, 3), dtype = np.uint8)

cv2.namedWindow('Drag Gambar')
cv2.setMouseCallback('Drag Gambar', gambar_drag)

while True:
    cv2.imshow('Drag Gambar', blank)
    if cv2.waitKey(20) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()