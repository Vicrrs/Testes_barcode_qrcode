import cv2
from pyzbar.pyzbar import decode
import time

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
used_codes = []

camera = True
while camera == True:
    success, frame = cap.read()

    for code in decode(frame):
        if code.date.decode('utf-8') not in used_codes:
            print("Aprovado. Pode entrar!")
            print(code.date.decode('utf-8'))
            used_codes.append(code.date.decode('utf-8'))
            time.sleep(5)
        elif code.data.decode('utf-8') in used_codes:
            print("Desculpe, este código já foi usado!")
            time.sleep(5)
        else:
            break
    cv2.imshow("Testando", frame)
    cv2.waitKey(1)
