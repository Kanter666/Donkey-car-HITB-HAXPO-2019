import cv2 as cv
import os
import glob
import matplotlib.pyplot as plt
import numpy as np



images = []
directory = "slow"
new_dir = directory+"_new2"

if not os.path.exists(new_dir):
    os.makedirs(new_dir)

for img in glob.glob("{}/*.jpg".format(directory)):
    n= cv.imread(img)
    crop = n[30:,:]
    '''
    plt.imshow(n, cmap='gray')
    plt.show()
    plt.imshow(crop, cmap='gray')
    plt.show()
    '''
    width, height = n.shape[:2]
    # edges = cv.Canny(n, width, height)
    lower_black = np.array([0,0,0], dtype = "uint16")
    upper_black = np.array([200,300,340], dtype = "uint16")
    black_mask = cv.inRange(crop, lower_black, upper_black)

    #plt.imshow(black_mask, cmap='gray')
    #plt.show()

    save = new_dir+img[len(directory):]
    # print(save)
    cv.imwrite(save, black_mask)
