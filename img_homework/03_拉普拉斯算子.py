import cv2 as cv
import numpy as np
src = cv.imread("01_实验测试图_汇总/03_03线性滤波/Fig3.35(a).bmp")
ret = np.zeros(src.shape,src.dtype)
n,m,ch = src.shape
cv.imshow("input",src)
for i in range(1,n - 1):
    for j in range(1,m - 1):
        sum = [0,0,0]
        for p in range(-1,2):
            for q in range(-1,2):
                sum -= src[i + p,j + q]
        sum += src[i,j] * [9,9,9]
        if(sum[0] < 0): sum = -sum
        ret[i,j] = sum
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
                    a.append(src[p,q,0])
            a.sort()
            ret[i,j] = [a[fac],a[fac],a[fac]]
        else:
            ret[i,j] = src[i,j]
        if(ret[i,j,0] > 50): ret[i,j] = [0,0,255]

cv.imshow("src",src)
cv.imshow("ret",ret)
cv.waitKey(0)
cv.destroyAllWindows()