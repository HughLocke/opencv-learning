import cv2 as cv
import numpy as np

src = cv.imread("01_实验测试图_汇总/01_02_256彩色/j10.bmp")
cv.imshow("input",src)
num = int(input("请输入要分的级数:"))
while num < 2 or num > 8:
    num = int(input("输入范围错误,请重新输入"))
num = 2 ** num
vis = []
for i in range(int(256 / num)):
    for j in range(num):
        vis.append(i * num)
n,m,ch = np.shape(src)
for i in range(n):
    for j in range(m):
        for k in range(ch):
            src[i,j,k] = vis[src[i,j,k]]
cv.imshow("output", src)
cv.waitKey(0)
cv.destroyAllWindows()