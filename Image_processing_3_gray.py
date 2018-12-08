import cv2

cap = cv2.VideoCapture(0)

print('Masukkan Mode Video')
print('===================')
print('1. Red Green Blue (RGB)')
print('2. Blue Green Red (BGR)')
print('3. Gray (GRAY)')
mode = int(input('Masukkan kode : '))

color = [None, cv2.COLOR_RGB2BGR, cv2.COLOR_RGB2GRAY]

while True:
    
    ret, frame = cap.read()
    
    if mode == 1:
        cv2.imshow('Webcam Gray', frame)
    elif mode == 2:
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        cv2.imshow('Webcam Gray', frame)
    elif mode == 3:
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        cv2.imshow('Webcam Gray', frame)
    else:
        print('input Salah')
        break
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()