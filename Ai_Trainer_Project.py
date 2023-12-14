import cv2
import numpy as np
import time 

cap = cv2.VideoCapture("AiTrainer/videos/curls.mp4")

while True:
    #success, img = cap.read()
    #img = cv2.resize(img, (1280, 720))
    img = cv2.imread("AiTrainer")
    cv2.imshow("Image", img)
    cv2.waitKey(1)
