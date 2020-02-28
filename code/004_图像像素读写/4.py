import cv2 as cv

src = cv.imread("./test.png")
cv.imshow("m1",src)
h,w,ch = src.shape
print("h,w,ch:",h,w,ch)
#将图像取反
for row in range(h):
    for col in range(w):
        b,g,r = src[row,col]
        b = 255 - b
        g = 255 - g
        r = 255 - r
        src[row,col] = [b,g,r]
cv.imshow("output",src)

cv.waitKey(0)
cv.destroyAllWindows()