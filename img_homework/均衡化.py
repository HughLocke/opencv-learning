import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
matplotlib.rc("font", family="AR PL UKai CN")
def custom_hist(gray):
    h, w = gray.shape
    hist = np.zeros([256], dtype=np.int32)
    for row in range(h):
        for col in range(w):
            pv = gray[row, col]
            hist[pv] += 1
    y_pos = np.arange(0,256,1,dtype = np.int32)
    plt.bar(y_pos,hist,align='center',color = 'r')
    plt.xticks(y_pos,y_pos)
    plt.ylabel('Grequency')
    plt.title('His')
    plt.show()