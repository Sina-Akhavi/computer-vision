import numpy as np
import cv2

I = cv2.imread('isfahan.jpg', cv2.IMREAD_GRAYSCALE);
I = I.astype(np.float64) / 255

sigma = 0.04  # initial standard deviation of noise

while True:
    # Apply noise to the original image I
    N = np.random.randn(*I.shape) * sigma
    J = I + N

    cv2.imshow('snow noise', J)

    # press any key to exit
    key = cv2.waitKey(33)
    if key & 0xFF == ord('u'):  # if 'u' is pressed
        sigma += 0.01

    elif key & 0xFF == ord('d'):  # if 'd' is pressed
        if sigma < 0.01:
            continue
        sigma -= 0.01

    elif key & 0xFF == ord('q'):  # if 'q' is pressed then
        break  # quit


cv2.destroyAllWindows()
