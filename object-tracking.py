import cv2
import math

p1 = 530
p2 = 300

xs = []
ys = []

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

def goal_track(img, bounding_box):
    x, y, w, h = int(bounding_box[0]), int(bounding_box[1]), int(bounding_box[2]), int(bounding_box[3])
    c1 = x + int(w / 2)
    c2 = y + int(h / 2)
    cv2.circle(img, (c1, c2), 2, (0, 0, 255), 5)
    cv2.circle(img, (int(p1), int(p2)), 2, (0, 255, 0), 3)

    dist = math.sqrt(((c1 - p1)**2) + ((c2 - p2)**2))
    print(dist)

    if dist <= 20:
        cv2.putText(img, "Cesta!", (300, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)


while True:
    check, img = vid.read()
    success, bounding_box = tracker.update(img)

    if success:
        draw_box(img, bounding_box)
    else:
        cv2.putText(img, "Errou", (75, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    goal_track(img, bounding_box)
    cv2.imshow("Resultado", img)
    key = cv2.waitKey(25)

    if key == 32:
        print("Interrompido")
        break

vid.release()
cv2.destroyAllWindows()