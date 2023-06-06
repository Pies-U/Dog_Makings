import cv2

def calculate_rectangle_center(width, height, x1, y1):
    x2 = x1 + width
    y2 = y1 + height
    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2
    return center_x, center_y

def crop(frame,center_x, center_y, width, height):
        
    x1 = int(center_x - width/2)
    y1 = int(center_y - height/2)
    x2 = int(center_x + width/2)
    y2 = int(center_y + height/2)

    if x1 < 0:
        x1 = 0
    
    if x2 < 0:
        x2 = 0
    
    if y1 < 0:
        y1 = 0

    if y2 < 0:
        y2 = 0

    return frame[y1:y2, x1:x2]

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_fullbody.xml")

while True:
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)

    for (x, y, width, height) in faces:
        pass

    if len(faces) >= 1:
        for face in faces:
            center = calculate_rectangle_center(width,height,x,y)
            centerX = int(center[0])
            centerY = int(center[1])
            crop_img = crop(frame,centerX,centerY,350,300)
            cv2.imshow("Camera", crop_img)
    else:
        cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()