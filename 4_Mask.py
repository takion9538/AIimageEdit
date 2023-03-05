import cv2
import sys

src = cv2.imread()
mask = cv2.imread('', cv2.IMREAD_GRAYSCALE)
dst = cv2.imread()

if src is None or mask is None or dst is None :
    print('오류')
    sys.exit()

cv2.copyTo(src, mask, dst=None)

cv2.imshow('src', src)
cv2.imshow('mask', mask)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()