import cv2

src = cv2.imread("test.jpg")
cv2.namedWindow("test.jpg",cv2.WINDOW_NORMAL)
cv2.imshow("test.jpg",src)
cv2.waitKey(0)
cv2.destroyAllWindows()

