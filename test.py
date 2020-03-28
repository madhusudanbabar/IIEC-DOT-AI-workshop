# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%% imports
import cv2

#%% 
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
if ret == True:
    cv2.imshow("win", frame)
    cv2.waitKey(2000)

cap.release()
cv2.destroyAllWindows()