'''
сделала callback функции на ползунки
маску объекта для его поиска в цветовом пространстве bgr
защиту
'''
b_min, g_min, r_min = 0, 0, 0
b_max, g_max, r_max = 255, 255, 255

def b_min_change(arg):
    global b_min, b_max
    if arg < b_max:
        b_min = arg


def g_min_change(arg):
    global g_min, g_max
    if arg < g_max:
        g_min = arg


def r_min_change(arg):
    global r_min, r_max
    if arg < r_max:
        r_min = arg


def b_max_change(arg):
    global b_min, b_max
    if arg > b_min:
        b_max = arg


def g_max_change(arg):
    global g_min, g_max
    if arg > g_min:
        g_max = arg


def r_max_change(arg):
    global r_min, r_max
    if arg > r_min:
        r_max = arg


import cv2

cv2.namedWindow("setup")
cv2.createTrackbar("b1", "setup", 0, 255, b_min_change)
cv2.createTrackbar("g1", "setup", 0, 255, g_min_change)
cv2.createTrackbar("r1", "setup", 0, 255, r_min_change)
cv2.createTrackbar("b2", "setup", 255, 255, b_max_change)
cv2.createTrackbar("g2", "setup", 255, 255, g_max_change)
cv2.createTrackbar("r2", "setup", 255, 255, r_max_change)
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
            min_p = (b_min, g_min, r_min)
            max_p = (b_max, g_max, r_max)
            mask = cv2.inRange(frame, min_p, max_p)
            # Display the resulting frame
            cv2.imshow('Img', mask)
            cv2.imshow('Frame', frame)
            
