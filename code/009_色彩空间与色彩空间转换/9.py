import cv2 as cv
#cvtColor实现色彩空间的转化,例如BGR空间转化为HSV空间
src = cv.imread("test.jpg")
cv.namedWindow("rgb",cv.WINDOW_NORMAL)
cv.imshow("rgb",src)

hsv = cv.cvtColor(src,cv.COLOR_BGR2HSV)
cv.namedWindow("hsv",cv.WINDOW_NORMAL)
cv.imshow("hsv",hsv)

yuv = cv.cvtColor(src,cv.COLOR_BGR2YUV)
cv.namedWindow("yuv",cv.WINDOW_NORMAL)
cv.imshow("yuv",yuv)

rgb = cv.cvtColor(src,cv.COLOR_BGR2RGB)
cv.namedWindow("rgb",cv.WINDOW_NORMAL)
cv.imshow("rgb",rgb)

ycrcb = cv.cvtColor(src,cv.COLOR_BGR2YCrCb)
cv.namedWindow("ycrcb",cv.WINDOW_NORMAL)
cv.imshow("ycrcb",ycrcb)

src2 = cv.imread("test.png")
cv.namedWindow("src2",cv.WINDOW_NORMAL)
hsv = cv.cvtColor(src2,cv.COLOR_BGR2HSV)
cv.imshow("src2",hsv)
cv.namedWindow("mask",cv.WINDOW_NORMAL)
#inrange筛选出hsv中上阈值和下阈值内的颜色
mask = cv.inRange(hsv,(35,43,46),(99,255,255))
cv.imshow("mask",mask)

cv.waitKey(0)
cv.destroyAllWindows()