import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(1)
cap.set(3,1280)
cap.set(4,720)
detector = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    # Get image frame
    success, img = cap.read()
    # img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
