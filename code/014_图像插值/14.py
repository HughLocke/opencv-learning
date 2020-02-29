import cv2 as cv
'''
缩放函数cv.resize 参数解释
InputArray src 	输入图片
OutputArray dst 	输出图片
Size 	输出图片尺寸,如果这个参数为0,则按照fx,fy缩放
fx, fy 	沿x轴，y轴的缩放系数,如果这个参数为0,则按照Size缩放
interpolation 	插入方式

插值方法
INTER_NEAREST 最近邻插值
INTER_LINEAR 双线性插值（默认设置）
INTER_AREA 使用像素区域关系进行重采样。
INTER_CUBIC 4x4像素邻域的双三次插值
INTER_LANCZOS4 8x8像素邻域的Lanczos插值
'''
src = cv.imread("./test.png")
cv.imshow("input",src)

h,w = src.shape[:2]
print(h,w)
dst = cv.resize(src,(w*2,h*2),interpolation=cv.INTER_NEAREST)
cv.imshow("INTER_NEAREST",dst)

dst = cv.resize(src,(w*2,h*2),interpolation=cv.INTER_LINEAR)
cv.imshow("INTER_LINERAR",dst)

dst = cv.resize(src,(w*2,h*2),interpolation=cv.INTER_CUBIC)
cv.imshow("INTER_CUBIC",dst)

dst = cv.resize(src,(w*2,h*2),interpolation=cv.INTER_LANCZOS4)
cv.imshow("INTER_LANCZOS4",dst)


cv.waitKey(0)
cv.destroyAllWindows()