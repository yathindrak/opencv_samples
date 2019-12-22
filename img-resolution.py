import numpy as np
import cv2

cap = cv2.VideoCapture(0)

def make_1080p():
    cap.set(3, 1920)
    cap.set(4, 1080)

def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)

def make_480p():
    cap.set(3, 640)
    cap.set(4, 480)

def change_res(width, height):
    cap.set(3, width)
    cap.set(4, height)

make_1080p()
# change_res(4000, 2000)

print(cap.get(3))
if cap.isOpened():
    # infinite loop
    while(True):
        #capture frame by frame
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame',frame)
        # waitKey(0) will display the window infinitely until any keypress 
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()