import cv2
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
cam = cv2.VideoCapture(0)

while True:
    isTrue, image = cam.read()
    faces = faceCascade.detectMultiScale(image,1.5,3, minSize = (30,30))

    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(225,225,0),2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image,"Target Face",(x,y-10),font,0.5,(0,0,255))

    cv2.imshow("Face Recognition System", image)

    l = cv2.waitKey(1)
    if l == 27:
        break

cam.release()
cv2.destroyAllWindows()





