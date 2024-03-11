import numpy as np
import cv2

# create a VideoCapture object
cap = cv2.VideoCapture('eggs.avi')

# get the dimensions of the frame
# you can also read the first frame to get these
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # width of the frame
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # height of the frame

fourcc = cv2.VideoWriter_fourcc(*'XVID')  # choose codec

# opencv 2.x:
# w = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
# h = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
# fourcc = cv2.cv.CV_FOURCC(*'XVID')

# create VideoWriter object w by h, 30 frames per second
out = cv2.VideoWriter('eggs-reverse.avi', fourcc, 30.0, (w, h))

frame_lists = []

while True:
    ret, I = cap.read()

    frame_lists.append(I)

    if ret == False:  # end of video (or error)
        break

frame_lists.pop()
frame_lists = frame_lists[::-1]

current_frame_index = 0
num_frames = len(frame_lists)
while current_frame_index < num_frames:
    frame = frame_lists[current_frame_index]
    cv2.imshow("frame_list", frame)

    key = cv2.waitKey(33) # ~ 30 frames per second
    if key & 0xFF == ord('q'):
        break

    out.write(frame)
    current_frame_index += 1

cap.release()
out.release()


