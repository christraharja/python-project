import numpy as np
import cv2

i, j, k = 200, 200, -1

cap = cv2.VideoCapture(0)

def takeInput(event, i1, j1, flag, param):
    global i, j, k
    if event == cv2.EVENT_LBUTTONDOWN:
        i = i1
        j = j1
        k = 1


cv2.namedWindow("enter_point")
cv2.setMouseCallback("enter_point", takeInput)

# throwing while loop when the condition is met
while True:

    _, inp_img = cap.read()
    inp_img = cv2.flip(inp_img, 1)
    gray_inp_img = cv2.cvtColor(inp_img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("enter_point", inp_img)

    if k == 1 or cv2.waitKey(30) == 27:
        cv2.destroyAllWindows()
        break
stp = 0
old_pts = np.array([[i, j]], dtype=np.float32).reshape(-1, 1, 2)

mask = np.zeros_like(inp_img)

while True:
    _, new_inp_img = cap.read()
    new_inp_img = cv2.flip(new_inp_img, 1)
    new_gray = cv2.cvtColor(new_inp_img, cv2.COLOR_BGR2GRAY)
    new_pts, status, err = cv2.calcOpticalFlowPyrLK(gray_inp_img,
                                                    new_gray,
                                                    old_pts,
                                                    None, maxLevel=1,
                                                    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,
                                                              15, 0.08))

    for l, s in zip(old_pts, new_pts):
        i, j = l.ravel()
        a, b = s.ravel()
        if cv2.waitKey(2) & 0xff == ord('q'):
            stp = 1

        elif cv2.waitKey(2) & 0xff == ord('w'):
            stp = 0

        elif cv2.waitKey(2) == ord('n'):
            mask = np.zeros_like(new_inp_img)

        if stp == 0:
            mask = cv2.line(mask, (a, b), (i, j), (0, 0, 255), 6)

        cv2.circle(new_inp_img, (i, j), 6, (0, 255, 0), -1)

    new_inp_img = cv2.addWeighted(mask, 0.3, new_inp_img, 0.7, 0)
    cv2.putText(mask, "'q' to gap 'w' - start 'n' - clear", (10, 50),
                cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255))
    cv2.imshow("ouput", new_inp_img)
    cv2.imshow("result", mask)

    gray_inp_img = new_gray.copy()
    old_pts = new_pts.reshape(-1, 1, 2)

    if cv2.waitKey(1) & 0xff == 27:
        break

cv2.destroyAllWindows()
cap.release()