import cv2
import imageio

#face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
face_cascade = cv2.CascadeClassifier('C:\pytry\DerinOgrenme\haarcascade-eye.xml')
eye_cascade = cv2.CascadeClassifier('C:\pytry\DerinOgrenme\haarcascade__eye.xml')

def detect(frame):
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        gray_face = gray[y:y+h,x:x+w]
        color_face = frame[y:y+h,x:x+w]
        eyes = face_cascade.detectMultiScale(gray_face,1.1,3)
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(color_face,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    return frame        

#print(cv2.__version__)
