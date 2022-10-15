import cv2

detector = cv2.QRCodeDetector()

reval, points, s_qr = detector.detectAndDecode(cv2.imread('/home/roza/PycharmProjects/PoC_junior/imgs/qr00006.png'))
print(reval)

print("Pontos")
print(points)
