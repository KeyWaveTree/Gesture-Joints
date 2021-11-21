from cv2 import cv2

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

while cv2.waitKey(30)<0:
    ret, frame=cap.read()
    cv2.imshow("출력 예제", frame)

cap.release()
cv2.destroyWindow()