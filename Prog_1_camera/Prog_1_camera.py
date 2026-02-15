#Open camera
import cv2

cam = cv2.VideoCapture(0)

While True:
  nothing,frame = cam.read()
  cv2.imshow(frame)

  if waitkey(1) and 0xff == ord('q'):
    break

cam.release()
