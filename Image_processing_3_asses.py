import cv2

cap = cv2.VideoCapture(0)

clicked = False
center = (0,0)

def fungsi_circle(event, x, y, flags, param):
    global center, clicked
    
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked = True
        center = (x,y)
        
    elif event == cv2.EVENT_LBUTTONUP:
        clicked = False
        
cv2.namedWindow('Webcam Circle Drawing')
cv2.setMouseCallback('Webcam Circle Drawing', fungsi_circle)

while True:
    ret, frame = cap.read()
    
    if clicked == True:
        cv2.circle(frame, center = center, radius = 50, color = (255,0,0), thickness = 4)
    
    cv2.imshow('Webcam Circle Drawing', frame)
    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()