import cv2

src = cv2.imread('../Day5/cat.bmp', cv2.IMREAD_COLOR)
betman = cv2.imread('betman.png', cv2.IMREAD_UNCHANGED) # png 값을 가져오기 위한 타입

if src is None or betman is None :
    print('error')
    sys.exit()

mask = betman[:, :, 3]
betman = betman[:, :, :-1] # betman 은 alpha 채널을 갖기 때문에 4채널, 따라서 b, g, r 3채널로 변경해준다.
h, w = mask.shape[:2]
crop = src[30:30+h, 30:30+w] # betman, mask 와 같은 크기의 부분 영상을 추출한다. > 영상이 입력될 위치

cv2.copyTo(betman, mask, crop)

cv2.imshow('betman', betman)
cv2.imshow('src', src)
cv2.imshow('mask', mask)
cv2.waitKey()
cv2.destroyAllWindows()