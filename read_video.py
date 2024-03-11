import numpy as np
import cv2

# create a VideoCapture object
cap = cv2.VideoCapture('kntu-computer.avi')

print("cap=\n", cap)
# sometimes this is needed:
#if not cap.isOpened():
#    cap.open();


while True:
    
    # Capture frame-by-frame
    ret, I = cap.read()
    
    if ret == False: # end of video (perhaps)
        print("End of the video")
        break

    # Display I
    cv2.imshow('win1',I)
    
    # key = cv2.waitKey(33) # ~ 30 frames per second
    # key = cv2.waitKey(300) # ~ 30 frames per second
    # key = cv2.waitKey(3) # ~ 30 frames per second

    key = cv2.waitKey()
    # key = cv2.waitKey(0)

    if key & 0xFF == ord('q'): 
        break


cap.release()
cv2.destroyAllWindows()


