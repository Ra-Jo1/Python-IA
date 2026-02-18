#Just launch the camera faster that prog_1

import cv2

cam = cv2.VideoCapture(0)

while True:
    ignore,frame = cam.read()

    cv2.imshow("TheEnginneer",frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
