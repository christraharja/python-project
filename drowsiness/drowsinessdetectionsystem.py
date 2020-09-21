from scipy.spatial import  distance
import cv2
import dlib

def calculationofEar(eye):
    A = distance.euclidean(eye[1],eye[5])
    B = distance.euclidean(eye[2],eye[4])
    C = distance.euclidean(eye[0],eye[3])
    earRatio = (A + B)/(2.0 * C)
    return  earRatio
cap = cv2.VideoCapture(0)
faceDetector = dlib.get_frontal_face_detector()
dlibFacelandmark = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceDetector(gray)
    for face in faces:

        face_landmarks = dlibFacelandmark(gray, face)
        leftEye = []
        rightEye = []

        for n in range(36, 42):
            x = face_landmarks.part(n).x
            y = face_landmarks.part(n).y
            leftEye.append((x, y))
            next_point = n + 1
            if n == 41:
                next_point = 36
            x2 = face_landmarks.part(next_point).x
            y2 = face_landmarks.part(next_point).y
            cv2.line(frame, (x, y), (x2, y2), (0, 255, 0), 1)

        for n in range(42, 48):
            x = face_landmarks.part(n).x
            y = face_landmarks.part(n).y
            rightEye.append((x, y))
            next_point = n + 1
            if n == 47:
                next_point = 42
            x2 = face_landmarks.part(next_point).x
            y2 = face_landmarks.part(next_point).y
            cv2.line(frame, (x, y), (x2, y2), (0, 255, 0), 1)

        left_ear = calculationofEar(leftEye)
        right_ear = calculationofEar(rightEye)

        EAR = (left_ear + right_ear) / 2
        EAR = round(EAR, 2)
        if EAR < 0.26:
            cv2.putText(frame, "sleepy", (20, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 4)
            cv2.putText(frame, "Do you feel sleepy?", (20, 400),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)
            print("Drowsy")
        print(EAR)

    cv2.imshow("Do you feel sleepy?", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()


