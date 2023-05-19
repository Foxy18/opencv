'''
blur, gayssianblur,medianblur,Bilateral Filtering дописать последние
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
            blu = cv2.blur(frame, (21,21)) 
            # Display the resulting frame
            cv2.imshow('Frame', frame)
            cv2.imshow('Blur', blu)
            
