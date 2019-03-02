import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray_img)

    corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
    corners =  np.int0(corners)

    for corner in corners:
        x, y = corner.ravel()
        cv2.circle(frame, (x,y), 3, 255, -1)
    

    cv2.imshow("Coners", frame)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break


cv2.destoryAllWindows()
cap.release()
