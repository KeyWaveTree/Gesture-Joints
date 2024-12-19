from cv2 import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,800)

while cv2.waitKey(30)<0:
    ret, frame=cap.read()
    cv2.imshow("Video", frame)

cap.release()
cv2.destroyAllWindows()