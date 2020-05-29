import cv2 as cv
import numpy as np
import 均衡化 as jh
src = cv.imread("01_实验测试图_汇总/03_03线性滤波/Fig3.35(a).bmp")
src = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
ret = np.zeros(src.shape,src.dtype)
N = 3
t = N // 2
fac = N * N
n,m = src.shape
for i in range(n):
    for j in range(m):
        if i >= t and i + t < n and j >= t and j + t < m:
            a = []
            for p in range(i - t,i + t + 1):
                for q in range(j - t,j + t + 1):
                    a.append(src[p,q])
            a.sort()
            ret[i,j] = a[t + 1]
        else:
            ret[i,j] = src[i,j]
jh.custom_hist(src)
cv.imshow("src",src)
cv.imshow("ret",ret)
cv.waitKey(0)
cv.destroyAllWindows()