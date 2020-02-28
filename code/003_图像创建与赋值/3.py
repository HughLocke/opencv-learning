import cv2 as cv
import numpy as np

src = cv.imread("./test.png")
#cv.imshow("test1",src)

m1 = np.copy(src)

m2 = src
#取x轴0:200,y轴200:300的矩形全部变成RGB(255,255,255)白色
src[0:200,200:300,:] = 255
#cv.imshow("im2",m2)

#建立一个和原图一样大的矩阵,所有元素都是0,因此是全黑矩阵
m3 = np.zeros(src.shape,src.dtype)
#cv.imshow("m3",m3)

#建立一个[512,512]长宽的全0矩阵
m4 = np.zeros([512,512],np.uint8)
m4[:,:] = 127 #全部变为127
#cv.imshow("m4",m4)

#创建一个长宽512,所有像素点都是(255,0,0)的图像
m5 = np.ones(shape = [512,512,3],dtype = np.uint8)
m5[:,:,0] = 255
cv.imshow("m5",m5)

cv.waitKey(0)
cv.destroyAllWindows()
