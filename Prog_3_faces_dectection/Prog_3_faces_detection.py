#Use openCV to detect multiplefaces run on py 3.14

import cv2

height = 360
width = 640

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

facecascade = cv2.CascadeClassifier('haar/haarcascade_frontalface_default.xml')

while True:
    ignore,frame = cam.read()
  
    framegray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #this conversion allow use to use less computations
    faces = facecascade.detectMultiScale(framegray,1.3,5) #use the model to detect faces
  
    for face in faces:
        x,y,w,h = face #face wait 4 parameters
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
    
    cv2.imshow("TheEnginneer",frame)
    cv2.moveWindow("TheEnginneer",0,0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
