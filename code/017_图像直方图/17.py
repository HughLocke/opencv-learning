import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def custom_hist(gray):
    h,w = gray.shape
    #手动计算hist
    hist = np.zeros([256],dtype=np.int32)

    for row in range(h):
        for col in range(w):
            pv = gray[row,col]
            hist[pv] += 1
    #y_pos初始化为从0-255的所有整数的数组
    y_pos = np.arange(0,256,1,dtype = np.int32)

    plt.bar(y_pos,hist,align='center',color='r',alpha=0.5)
    plt.xticks(y_pos,y_pos)
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.show()
'''
cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]]) ->hist
imaes: 输入的图像
channels: 选择图像的通道
mask: 掩膜，是一个大小和image一样的np数组，其中把需要处理的部分指定为1，不需要处理的部分指定为0，一般设置为None，表示处理整幅图像
histSize: 使用多少个bin(柱子)，一般为256
ranges: 像素值的范围，一般为[0, 255],表示0~255
'''
def image_hist(image):
    cv.imshow("input",image)
    color = ('blue','green','red')
    #enumerate 列出列表的索引及元素,即第一组i = 0,color = 'blue'
    for i,color in enumerate(color):
        #hist对应i通道上每个像素值对应的像素个数
        hist = cv.calcHist([image],[i],None,[256],[0,256])
        plt.plot(hist,color=color)
        #plt.xlim:x轴的最小值和最大值
        plt.xlim([0,256])
    plt.show()

src = cv.imread("./test.png")
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
#cv.imshow("input",gray)

#画原图直方图
image_hist(src)
custom_hist(gray)

cv.waitKey(0)
cv.destroyAllWindows()