'''
contours дописать area, min/max, иеарархия
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
            frame_copy = frame.copy()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            _, thresh = cv2.threshold(gray, 127, 255, 0)
            contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            cv2.drawContours(frame_copy, contours, -1, (255,0,0), 3)
            # Display the resulting frame
            cv2.imshow('Frame', frame)
            cv2.imshow('Img', frame_copy)
            

            
