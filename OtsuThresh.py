#!/usr/bin/env python
# coding: utf-8

import numpy as np
import random
import cv2

#TACHE TAMAZOUZT ABDERRAHMANE

#FIN DU TACHE 


# In[17]:



img=cv2.imread ("image1.jpeg");
imgclear = cv2.imread("image1.tif",0)
imgnoise = cv2.imread("image_noise.tif",0)
#hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#h,s,v= cv2.split(hsv)
#ret_h, th_h = cv2.threshold(h,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#ret_s, th_s = cv2.threshold(s,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#ret_v, th_v = cv2.threshold(s,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret,th = cv2.threshold(imgclear,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
retn,thn = cv2.threshold(imgnoise,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#cv2.imwrite("th_h.png",th_h)
#cv2.imwrite("th_s.png",th_s)
#cv2.imwrite("th_v.png",th_v)


cv2.imwrite("otsuclear.tif",th)
cv2.imwrite("otsunoise.tif",thn)


# In[ ]:




