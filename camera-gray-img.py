import numpy as np
import cv2

cap = cv2.VideoCapture(0)
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
        cv2.imshow('frame',gray)
        # waitKey(0) will display the window infinitely until any keypress 
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()