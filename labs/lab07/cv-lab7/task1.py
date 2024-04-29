import numpy as np
import cv2

I = cv2.imread('coins.jpg')


G = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
G = cv2.GaussianBlur(G, (5,5), 0);


canny_high_threshold = 122
min_votes = 115  # minimum no. of votes to be considered as a circle
min_centre_distance = 35  # minimum distance between the centres of detected circles
resolution = 2  # resolution of parameters (centre, radius) relative to image resolution
circles = cv2.HoughCircles(G, cv2.HOUGH_GRADIENT, resolution, min_centre_distance,
                           param1=canny_high_threshold,
                           param2=min_votes, minRadius=10, maxRadius=80)

#
# canny_high_threshold = 160
# min_votes = 80 # minimum no. of votes to be considered as a circle
# min_centre_distance = 40

# circles = np.array([[10,10]])

for c in circles[0,:]:
    x = int(c[0])
    y = int(c[1])
    r = int(c[2])

    cv2.circle(I,(x,y), r, (0,255,0),2)
    cv2.circle(I, (x, y), 2, color=(0, 0, 255), thickness=2)




print(circles.shape)
    
n = circles.shape[1]
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(I,'There are %d coins!'%n,(400,40), font, 1,(255,0,0),2)

cv2.imshow("I",I)
cv2.waitKey(0)

