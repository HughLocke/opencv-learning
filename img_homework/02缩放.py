import cv2 as cv
import numpy as np

src = cv.imread("01_实验测试图_汇总/01_02_256彩色/j10.bmp")
n,m,ch = np.shape(src)
cv.imshow("src",src)

#放大两倍
src2 = np.zeros([n * 2,m * 2,ch],src.dtype)
for i in range(int(2*n)):
    for j in range(int(2*m)):
        src2[i,j] = src[int(i/2),int(j/2)]
#cv.imshow("src2",src2)

#缩小两倍
src05 = np.zeros([int(n / 2),int(m / 2),ch],src.dtype)
for i in range(int(n/2)):
    for j in range(int(m/2)):
        src05[i,j] = src[int(i*2),int(j*2)]
#cv.imshow("src05",src05)

#双线性插值算法放大num倍
num = 2
src5 = np.zeros([n * num,m * num,ch],src.dtype)
print(src5.shape)
for i in range(int(num*n)):
    for j in range(int(num*m)):
        x,y = i/num,j/num
        x1,x2 = min(int(x),n - 1),min(int(x) + 1,n - 1)
        y1,y2 = min(int(y),m - 1),min(int(y) + 1,m - 1)
        up1 = (x - x1) * src[x1,y1] + (x2 - x) * src[x2,y1]
        up2 = (x - x1) * src[x1,y2] + (x2 - x) * src[x2,y2]
        src5[i,j] = (y - y1) * up1 + (y2 - y) * up2
cv.imshow("src5",src5)
cv.waitKey(0)
cv.destroyAllWindows()