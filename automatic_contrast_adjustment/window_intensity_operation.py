import cv2
import numpy as np
import matplotlib.pyplot as plt

img_obj = cv2.imread("./original_image.png", flags=0)


# print("image shape=", img_obj.shape)
# print("image=", img_obj)

def plot_histogram(histogram, axis, title):

    axis.set_title(title, fontdict={'fontsize': 10, 'color': 'blue'})
    # print("HISTOGRAM =\n", histogram)

    axis.plot(histogram, color='r')
    axis.set_ylim([0, 1000])
    axis.set_xlim([0, 256])

    axis.set_xlabel("Intensity")
    axis.set_ylabel("Frequency")
    axis.margins(1)

    axis.grid(True)


def compute_histogram(img):
    histogram = np.zeros(256)
    m, n = img.shape

    for u in range(m):
        for v in range(n):
            intensity = img[u, v]

            histogram[int(intensity)] += 1

    return histogram


def make_background_black(image, threshold):
    m, n = image.shape
    J = np.zeros((m, n))

    for u in range(m):
        for v in range(n):
            if image[u, v] <= threshold:
                J[u, v] = 0
            else:
                J[u, v] = image[u, v]

    return J


def window_intensity_operation(img, low_intensity, high_intensity):
    m, n = img.shape

    J = np.zeros((m, n))
    for u in range(m):
        for v in range(n):
            if img[u, v] <= low_intensity:
                J[u, v] = 0
            elif img[u, v] >= high_intensity:
                J[u, v] = 255
            else:
                J[u, v] = 255 * (img[u, v] - low_intensity) / (high_intensity - low_intensity)

    return J


# -------------------- make background_black test case 1 --------------------
# J = make_background_black(img_obj, threshold=35)
# cv2.imwrite("./output/black_background.png", J)
#
# # print("J=", J)
# histogram_j = compute_histogram(J)
# plot_histogram(histogram_j, title="altered image histogram")

# --------------------- window_intensity_operation test case 1 ---------------------
# low_intensity = 35
# high_intensity = 210
#
# J = window_intensity_operation(img_obj, low_intensity, high_intensity)
# cv2.imwrite("./output/windowed_img.png", J)
#
# histogram = compute_histogram(J)
# plot_histogram(histogram, title="windowed image histogram")

# ---------------------- main task ----------------------
# create plots
figure, (axis1, axis2, axis3) = plt.subplots(nrows=1, ncols=3, sharey=True)

high_intensity = 210
low_intensity = 35

img_histogram = compute_histogram(img_obj)

J_blackened_background = make_background_black(img_obj, threshold=low_intensity)
blackened_background_histogram = compute_histogram(J_blackened_background)
cv2.imwrite("./output/blackened_img.png", J_blackened_background)

windowed_img = window_intensity_operation(img_obj, low_intensity, high_intensity)
cv2.imwrite("./output/windowed_img.png", windowed_img)
windowed_histogram = compute_histogram(windowed_img)

# plot histograms
plot_histogram(img_histogram, axis1, title="image histogram")
plot_histogram(blackened_background_histogram, axis2, title="blackened image histogram")
plot_histogram(windowed_histogram, axis3, title="windowed image histogram")

plt.show()
# --------------------- another method ---------------------

# histo = cv2.calcHist(img_obj, [0], None, [256], [0, 256])
#
# plt.plot(histo, 'g')
# plt.show()
