import cv2
import numpy as np

I = cv2.imread('polygons.jpg')
G = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
ret, T = cv2.threshold(G, 220, 255, cv2.THRESH_BINARY_INV)
nc1, CC1 = cv2.connectedComponents(T)

for k in range(1, nc1):
    Ck = np.zeros(T.shape, dtype=np.float32)
    Ck[CC1 == k] = 1
    Ck = cv2.GaussianBlur(Ck, (5, 5), 0)
    Ck = cv2.cvtColor(Ck, cv2.COLOR_GRAY2BGR)
    Ck = np.float32(Ck)
    # Calculate Harris scores
    window_size = 5
    soble_kernel_size = 3
    alpha = 0.04
    H = cv2.cornerHarris(cv2.cvtColor(Ck, cv2.COLOR_BGR2GRAY), window_size, soble_kernel_size, alpha)
    H = H / H.max()  # Normalize scores
    H[H < 0.01] = 0  # Threshold scores

    # Apply non-maximum suppression
    corners = []
    for y in range(1, H.shape[0] - 1):
        for x in range(1, H.shape[1] - 1):
            if H[y, x] > 0:
                neighborhood = H[y - 1:y + 2, x - 1:x + 2]
                if np.max(neighborhood) == H[y, x]:
                    corners.append((x, y))

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(Ck, 'There are %d vertices!' % len(corners), (20, 30), font, 1, (0, 0, 255), 1)

    for x, y in corners:
        cv2.circle(Ck, (x, y), 3, (0, 0, 255))
    cv2.imshow('corners', Ck)
    cv2.waitKey(0)