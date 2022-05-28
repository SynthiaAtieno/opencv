
import cv2
import numpy as np

video = cv2.VideoCapture("green video.mp4")
image = cv2.imread("download(4).jpg")

while True:
    ret, frame =video.read()
    frame = cv2.resize(frame, (600,350))  #resizes the frame

    cv2.imshow("Frame", frame)
    k=cv2.waitKey(1) #saves the key pressed to k
    if k==ord('q'): #checks if the key pressd == to 'q'
        break
video.release()
cv2.destroyAllWindows()   # destroys the frame  and everytime the project is debugged new resources are allocated