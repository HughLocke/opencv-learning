import cv2
#彩色转灰度图
src = cv2.imread("./test.png")
cv2.imshow("test2",src)
gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray.png',gray)
cv2.imshow("gray",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
