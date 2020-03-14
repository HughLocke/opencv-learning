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

def solve(gray):
    h,w = gray.shape
    hist = np.zeros([256], dtype=np.int32)
    for row in range(h):
        for col in range(w):
            pv = gray[row, col]
            hist[pv] += 1
    sum = h * w
    t = []
    t.append(hist[0]/sum)
    ret = []
    for i in range(1,256):
        t.append(hist[i]/sum + t[i - 1])
    for i in range(256):
        ret.append(int(t[i]*255+0.5))
    for i in range(h):
        for j in range(w):
            gray[i, j] = ret[gray[i, j]]
    return gray

src = cv.imread("./01_实验测试图_汇总/03_02直方图均衡化/Fig3.10(b).bmp")
gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
cv.imshow("eh",gray)

custom_hist(gray)
for i in range(100):
    gray = solve(gray)

cv.imshow("ans",gray)
custom_hist(gray)

cv.waitKey(0)
cv.destroyAllWindows()