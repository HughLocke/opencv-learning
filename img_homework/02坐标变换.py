import cv2 as cv
import numpy as np

src = cv.imread("01_实验测试图_汇总/01_02_256彩色/j10.bmp")
n,m,ch = np.shape(src)
cv.imshow("src",src)
a = 1
print(f"{a}")
#垂直镜像
srcx = np.zeros(src.shape,src.dtype)
for i in range(n):
    srcx[i] = src[n - i - 1]
cv.imshow("srcx",srcx)

srcy = np.zeros(src.shape,src.dtype)
for i in range(m):
    srcy[:,i,:] = src[:,m - i - 1,:]
cv.imshow("srcy",srcy)

srcxy = np.zeros([m,n,ch],src.dtype)
for i in range(n):
    for j in range(m):
        srcxy[j,i] = src[i,j]
cv.imshow("srcxy",srcxy)

cv.waitKey(0)
cv.destroyAllWindows()