import cv2 as cv
import numpy as np

#读入灰度图
src = cv.imread("./test.png",cv.IMREAD_GRAYSCALE)
cv.namedWindow("input",cv.WINDOW_NORMAL)
cv.imshow("input",src)

#查找最深点的像素和最浅点的像素并找出他们的位置
min,max,minLoc,maxLoc = cv.minMaxLoc(src)
print(min,max,minLoc,maxLoc)

#计算均值和标准差
means,stddev = cv.meanStdDev(src)
print(means,stddev)

#将大于均值的变为白色,小于均值的变为黑色
src[np.where(src < means)] = 0
src[np.where(src > means)] = 255
cv.imshow("binary",src)


cv.waitKey(0)
cv.destroyAllWindows()