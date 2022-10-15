# import necessary packages
import cv2
import os
import glob
import matplotlib.pyplot as plt

# Set the path where images are stored
# Enter Directory of all images
img_dir = "/home/roza/PycharmProjects/PoC_junior/imgs"
data_path = os.path.join(img_dir, '*g')
files = glob.glob(data_path)
data = []
for f1 in files:
    img = cv2.imread(f1)
    data.append(img)
    plt.figure()
    plt.imshow(img)
