import cv2
from pyzbar.pyzbar import decode, ZBarSymbol

# Image.open('barcode1.png')  # if use PIL library
im = cv2.imread(
    "/home/roza/PycharmProjects/PoC_junior/imgs/bar15.jpeg")  # if use cv2

# codes = decode(im, symbols=[ZBarSymbol.QRCODE])  # specify code type
codes = decode(im)  # auto detect code type
print('Decoded:', codes)

for code in codes:
    data = code.data.decode('ascii')
    print('Data:', code.data.decode('ascii'))
    print('Code Type:', code.type)
    print('BBox:', code.rect)
    x, y, w, h = code.rect.left, code.rect.top, \
        code.rect.width, code.rect.height
    cv2.rectangle(im, (x, y), (x+w, y+h), (255, 0, 0), 8)
    print('Polygon:', code.polygon)
    cv2.rectangle(im, code.polygon[0], code.polygon[1],
                  (0, 255, 0), 4)

    txt = '(' + code.type + ')  ' + data
    cv2.putText(im, txt, (x - 10, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 50, 255), 2)

text1 = 'No. Codes: %s' % len(codes)
cv2.putText(im, text1, (5, 15),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

cv2.imshow('bounding box', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
