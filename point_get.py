'''
сделала callback функции на ползунки
маску объекта для его поиска в цветовом пространстве bgr
защиту
cтолбец строка у х
'''
h_min, s_min, v_min = 0, 0, 0
h_max, s_max, v_max = 255, 255, 255

def h_min_change(arg):
    global h_min, h_max
    if arg < h_max:
        h_min = arg


def s_min_change(arg):
    global s_min, s_max
    if arg < s_max:
        s_min = arg


def v_min_change(arg):
    global r_min, r_max
    if arg < v_max:
        v_min = arg


def h_max_change(arg):
    global h_min, h_max
    if arg > h_min:
        h_max = arg


def s_max_change(arg):
    global s_min, s_max
    if arg > s_min:
        s_max = arg


def v_max_change(arg):
    global v_min, v_max
    if arg > v_min:
        v_max = arg


import cv2

cv2.namedWindow("setup")
cv2.createTrackbar("h1", "setup", 0, 180, h_min_change)
cv2.createTrackbar("s1", "setup", 0, 255, s_min_change)
cv2.createTrackbar("v1", "setup", 0, 255, v_min_change)
cv2.createTrackbar("h2", "setup", 180, 180, h_max_change)
cv2.createTrackbar("s2", "setup", 255, 255, s_max_change)
cv2.createTrackbar("v2", "setup", 255, 255, v_max_change)
# Видео с камеры
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
else:
    while cv2.waitKey(1) != 27:  # escape
        # Capture frame-by-frame
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if ret:
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            min_p = (h_min, s_min, v_min)
            max_p = (h_max, s_max, v_max)    
            mask = cv2.inRange(hsv, min_p, max_p)
            frame_copy = frame.copy()
            cv2.circle(frame_copy, (320, 240), 6, (255, 0, 0), -1)
            print(hsv[240,320])
            # Display the resulting frame
            cv2.imshow('Img', mask)
            cv2.imshow('Frame_copy', frame_copy)
            
