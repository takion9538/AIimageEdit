import numpy as np
import cv2

img1 = np.empty((240, 320), dtype=np.uint8) # 노이즈가 존재
img1 = np.zeros((240, 320, 3), dtype=np.uint8)
img1 = np.ones((240, 320), dtype=np.uint8) * 255
img1 = np.full((240, 320, 3), (0, 255, 255), dtype=np.uint8)


cv2.imshow('img1', img1)
cv2.waitKey()
cv2.destroyAllWindows()