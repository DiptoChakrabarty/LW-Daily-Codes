import cv2
def photoclick():
	face=cv2.CascadeClassifier("/root/Desktop/Github/CV/haarcascade_frontalface_default.xml")
	cap=cv2.VideoCapture(0)
	ret,photo=cap.read()
	cr=face.detectMultiScale(photo)
	for (x,y,w,h) in cr:
	#x,y,w,h=face.detectMultiScale(photo)
		face_save=photo[x:x+w,y:y+h]
	face_final=cv2.cvtColor(face_save,cv2.COLOR_BGR2GRAY)
	cv2.imwrite("Face{}.png".format(i+84),face_final)
	cap.release()

for i in range(50):
	photoclick()

