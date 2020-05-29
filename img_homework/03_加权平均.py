import cv2 as cv
import numpy as np
import 均衡化 as jh
src = cv.imread("01_实验测试图_汇总/03_03线性滤波/Fig3.35(a).bmp")
src = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
N = 7
t = N // 2
pMat = np.zeros((N,N))
for i in range(N):
    pMat[0,i] = 1         #领域平均
SMat = np.dot(pMat.T,pMat)
sum = SMat.sum()
n,m = src.shape
ret = np.zeros(src.shape)
dst = np.zeros(src.shape,src.dtype)
for i in range(n):
    for j in range(m):
        if j + N - 1 < m:
            for k in range(N):
                ret[i,j] += src[i,j + k] * pMat[0,k]
        else:
            ret[i,j] = src[i,j]
for i in range(n):
    for j in range(m):
        if i + N - 1 < n and j + t < m:
            for k in range(N):
                dst[i + t,j + t] += ret[i + k,j] * pMat[0,k] / sum
jh.custom_hist(dst)
cv.imshow("src",src)
cv.imshow("dst",dst)
cv.waitKey(0)
cv.destroyAllWindows()