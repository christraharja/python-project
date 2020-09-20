import cv2
import numpy as np 

Face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
Smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

cap = cv2.VideoCapture(0)

while True:
	ret, img = cap.read()
	g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = Face_cascade.detectMultiScale(
		g,
		scaleFactor=1.3,
        minNeighbors=5,      
        minSize=(30, 30)
    )

	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		Rgray = g[y:y+h, x:x+w]
		smile = Smile_cascade.detectMultiScale(
			Rgray,
            scaleFactor= 1.5,
            minNeighbors=15,
            minSize=(25, 25),
            )

		for k in smile:
			if len(smile) > 1:
				cv2.putText(img,"smilling",(x,y-25),cv2.FONT_HERSHEY_SIMPLEX,
                    2,(0,255,0),3,cv2.LINE_AA)

	cv2.imshow('video',img)
	y = cv2.waitKey(30) & 0xff
	if y == 27:
		break

cap.release()
cv2.destroyAllWindows()
