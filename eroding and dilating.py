'''
eroding, dilating описать, смысл - избавиться от шума на изображенииза счет изменения размера областей
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
            dilatation_dst = cv2.dilate(frame,(21,21),iterations = 9)
            erode_dst = cv2.erode(frame, (21,21), iterations = 9)
            # Display the resulting frame
            cv2.imshow('Frame', frame)
            cv2.imshow('Dilate', dilatation_dst)
            cv2.imshow('Erode', erode_dst)

            
