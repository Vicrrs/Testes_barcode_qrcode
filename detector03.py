import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import glob
import os


folder_dir = "/home/roza/PycharmProjects/PoC_junior/imgs"

def process(filename: str=None) -> None:

    data_path = os.path.join(folder_dir, '*g')
    image = mpimg.imread(folder_dir)
    images = glob.glob(data_path)
    plt.figure()
    plt.imshow(image)

    for file in images:
        process(file)

process()