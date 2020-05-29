import cv2 as cv
import numpy as np

src = cv.imread("01_实验测试图_汇总/03_03线性滤波/Fig3.35(a).bmp")
src = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
N = 35
t = N // 2
fac = N * N
n,m = src.shape
ret = np.zeros(src.shape,src.dtype)
Max = 0
for i in range(n):
    for j in range(m):
        ret[i,j] = src[i,j]

for i in range(n//3,n//2):
    for j in range(m//6,m//3):
        if(i >= t and j >= t and i + t < n and j + t  < m):
            sum = 0.0
            for p in range(i - t,i + t + 1):
                for q in range(j - t,j + t + 1):
                    sum += src[p,q] / fac
            ret[i, j] = sum
        else:
            ret[i,j] = src[i,j]

cv.imshow("src",src)
cv.imshow("ret",ret)
cv.waitKey(0)
cv.destroyAllWindows()