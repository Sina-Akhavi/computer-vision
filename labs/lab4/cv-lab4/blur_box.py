import numpy as np
import cv2
from matplotlib import pyplot as plt

I = cv2.imread('isfahan.jpg').astype(np.float64) / 255

# display the original image
cv2.imshow('original', I)

# creating a box filter
m = 7  # choose filter size

# create an m by m box filter
F = np.ones((m, m), np.float64) / (m * m)
print(F)


# Now, filter the image
J = cv2.filter2D(I, -1, F)
blur = cv2.blur(I, (m, m))

cv2.imshow('blurred by filter2D', J)
cv2.imshow('blurred by blur', blur)

cv2.waitKey()

cv2.destroyAllWindows()

# task2