# import the modules
import os
from os import listdir
import glob
from matplotlib import pyplot as plt
from pathlib import Path
import cv2

detector = cv2.QRCodeDetector()
# obter o caminho/diretório00
folder_dir = Path("/home/roza/PycharmProjects/PoC_junior/imgs")
for images in os.listdir(folder_dir):

    # verifique se a imagem termina com png
    if (images.endswith(".jpg")):
        print(images)
    data_path = os.path.join(folder_dir, '*g')
    files = glob.glob(data_path)
    data = []
    for f1 in files:
        reval, points, s_qr = detector.detectAndDecode(cv2.imread(f1))
        img = cv2.imread(f1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print('Sai')
            break
        data.append(reval)
        plt.figure()
        plt.imshow(img)
        plt.show()
        print("Pontos: \n", points)
