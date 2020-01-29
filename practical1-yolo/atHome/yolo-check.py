import cv2
import numpy as np
import time

# Load Yolo
net = cv2.dnn.readNet("yolov3-tiny.weights", "yolov3-tiny.cfg")
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
print("Number of classes:",len(classes))
print(classes)

# Loading camera
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    cv2.imshow("Image", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()