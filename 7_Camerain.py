import sys

import cv2

cap = cv2.VideoCapture(0) # 카메라의 index 번호(첫 번째로 설치된 카메라)

if not cap.isOpened() : 
    print('카메라를 열 수 없습니다.')
    sys.exit()

print('가로 사이즈 : ', int(cap.get(cv2.CAP_PROT_FRAME_WIDTH)))
print('세로 사이즈 : ', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

while True : 
    # ret : read() 의 결과값, 성공할 경우 True, 실패할 경우 False
    # fraame : 현재 영상의 프레임, numpy.ndarray 의 형태
    ret, frame = cap.read()
    
    if not ret : 
        break
    
    inversed = ~frame # 프레임을 반전(색정보)
    
    cv2.imshow('프레임', frame)
    cv2.imshow('inversed', inversed)

    if cv2.waitKey(10) == 27 : # ESC 키
        break

cap.release()
cv2.destroyAllWindows()