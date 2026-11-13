import cv2
import time
import math

vid = cv2.VideoCapture("basquete.mp4")

tracker = cv2.TrackerCSRT_create()
returned, img = vid.read()
bounding_box = cv2.selectROI("tracking", img, False)
tracker.init(img, bounding_box)
print(bounding_box)

def draw_box(img, bounding_box):
    x, y, w, h = int(bounding_box[0]), int(bounding_box[1]), int(bounding_box[2]), int(bounding_box[3])
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3, 1)
    cv2.putText(img, "Rastreando", (75, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

while True:
    check, img = vid.read()
    success, bounding_box = tracker.update(img)

    if success:
        draw_box(img, bounding_box)
    else:
        cv2.putText(img, "Errou", (75, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.imshow("Resultado", img)
    key = cv2.waitKey(25)

    if key == 32:
        print("Interrompido")
        break

vid.release()
cv2.destroyAllWindows()