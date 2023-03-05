import cv2

img1 = cv2.imread('../Day5/cat.bmp')
# img2 = img1
# img3 = img1.copy()

img2 = img1[64:300, 165:]
img3 = img1[64:300, 165:].copy()

img2.fill(0)

# h = 597, w = 593

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()
cv2.destroyAllWindows()