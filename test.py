import cv2

import extractor_qr as reader

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    codes, frame = reader.extract(frame, True)
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('Sai')
        break

# When everything done, release the capture
cap.release()