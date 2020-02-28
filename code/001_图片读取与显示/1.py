import cv2

src = cv2.imread("test.jpg")
cv2.imshow("test.jpg",src)
cv2.waitKey(5000)
cv2.destroyAllWindows()

