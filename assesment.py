import cv2

face = cv2.CascadeClassifier('DATA/haarcascades/haarcascade_frontalface_default.xml')
eyes = cv2.CascadeClassifier('DATA/haarcascades/haarcascade_eye.xml')
full_body = cv2.CascadeClassifier('DATA/haarcascades/haarcascade_fullbody.xml')

cascade = [face, eyes, full_body]
color = [(0,0,255), (0,255,0), (255,0,0)]

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    for i in range(len(cascade)):
        location = cascade[i].detectMultiScale(frame, scaleFactor = 1.7)
        for x, y, w, h in location:
            cv2.rectangle(frame, (x,y), (x+w, y+h), color[i], thickness = 5)

    
    cv2.imshow('Webcam', frame)
    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()