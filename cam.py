import cv2


cam = cv2.VideoCapture(0)



while True:
    _ , img = cam.read()

    

    cv2.imshow("Hand Gesture vol controller" , img)  # used for description of the video window 
    cv2.waitKey(1)
