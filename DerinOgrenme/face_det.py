import numpy as np
import cv2
import imageio
import os

#face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
face_cascade = cv2.CascadeClassifier('C:\pytry\DerinOgrenme\haarcascade-eye.xml')
eye_cascade = cv2.CascadeClassifier('C:\pytry\DerinOgrenme\haarcascade__eye.xml')

def detect(frame):
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # Renkli resmi siyahbeyaza çevrir.
    
    # yüz tespiti ayarları --- 1.3 ölçeklendirme faktörü. Resim küçültülecek. 5 de komşu sayısı. En az 5 defa yüz tespit etmişse yüz var desin.
    faces = face_cascade.detectMultiScale(gray,1.3,5)

# x yatay eksen, y dikey ekseni yüzün yeri. w = weight, h = height 
    for (x,y,w,h) in faces: # bu döngü ile her bulduğumuz yüze dikdörtgen çizecek
        #yüze dikdörtgen çizecek.ilk parametre yüzümüz,
        # ikincisi sol üst köşenin koordinatı verilir. içinci sağ alt köşe,dördüncü parametre renkler,son parametre dikdörtge çizgi kalınlığıdır.
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2) 
        #alttaki satırda yüzün içinde göz arayacağız. Böylelikle bilgisayarı yormamış olacağız.
        gray_face = gray[y:y+h,x:x+w] # yüzün siyahbeyaz hali
        color_face = frame[y:y+h,x:x+w] # yüzün renkli hali.
        #göz tespiti için ayarlar.
        eyes = face_cascade.detectMultiScale(gray_face,1.1,3)# göz tespiti içindir.
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(color_face,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    return frame   
dir_path = os.path.dirname(os.path.realpath(__file__))   
reader = imageio.get_reader(dir_path+"\\"+"1.mp4")
fps = reader.get_meta_data()['fps']
writer = imageio.get_writer(dir_path+"\\"+"output.mp4",fps=fps)
for i, frame in enumerate(reader):
    frame = detect(frame)
    writer.append_data(frame)
    print(i)
writer.close()

#print(cv2.__version__)
