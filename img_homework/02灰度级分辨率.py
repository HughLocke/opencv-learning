import cv2 as cv
import numpy as np

src = cv.imread("01_实验测试图_汇总/02灰度级分辨率/Fig2.21(a).bmp")
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
        v = vis[src[i,j,0]]
        src[i,j] = [v,v,v]
cv.imshow("output", src)
cv.waitKey(0)
cv.destroyAllWindows()