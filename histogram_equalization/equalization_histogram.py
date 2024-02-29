from __future__ import print_function
import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv

# ---------------------------- Using CV2 methods ----------------------------
# src = cv.imread("./Unequalized_Hawkes_Bay_NZ.jpg", flags=0)
#
# if src is None:
#     print('Could not open or find the image:')
#     exit(0)
#
# # histogram and cdf of the original image
# hist, bins = np.histogram(src.flatten(), 256, [0, 256])
# cdf = hist.cumsum()
# cdf_normalized = cdf * float(hist.max()) / cdf.max()
#
# # histogram and cdf of the equalized image
# dst = cv.equalizeHist(src)
# hist, bins = np.histogram(dst.flatten(), 256, [0, 256])
# cdf = hist.cumsum()
# cdf_normalized_equalized = cdf * float(hist.max()) / cdf.max()
#
# # Comparison between Source and Equalized Image
# figure, (axis1, axis2) = plt.subplots(nrows=1, ncols=2)
# axis1.hist(src.flatten(), 256, [0, 256], color='r')
# axis1.plot(cdf_normalized, color='b')
# axis1.set_xlim([0, 256])
# axis1.legend(('cdf of original image', 'histogram of original image'), loc='upper left')
#
# axis2.hist(dst.flatten(), 256, [0, 256], color='r')
# axis2.plot(cdf_normalized_equalized, color='b')
# axis2.set_xlim([0, 256])
# axis2.legend(('cdf of equalized image', 'histogram of equalized image'), loc='upper left')
#
# plt.show()
#
# cv.imshow('Source image', src)
# cv.imshow('Equalized Image', dst)
#
# cv.waitKey(0)
# cv.destroyWindow()
#
# ----------------------------- From Scratch -----------------------------
def compute_histogram(img):
    histogram = np.zeros(256)
    m, n = img.shape

    for u in range(m):
        for v in range(n):
            intensity = img[u, v]

            histogram[int(intensity)] += 1

    return histogram


def compute_cdf(histogram, bins):
    cdf = np.zeros(bins + 1)

    for i, element in enumerate(histogram):
        if i != 0:
            cdf[i] = cdf[i - 1] + element
        else:
            cdf[0] = element

    return cdf


original_img = cv.imread("./Unequalized_Hawkes_Bay_NZ.jpg", flags=0)
# Step1: Flattening
flattened_img = original_img.flatten()

img_histogram = compute_histogram(original_img)
bins = 255
cdf = compute_cdf(img_histogram, bins)

# Step2: Normalizing CDF
normalized_cdf = (cdf - cdf.min()) / (cdf.max() - cdf.min())
normalized_cdf = normalized_cdf * bins

# Step3: New image is obtained
img_new = normalized_cdf[flattened_img]
img_new = np.reshape(img_new, original_img.shape)

histogram_new_img = compute_histogram(img_new)
cdf_new_img = compute_cdf(histogram_new_img, bins)
normalized_cdf_new_img = (cdf_new_img - cdf_new_img.min()) / (cdf_new_img.max() - cdf_new_img.min())
normalized_cdf_new_img = normalized_cdf_new_img * bins

figure, (axis1, axis2) = plt.subplots(nrows=1, ncols=2)

axis1.plot(img_histogram, color='b', label="histogram")
axis1.plot(normalized_cdf, color='r', label="normalizes cdf")
axis1.legend(loc="upper right")

axis2.plot(histogram_new_img, color='b', label="histogram of new img")
axis2.plot(normalized_cdf_new_img, color='r', label="normalized cdf of new img")
axis2.legend(loc="upper right")

plt.show()

# --------------------------- original img VS equalized img ---------------------------
figure, (axis1, axis2) = plt.subplots(nrows=1, ncols=2)
axis1.imshow(original_img, cmap='gray')
axis2.imshow(img_new, cmap='gray')

plt.show()
