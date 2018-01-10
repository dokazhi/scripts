# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 16:49:03 2017

@author: dos
"""
import cv2
import dlib
from skimage import io
from scipy.spatial import distance

sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')
detector = dlib.get_frontal_face_detector()

img = io.imread('check.jpg')
win1 = dlib.image_window()
win1.clear_overlay()
win1.set_image(img)

dets = detector(img,1)
for k, d in enumerate(dets):
    print('Detection {}: left:{} top:{} right:{} bottom{}'.format(k,d.left(),d.top(),d.right(),d.bottom()))
    shape = sp(img,d)
    win1.clear_overlay()
    win1.add_overlay(d)
    win1.add_overlay(shape)
    
face_descriptor1 = facerec.compute_face_descriptor(img,shape)
#print(face_descriptor1)

#2nd load
img = io.imread('web1.jpg')
win2 = dlib.image_window()
win2.clear_overlay()
win2.set_image(img)
dets_webcam = detector(img,1)
for k, d in enumerate(dets_webcam):
    print('Detection {}: left:{} top:{} right:{} bottom{}'.format(k,d.left(),d.top(),d.right(),d.bottom()))
    shape = sp(img,d)
    win2.clear_overlay()
    win2.add_overlay(d)
    win2.add_overlay(shape)
    
face_descriptor2 = facerec.compute_face_descriptor(img,shape)

#меньше 0.6 похожи а если больше то нет
a = distance.euclidean(face_descriptor1, face_descriptor2)
print(a)

cap = cv2.VideoCapture(0)
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    dets_webcam = detector(img,1)
    for k, d in enumerate(dets_webcam):
        print('Detection {}: left:{} top:{} right:{} bottom:{}'.format(k,d.left(),d.top(),d.right(),d.bottom()))
        shape = sp(img,d)
        
        cv2.rectangle(img,(d.left(),d.top()),(d.right(),d.bottom()), (255,0,0),2)
        # cv2.rectangle(img,(shape.left(),shape.top()),(shape.right(),shape.bottom()), (255,255,0),2)
        win2.clear_overlay()
        win2.add_overlay(d)
        win2.add_overlay(shape)
        
        for i in range(shape.num_parts):
            cv2.circle(img, (shape.part(i).x,shape.part(i).y), 1, (255,255,0), -1)
            
    
    face_descriptor2 = facerec.compute_face_descriptor(img,shape)

    a = distance.euclidean(face_descriptor1, face_descriptor2)
    cv2.putText(img,str(a),(5,30), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255),1,cv2.LINE_AA)
    cv2.imshow('winname', img)
    k=cv2.waitKey(30) & 0xff
    #print(d.left(),d.top(),d.right(),d.bottom())
    if k == 115:
        face=img[d.top():d.left()+50, d.bottom()-50:d.right()]
        # win3 = dlib.image_window()
        # win3.clear_overlay()
        # win3.set_image(face)
        cv2.imwrite('face.jpg', face)
        cv2.imshow('12', face)
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()