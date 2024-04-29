import cv2
import numpy as np
from matplotlib import pyplot as plt

f, axes = plt.subplots(2, 3)


def compute_histogram(img):
    histogram = np.zeros(256)
    m, n = img.shape

    for u in range(m):
        for v in range(n):
            intensity = img[u, v]

            histogram[int(intensity)] += 1

    return histogram


def compute_a_b(image):
    image = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    a = None
    b = None

    w, h = image.shape
    # compute histogram
    histogram = compute_histogram(image)
    # obtain number of all pixels
    num_pixels = w * h
    # Iterate through the histogram and pass the 10 perent of the points (get a)
    tail_length = int(0.01 * num_pixels)
    head_length = int(0.99 * num_pixels)

    passed_num_points = 0
    for i in range(255):
        passed_num_points += histogram[i]

        if tail_length <= passed_num_points:
            a = i
            break
    # Iterate through the histogram and pass the 90 perent of the points (get b)

    passed_num_points = 0
    for i in range(255):
        passed_num_points += histogram[i]

        if head_length <= passed_num_points:
            b = i
            break

    return a, b


fname = 'crayfish.jpg'
a, b = compute_a_b(fname)
# print(f'a={a}, b={b}')

# a = 100
# b = 200

# fname = 'map.jpg'
# a, b = compute_a_b(fname)
# print(f'a={a}, b={b}')
# a = 150
# b = 220
#
# fname = 'terrain.jpg'
# a, b = compute_a_b(fname)
# print(f'a={a}, b={b}')
# a = 120
# b = 250

# fname = 'train.jpg'
# a, b = compute_a_b(fname)
# print(f'a={a}, b={b}')
# a = 80
# b = 230

# fname = 'branches.jpg'
# a, b = compute_a_b(fname)
# print(f'a={a}, b={b}')
# a = 140
# b = 220

I = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)

axes[0, 0].imshow(I, 'gray', vmin=0, vmax=255)
axes[0, 0].axis('off')

axes[1, 0].hist(I.ravel(), 256, [0, 256]);

J = (I - a) * 255.0 / (b - a)
J[J < 0] = 0
J[J > 255] = 255
J = J.astype(np.uint8)

axes[0, 1].imshow(J, 'gray', vmin=0, vmax=255)
axes[0, 1].axis('off')

axes[1, 1].hist(J.ravel(), 256, [0, 256]);

K = cv2.equalizeHist(I)

axes[0, 2].imshow(K, 'gray', vmin=0, vmax=255)
axes[0, 2].axis('off')

axes[1, 2].hist(K.ravel(), 256, [0, 256]);

plt.show()
