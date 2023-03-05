import cv2
import numpy as np
import sys

img = np.full((400, 400, 3), 255, np.uint8)

# 선 그리기
# img : 그림을 그릴 영상
# (50, 50) : 선이 시작될 x/y좌표 의 튜플값
# (200, 150) : 선이 끝날 x/y좌표
# (0, 0, 255) : 선의 색깔
# 4 : 선의 두께
cv2.line(img, (50, 50), (200, 150), (0, 0, 255), 4)

# 네모 그리기
# (50, 200, 150, 100) : 사각형의 위치정보 (x, y, w, h) 의 튜플
# 2 : 두께, -1 을 입력할 경우 내부를 채운다.
cv2.rectangle(img, (50, 200, 150, 100), (0, 255, 0), 2)
cv2.rectangle(img, (70, 220, 180, 180), (255, 255, 0), -1)

# 원 그리기
# (300, 100) : 원의 중심의 좌표 (x, y) 의 튜플
# 30 : 원의 반지름
# (255, 255, 0) : 색상 또는 밝기, BGR 튜플
# -1 : 선의 두께, 내부를 채움
# cv2.LINE_AA : 선 타입, LINE_4 / LINE_8 / LINE_AA (AA 가 곡선에 유리함)
cv2.circle(img, (300, 100), 30, (255, 255, 0), -1, cv2.LINE_AA)

# 텍스트 입력
text = 'Hello, Python'
# (50, 350) : 영상에서 문자열을 출력할 위치의 *좌측 하단 좌표
# cv2.FONT_HERSHEY_COMPLEX : 폰트
# 0.8 : 폰트 크기의 확대/축소 비율
# 1 : 선의 두께
cv2.putText(img, text, (50, 350), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 1, cv2.LINE_AA)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()