# import the modules
import os
from os import listdir
import glob
from matplotlib import pyplot as plt
import cv2
 
# obter o caminho/diretório00
folder_dir = "/home/roza/PycharmProjects/PoC_junior/imgs"
for images in os.listdir(folder_dir):
 
    # verifique se a imagem termina com png
    if (images.endswith(".png")):
        print(images)
    data_path = os.path.join(folder_dir, '*g')
    files = glob.glob(data_path)
    data = []
    for f1 in files:
        img = cv2.imread(f1)
        data.append(img)
        plt.figure()
        plt.imshow(img)