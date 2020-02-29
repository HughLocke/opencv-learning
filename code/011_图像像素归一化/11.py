import cv2 as cv
import numpy as np
'''
归一化函数normalize 参数说明
src               输入数组；
dst               输出数组，数组的大小和原数组一致；
alpha           1,用来规范值，2.规范范围，并且是下限；
beta             只用来规范范围并且是上限；
norm_type   归一化选择的数学公式类型；
dtype           当为负，输出在大小深度通道数都等于输入，当为正，输出只在深度与输如不同，不同的地方游dtype决定；
mark            掩码。选择感兴趣区域，选定后只能对该区域进行操作。
'''

src = cv.imread("./test.png")
cv.namedWindow("input",cv.WINDOW_AUTOSIZE)
cv.imshow("input",src)
gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
#转化为浮点数矩阵
cv.imshow("gray",gray)
gray = np.float32(gray)
print(gray)
#将gray按照MINMAX的公式归一化为上限1.0,下限0.0的矩阵,输出在dst
dst = np.zeros(gray.shape,dtype = np.float32)
cv.normalize(gray,dst=dst,alpha=1.0,beta=0,norm_type=cv.NORM_MINMAX)
print(dst)
cv.imshow("NORM_MINMAX",np.uint8(dst*255))
#NORM_L1
dst = np.zeros(gray.shape,dtype = np.float32)
cv.normalize(gray,dst=dst,alpha=1.0,beta=0,norm_type=cv.NORM_L1)
print(dst)
cv.imshow("NORM_L1",np.uint8(dst*10000000))
#NORM_L2
dst = np.zeros(gray.shape,dtype = np.float32)
cv.normalize(gray,dst=dst,alpha=1.0,beta=0,norm_type=cv.NORM_L2)
print(dst)
cv.imshow("NORM_L2",np.uint8(dst*10000))



cv.waitKey(0)
cv.destroyAllWindows()