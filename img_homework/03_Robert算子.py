import cv2 as cv
import numpy as np
from math import sqrt
src = cv.imread("01_实验测试图_汇总/03_03线性滤波/Fig3.35(a).bmp")
src = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
cv.imshow("src",src)
ret = np.zeros(src.shape,src.dtype)
n,m = src.shape
for i in range(n - 1):
    for j in range(m - 1):
        #sum = sqrt((src[i + 1,j + 1] - src[i,j])*(src[i + 1,j + 1] - src[i,j]) + (src[i + 1,j] - src[i,j + 1]) * (src[i + 1,j] - src[i,j + 1]))
       # print(sum)
        sum = abs(int(src[i + 1,j + 1]) - src[i,j]) + abs(int(src[i + 1,j]) - src[i,j + 1])
        ret[i,j] = sum
'''
src = ret.copy()
ret = np.zeros(src.shape,src.dtype)

N = 3
t = N // 2
fac = N * N // 2
for i in range(n):
    for j in range(m):
        if i >= t and i + t < n and j >= t and j + t < m:
            a = []
            for p in range(i - t,i + t + 1):
                for q in range(j - t,j + t + 1):
                    a.append(src[p,q])
            a.sort()
            ret[i,j] = a[fac]
        else:
            ret[i,j] = src[i,j]
'''
cv.imshow("ret",ret)
cv.waitKey(0)
cv.destroyAllWindows()