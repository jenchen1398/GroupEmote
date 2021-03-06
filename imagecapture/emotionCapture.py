import numpy as np
import cv2
import time
#import emotion
cap = cv2.VideoCapture("G:\git_repos\GroupEmote\imagecapture\Dataset\ConAndyVid.mp4")

#faces = none
cascPath = 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)


cv2.startWindowThread()
rectangleColor= (0,255,0)

ret,frame = cap.read()
print(ret)
cntf = 0
while(ret):
    #cntf+=1
    ret, frame = cap.read()

    # Our operations on the frame come here
    if cntf%10==0:
        cntf=0
        gray =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags = cv2.CASCADE_SCALE_IMAGE
        )
        # Display the resulting frame
        cnt = 0
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            subface = gray[y:y+h, x:x+w]
            #cv2.imshow('subface',subface)
            #feeling = emotion.get(subface)
            cv2.putText(frame,str(cnt)+' ',(x,y+h+25),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2,cv2.LINE_AA)
            cnt+=1

        cv2.putText(frame,'FACES'+str(len(faces)), (0,frame.shape[0]), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255), 2, cv2.LINE_AA)
        cv2.imshow('frame',frame)


    cv2.imshow('frame',frame)
        #print("faces",len(faces))
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break




#When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
