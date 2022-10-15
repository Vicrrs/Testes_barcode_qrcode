import cv2

detector = cv2.QRCodeDetector()

reval, points, s_qr = detector.detectAndDecode(cv2.imread('arquivo02.png'))
print(reval)

print("Pontos")
print(points)
