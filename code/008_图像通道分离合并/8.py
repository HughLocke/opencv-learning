import cv2 as cv

src = cv.imread("./test.png")
cv.imshow("input",src)

#将所有像素点的蓝色rgb值设为0
mv = cv.split(src)
mv[0][:,:] = 0
dst1 = cv.merge(mv)
cv.imshow("output1",dst1)

mv = cv.split(src)
mv[1][:,:] = 0
dst2 = cv.merge(mv)
cv.imshow("output2",dst2)

mv = cv.split(src)
mv[2][:,:] = 0
dst3 = cv.merge(mv)
cv.imshow("output3",dst3)

cv.waitKey(0)
cv.destroyAllWindows()
