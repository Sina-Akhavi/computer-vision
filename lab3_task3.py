import cv2
import numpy as np
import matplotlib.pyplot as plt

I = cv2.imread("pasargadae.jpg", cv2.IMREAD_GRAYSCALE)

levels = 256

# calculating histogram
def calc_hist(I, levels):
  hist = np.zeros(levels)
  ...
  return hist


# calculating CDF
def calc_cdf(hist, levels):
  cdf = np.zeros_like(hist)
  ...
  return cdf

hist = calc_hist(I, levels)
cdf = calc_cdf(hist, levels)

# normalize CDF
...

# mapping
mapping = ...

# replace intensity
equalized_image = ...

equalized_image_hist = calc_hist(equalized_image, levels)
equalized_image_cdf = calc_cdf(equalized_image_hist, levels)

fig = plt.figure(figsize= (16, 8))
fig.add_subplot(2,3,1)
plt.imshow(I, cmap='gray')
plt.title('pasargadae')
plt.axis('off')

fig.add_subplot(2,3,2)
plt.plot(hist)
plt.title('Source histogram')

fig.add_subplot(2,3,3)
plt.plot(cdf)
plt.title('Source CDF')

fig.add_subplot(2,3,4)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized image')
plt.axis('off')

fig.add_subplot(2,3,5)
plt.plot(equalized_image_hist)
plt.title('Equalized histogram')


fig.add_subplot(2,3,6)
plt.plot(equalized_image_cdf)
plt.title('Equalized CDF')

plt.show()