import cv2

'''
Получение изображения:
1. Из файла:
1.1. Изображение
1.2. Видео
2. По сети: с помощью VLC можно создать сетевой видео-поток 
2.1. RSTP
2.2. UDP
2.3. TCP
3. Веб-камера(видео-поток от физического устройства)
'''

img = cv2.imread(r"dog.jpg")
if img is None:
    print("Картинка не найдена")
else: 
    cv2.imshow("display window", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

cap = cv2.VideoCapture('selfeat.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")

else:
    while cv2.waitKey(1) != ord('q'):
            # Capture frame-by-frame
        ret, frame = cap.read()
            # if frame is read correctly ret is True
        if ret:
                # Display the resulting frame
            cv2.imshow('frame', frame)
    