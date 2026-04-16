#Open camera
import cv2

cam = cv2.VideoCapture(0)

while True:
  nothing,frame = cam.read()
  cv2.imshow("Yo_World",frame)

  if cv2.waitKey(1) & 0xff == ord('q'):
    break

cam.release()
