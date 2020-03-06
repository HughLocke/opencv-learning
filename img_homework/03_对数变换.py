import cv2 as cv
import numpy as np
import math
import PaintLine as PL

src = cv.imread("01_实验测试图_汇总/03_01灰度映射/对数变换/Fig3.05(a).bmp")
cv.imshow("src",src)
n,m,ch = np.shape(src)
rule = []
fac = 100
for i in range(256):
    rule.append(fac * math.log(i + 1))
Max = 0
for i in range(n):
    for j in range(m):
        src[i,j,:] = rule[src[i,j,0]]
        Max = max(Max,src[i,j,0])
cha = 255.0 / Max
for i in range(n):
    for j in range(m):
        src[i,j,:] = cha * src[i,j,0]

cv.imshow("output",src)
PL.paint(rule)

cv.waitKey(0)
cv.destroyAllWindows()