import cv2 as cv

#彩色映射
src = cv.imread("test1.png")
cv.imshow("input",src)
dst = cv.applyColorMap(src,cv.COLORMAP_COOL)
cv.imshow("output",dst)

#伪色彩
image = cv.imread("test0.jpg")
color_image = cv.applyColorMap(image,cv.COLORMAP_JET)
cv.imshow("image",image)
cv.imshow("color_image",color_image)

cv.waitKey(0)
cv.destroyAllWindows()