import cv2
import numpy as np
import matplotlib.pyplot as plt

I = cv2.imread("pasargadae.jpg", cv2.IMREAD_GRAYSCALE)

levels = 255

# calculating histogram
def calc_hist(I, levels):
    histogram = np.zeros(256)
    m, n = I.shape

    for u in range(m):
        for v in range(n):
            intensity = I[u, v]

            histogram[int(intensity)] += 1

    return histogram


# calculating CDF
def calc_cdf(hist, bins):
    cdf = np.zeros(bins + 1)

    for i, element in enumerate(hist):
        if i != 0:
            cdf[i] = cdf[i - 1] + element
        else:
            cdf[0] = element

    return cdf


flattened_img = I.flatten()

hist = calc_hist(I, levels)
cdf = calc_cdf(hist, levels)

# normalize CDF
normalized_cdf = (cdf - cdf.min()) / (cdf.max() - cdf.min())
normalized_cdf = normalized_cdf * levels

# mapping
# mapping = ...

# replace intensity
# equalized_image = ...
equalized_image = normalized_cdf[flattened_img]
equalized_image = np.reshape(equalized_image, I.shape)

equalized_image_hist = calc_hist(equalized_image, levels)
equalized_image_cdf = calc_cdf(equalized_image_hist, levels)

fig = plt.figure(figsize=(16, 8))
fig.add_subplot(2, 3, 1)
plt.imshow(I, cmap='gray')
plt.title('pasargadae')
plt.axis('off')

fig.add_subplot(2, 3, 2)
plt.plot(hist)
plt.title('Source histogram')

fig.add_subplot(2, 3, 3)
plt.plot(cdf)
plt.title('Source CDF')

fig.add_subplot(2, 3, 4)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized image')
plt.axis('off')

fig.add_subplot(2, 3, 5)
plt.plot(equalized_image_hist)
plt.title('Equalized histogram')

fig.add_subplot(2, 3, 6)
plt.plot(equalized_image_cdf)
plt.title('Equalized CDF')

plt.show()
