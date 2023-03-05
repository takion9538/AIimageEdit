import cv2

img1 = cv2.imread('../Day5/cat.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('../Day5/cat.bmp')

print('type(img1) : ', type(img1))
print('img1.shape : ', img1.shape)
print('img2.size : ', img2.size)
print('img2.dtype : ', img2.dtype)

h, w = img2.shape[:2] # h = 480, w = 640
print('img2 size = {} * {}'.format(w, h))

if len(img1.shape) == 2 :
    print('GRAYSCALE')
elif len(img1.shape) == 3 :
    print('COLOR')

if len(img2.shape) == 2 :
    print('GRAYSCALE')
elif len(img2.shape) == 3 :
    print('COLOR')

# for 문을 통해 픽셀값을 변경하는 작업은 매우 트래픽을 많이 소모하는 작업이기 때문에 사용하면 안된다
# for y in range(h) :
#     for x in range(w) :
#         img1[y, x] = 255
#         img2[y, x] = (0, 0, 255) # BGR 이기 때문에 빨간색

img1[:,:] = 255
img2[:,:] = (0, 0, 255)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey()
cv2.destroyAllWindow()








