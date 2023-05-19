'''
BGR
Gray:
cvtColor()
HSV:
cvtColor()
'''
import cv2
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
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            # Display the resulting frame
            cv2.imshow('Frame', frame)
            cv2.imshow('Gray', gray)
            cv2.imshow('HSV', hsv)
