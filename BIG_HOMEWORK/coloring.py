import cv2 as cv
import numpy as np
import random
import sys
import normal
import normalwb
import findjn
#灰度图的二值化
def twoclassify(src):
    n,m = src.shape
    arg = (int(src.max()) + int(src.min())) / 2
    for i in range(n):
        for j in range(m):
            if src[i,j] > 150: src[i,j] = 255
            else: src[i,j] = 0
    return src

def colorjn(src):
    def findshell(src):
        n,m,ch = src.shape
        CclK = [30, 60, 60, 120, 180, 220]
        EclK = [80,200,200,255,200,255]
        BclK = [180,250,180,240,140,185]
        Ac = [255,0,0]
        Bc = [0,255,0]
        Cc = [0,0,255]
        for i in range(n):
            for j in range(m):
                if (src[i, j, 0] > BclK[0] and src[i, j, 0] < BclK[1] and
                        src[i, j, 1] > BclK[2] and src[i, j, 1] < BclK[3] and
                        src[i, j, 2] > BclK[4] and src[i, j, 2] < BclK[5]):
                    src[i, j] = Ac
                if (src[i, j, 0] > CclK[0] and src[i, j, 0] < CclK[1] and
                        src[i, j, 1] > CclK[2] and src[i, j, 1] < CclK[3] and
                        src[i, j, 2] > CclK[4] and src[i, j, 2] < CclK[5]):
                    src[i,j] = Bc
                if (src[i, j, 0] > EclK[0] and src[i, j, 0] < EclK[1] and
                        src[i, j, 1] > EclK[2] and src[i, j, 1] < EclK[3] and
                        src[i, j, 2] > EclK[4] and src[i, j, 2] < EclK[5]):
                    src[i, j] = Cc
        B = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        src = normal.kai(src,Ac, B)
        src = normal.pengzhang(src,Ac, B)
        src = normal.kai(src,Bc, B)
        src = normal.pengzhang(src,Bc, B)
        src = normal.kai(src,Cc, B)
        src = normal.pengzhang(src,Cc, B)

        return src
    src = findshell(src)
    return src

def classifyjn(src,threshold):
    s = src.copy()
    s = colorjn(s)
    src = findjn.findjn(s,src,threshold)
    return src

def main():
    for i in range(1):
        s = cv.imread(f"img/jn{i + 1}.jpg")
        s = classifyjn(s)
        cv.imshow(f"src{i + 1}", s)
        #cv.imwrite(f"img/jn_1_{i + 1}.jpg", s,[int(cv.IMWRITE_JPEG_QUALITY),100])
    cv.waitKey(0)
    cv.destroyAllWindows()
if __name__ == '__main__':
    main()