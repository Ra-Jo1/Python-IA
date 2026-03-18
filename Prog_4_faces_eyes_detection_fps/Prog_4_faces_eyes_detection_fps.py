#Use openCV to detect multiplefaces, eyes and calcul fps run on py 3.14

import cv2
import time

height = 360
width = 640

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

facecascade = cv2.CascadeClassifier('haar/haarcascade_frontalface_default.xml') #Face detection
eyecascade = cv2.CascadeClassifier('haar/haarcascade_eye.xml') #Eyes detection

fps = 10
timeStart = time.time()

while True:
    ignore,frame = cam.read()
  
    framegray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #this conversion allow use to use less computations
    faces = facecascade.detectMultiScale(framegray,1.3,5) #use the model to detect faces
    eyes = eyecascade.detectMultiScale(framegray,1.3,5) #use the model to detect eyes
  
    for face in faces:
        x,y,w,h = face #face wait 4 parameters
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
        frameface = frame[y:y+h,x:x+w] #crop the face from the gray frame
        framefacegray = cv2.cvtColor(frameface,cv2.COLOR_BGR2GRAY) #convert the face to gray
        eyes = eyecascade.detectMultiScale(framefacegray,1.3,5) #use the model to detect eyes in the face area
        for eye in eyes:
            xeye,yeye,weye,heye = eye #eye wait 4 parameters
            cv2.rectangle(frame,(xeye+x,yeye+y),(xeye+x+weye,yeye+y+heye),(255,255,255),3)

    
        
    looptime = time.time() - timeStart
    timeStart = time.time()
    fpsnew = 1/looptime
    fps = .9*fps + .1*fpsnew
    cv2.putText(frame,"FPS: "+str(int(fpsnew)),(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
    
    cv2.imshow("TheEnginneer",frame)
    cv2.moveWindow("TheEnginneer",0,0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
