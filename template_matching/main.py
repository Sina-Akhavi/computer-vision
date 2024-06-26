import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('messi.jpeg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"

img2 = img.copy()
template = cv.imread('template.png', cv.IMREAD_GRAYSCALE)

w, h = template.shape[::-1]
w_img, h_img = img2.shape[::-1]

method = 'cv.TM_CCORR_NORMED'
method2 = 'cv.TM_CCORR'

img = img2.copy()
method2 = eval(method2)

res = cv.matchTemplate(img, template, method2)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

cv.rectangle(img, top_left, bottom_right, 255, 2)

plt.subplot(121), plt.imshow(res, cmap='gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img, cmap='gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
# plt.suptitle(method)

plt.show()