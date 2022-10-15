import cv2 
import os 
import glob 
img_dir = "/home/roza/PycharmProjects/PoC_junior/imgs" # Enter Directory of all images  
data_path = os.path.join(img_dir,'*g') 
files = glob.glob(data_path) 
data = [] 
for f1 in files: 
    img = cv2.imread(f1) 
    data.append(img)