import cv2 as cv
import numpy as np
import PaintLine as PL

src = cv.imread("01_实验测试图_汇总/03_01灰度映射/灰度求反/Fig3.04(a).bmp")
cv.imshow("src",src)
n,m,ch = np.shape(src)
rule = []
for i in range(256):
    rule.append(255 - i)

for i in range(n):
    for j in range(m):
        src[i,j,:] = rule[src[i,j,0]]

cv.imshow("output",src)
PL.paint(rule)

cv.waitKey(0)
cv.destroyAllWindows()