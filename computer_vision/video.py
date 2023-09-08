import cv2
import numpy as np

# file Path
file = r'C:\Users\prosecution\Desktop\New folder (5)\Gullak S01.mp4' #raw string
vid = cv2.VideoCapture(file)

while True:
    state, image = vid.read()
    if not state: break
    # resize to 500*500
    sm_image_1 = cv2.resize(image, (500,500)) #fixed size
    sm_image_2 = cv2.resize(image, None, fx=.25, fy=.25) #scaledown by 25%
    #filter
    bw_image = cv2.cvtColor(sm_image_2, cv2.COLOR_BGR2GRAY)
    rgb_image = cv2.cvtColor(sm_image_2, cv2.COLOR_BGR2RGB)
    #edge filter for outlines
    edge_image = cv2.Canny(rgb_image, 100, 200)


    cv2.imshow('video 1', sm_image_1)
    cv2.imshow('video 2', sm_image_2)
    cv2.imshow('bw', bw_image)
    cv2.imshow('rgb', rgb_image)
    cv2.imshow('edge', edge_image)
    key = cv2.waitKey(10)
    if key == 27: break
cv2.destroyAllWindows()
vid.release()