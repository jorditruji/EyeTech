#!/usr/bin/python
import cv2
import numpy as np
car_cascade = cv2.CascadeClassifier('cars3.xml')
vc = cv2.VideoCapture('video2.avi')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('laputa.avi',fourcc, 15.0, (320,240))
rval, frame = vc.read()
while rval:
    
    # car detection.
    #cv2.imwrite("Iiygoage.png", frame)
    cars = car_cascade.detectMultiScale(frame, 1.1, 1)
    ncars = 0    
    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        ncars = ncars + 1
       
        # show result
    reco = frame
    
    out.write(frame)
    rval, frame = vc.read()
        #cv2.imshow("Result",frame)
        #cv2.waitKey(1);
    cv2.imwrite("Iiygoage.png", reco)
    
vc.release()
out.release()
