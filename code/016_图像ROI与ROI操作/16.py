import cv2 as cv
import numpy as np

src = cv.imread("./test.png")
#cv.imshow("input",src)
h,w = src.shape[:2]

#选取ROI,中心100 * 100的图像
cy = h // 2
cx = w // 2
roi = src[cy-100:cy+100,cx-100:cx+100,:]
#cv.imshow("roi",roi)

image = np.copy(roi)

#把图片的红色通道变为0
image[:,:,2] = 0
#cv.imshow("result",src)
#cv.imshow("copy roi",image)

src2 = cv.imread("./test.png")
cv.imshow("src2",src2)
hsv = cv.cvtColor(src2,cv.COLOR_BGR2HSV)
#取给定阈值范围内的图像
mask = cv.inRange(hsv, (35, 43, 46), (99, 255, 255))

#cv.imshow("mask",mask)
#提取除了给定阈值范围内的图像
mask = cv.bitwise_not(mask)
person = cv.bitwise_and(src2,src2,mask = mask)
cv.imshow("person",person)
result = np.zeros(src2.shape,src2.dtype)
result[:,:,0] = 255
cv.imshow("person",result)

mask = cv.bitwise_not(mask)
dst = cv.bitwise_or(person,result,mask = mask)
dst = cv.add(dst,person)

cv.imshow("dst",dst)
cv.waitKey(0)
cv.destroyAllWindows()