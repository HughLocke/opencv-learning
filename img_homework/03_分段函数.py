import cv2 as cv
import numpy as np
import math
import PaintLine as PL

src = cv.imread("01_实验测试图_汇总/03_01灰度映射/分段变换/Fig3.10(b).bmp")
cv.imshow("src",src)
n,m,ch = np.shape(src)
rule = []
X1,Y1 = 100,10
X2,Y2 = 150,200

for i in range(0,X1):
    rule.append(i * Y1 / X1)
for i in range(X1,X2):
    rule.append(Y1 + (i-X1) * (Y2 - Y1) / (X2 - X1))
for i in range(X2,256):
    rule.append(Y2 + (i-X2) * (255 - Y2) / (255 - X2))
Max = 0
for i in range(n):
    for j in range(m):
        src[i,j,:] = rule[src[i,j,0]]
        Max = max(Max,src[i,j,0])
'''
cha = 255.0 / Max
for i in range(n):
    for j in range(m):
        src[i,j,:] = cha * src[i,j,0]
'''
cv.imshow("output",src)
PL.paint(rule)

cv.waitKey(0)
cv.destroyAllWindows()