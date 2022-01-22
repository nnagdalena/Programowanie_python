import cv2
import numpy as np
from imutils.object_detection import non_max_suppression


HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector()) #nadajemy domyślne współczynniki naszemu HOGowi (teraz ma wykrywać ludzi)


def detector(frame):
    rects, weights = HOGCV.detectMultiScale(frame, winStride=(4, 4), padding=(8,8), scale=1.04)
    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
    c = 1

    for x, y, w, h in pick:
        cv2.rectangle(frame, (x, y), (w, h), (238, 155, 0), 2)
        c += 1

    cv2.putText(frame, f'Number of people detected: {c - 1}', (30, 200), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,255,255), 1)
    cv2.imshow('output', frame)
    return frame
