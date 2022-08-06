# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 19:13:23 2022

@author: Anuraag Das
"""
import numpy as np
import cv2
import time
import urllib.request
import time
URL="http://25.116.193.207:8080/shot.jpg"
while True:
    img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
    img = cv2.imdecode(img_arr,-1)
    cv2.imshow('IPWebcam',img)
    q = cv2.waitKey(1)
    if q == ord("q"):
        break;
cv2.destroyAllWindows()