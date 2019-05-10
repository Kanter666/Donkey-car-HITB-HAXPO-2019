import cv2 as cv
import os
import glob
import matplotlib.pyplot as plt


images = []
directory = "slow"
new_dir = directory+"_edge"

if not os.path.exists(new_dir):
    os.makedirs(new_dir)

for img in glob.glob("{}/*.jpg".format(directory)):
    n= cv.imread(img)
    width, height = n.shape[:2]
    edges = cv.Canny(n, width, height)
    # plt.imshow(edges, cmap='gray')
    # plt.show()
    save = new_dir+img[len(directory):]
    # print(save)
    cv.imwrite(save, edges)
