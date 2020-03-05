import cv2 as cv
import numpy as np

src1 = cv.imread("./test.png")
src2 = cv.imread("./Mat.png")
src3 = cv.imread("./test.png")
src4 = cv.imread("./test.png")

hsv1 = cv.cvtColor(src1,cv.COLOR_BGR2HSV)
hsv2 = cv.cvtColor(src2,cv.COLOR_BGR2HSV)
hsv3 = cv.cvtColor(src3,cv.COLOR_BGR2HSV)
hsv4 = cv.cvtColor(src4,cv.COLOR_BGR2HSV)

hist1 = cv.calcHist([hsv1],[0,1],None,[60,64],[0,180,0,256])
hist2 = cv.calcHist([hsv2],[0,1],None,[60,64],[0,180,0,256])
hist3 = cv.calcHist([hsv3],[0,1],None,[60,64],[0,180,0,256])
hist4 = cv.calcHist([hsv4],[0,1],None,[60,64],[0,180,0,256])

cv.normalize(hist1,hist1,0,1.0,cv.NORM_MINMAX)
cv.normalize(hist2,hist2,0,1.0,cv.NORM_MINMAX)
cv.normalize(hist3,hist3,0,1.0,cv.NORM_MINMAX)
cv.normalize(hist4,hist4,0,1.0,cv.NORM_MINMAX)

#CORREL 相关性比较,值越大,相关性越高,范围[0,1]
#CHISQR 卡方比较,值越小,相关度越高,范围[0,+oo)
#INTERSECT 交集法,数值越大表示越像
#BHATTACHARYYA 巴氏距离比较,值越小,相关度越高,范围[0,1]
methods = [cv.HISTCMP_CORREL,cv.HISTCMP_CHISQR,
          cv.HISTCMP_INTERSECT,cv.HISTCMP_BHATTACHARYYA]
str_method = ""
#结果表明src1和src2比较像,src3和src4完全一致
for method in methods:
    src1_src2 = cv.compareHist(hist1,hist2,method)
    src3_src4 = cv.compareHist(hist3,hist4,method)
    if method == cv.HISTCMP_CORREL:
        str_method = "Correlation"
    if method == cv.HISTCMP_CHISQR:
        str_method = "Chi-square"
    if method == cv.HISTCMP_INTERSECT:
        str_method = "Intersection"
    if method == cv.HISTCMP_BHATTACHARYYA:
        str_method = "Bhattacharyya"

    print("%s src1_src2 = %.2f, src3_src4 = %.2f"%(str_method, src1_src2, src3_src4))

cv.waitKey(0)
cv.destroyAllWindows()