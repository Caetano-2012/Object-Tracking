import cv2
import time
import math

vid = cv2.VideoCapture("basquete.mp4")

while True:
    check, img = vid.read()
    cv2.imshow("Resultado", img)
    key = cv2.waitKey(25)

    if key == 32:
        print("Interrompido")
        break

vid.release()
cv2.destroyAllWindows()