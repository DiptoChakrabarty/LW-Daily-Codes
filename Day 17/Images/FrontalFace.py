import cv2
cv2.CascadeClassifier("/root/Desktop/Github/CV/haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)
ret,photo=cap.read()
cr=face.detectMultiScale(photo)
for (x,y,w,h) in cr:
	face_save=photo[x:x+w,y:y+h]
face_final=cv2.cvtColor(face_save,cv2.COLOR_BGR2GRAY)
cv2.imwrite("Face.png",face_final)
cap.release()

