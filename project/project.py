
import cv2
import numpy as np

video = cv2.VideoCapture("green video.mp4")
image = cv2.imread("image.jpg")


while True:
    ret, frame =video.read()
    frame = cv2.resize(frame, (600,350))  #resizes the frame
    image=cv2.resize(image, (600, 350))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_g = np.array([32, 94, 132])
    u_g = np.array([179, 255, 255])

    mask = cv2.inRange(hsv, l_g, u_g)
#identifying image from the video
    result = cv2.bitwise_and(frame, frame, mask=mask)
    #subtracting the background from the video
    final = frame-result
     #wherever zero replace with the image and 
    # whenever not zero, reatain the value of final
    green_screen = np.where(final==0, image, final)
    cv2.imshow("Frame", frame)
    #cv2.imshow("Mask", mask)
    #cv2.imshow("Image", image)
    #cv2.imshow("result", result)
    #cv2.imshow("final", final)
    cv2.imshow("green screen", green_screen)

    k=cv2.waitKey(1) #saves the key pressed to k
    if k==ord('q'): #checks if the key pressd == to 'q'
        break
video.release()
#image.release()
cv2.destroyAllWindows()   # destroys the frame  and everytime the project is debugged new resources are allocated