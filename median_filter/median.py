import cv2
import numpy as np

# --- Read noisy image
path = "noisy1.PNG"
img = cv2.imread(path)

# --- Get gray scale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ---- define height and width of image
height = gray_img.shape[0]
width = gray_img.shape[1]

# ---- define image result
result_img = np.ones((height, width), dtype=np.uint8)

# ---- calculate median for each pixel
for i in range(1, height - 1):
    for j in range(1, width - 1):
        temp_list = [gray_img[i][j], gray_img[i - 1][j], gray_img[i][j - 1], gray_img[i - 1][j - 1], gray_img[i + 1][j],
                     gray_img[i][j + 1], gray_img[i + 1][j + 1], gray_img[i + 1][j - 1], gray_img[i - 1][j + 1]]
        result_img[i][j] = np.median(temp_list)

cv2.imshow("result", gray_img)
cv2.imshow("result_filter", result_img)
cv2.waitKey(0)
