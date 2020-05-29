import cv2 as cv
import numpy as np
from math import *
src = cv.imread("01_实验测试图_汇总/04_彩色图像/Fig6.35(1).bmp")
src = cv.cvtColor(src,cv.COLOR_BGR2RGB)
ret = np.zeros(src.shape,src.dtype)
PI = acos(-1.0)
n,m,ch = src.shape
cv.imshow("input",src)
for i in range(n):
    for j in range(m):
        R = src[i,j,0] / 255.0
        G = src[i,j,1] / 255.0
        B = src[i,j,2] / 255.0
        I = (R + G + B) / 3
        PI2 = 2 * acos(-1.0)
        if R == G and R == B:
            H = S = 0
        else:
            MIN = min(R, G, B)
            S = 1 - 3 * MIN / (R + G + B)
            son = ((R-G) + (R-B)) / 2
            mother = sqrt((R-G)*(R-G)+(R-B)*(G-B))
            st = acos(son/mother)
            if B <= G: H = st
            else: H = PI2 - st
        H = min(H + PI,PI2)
        H = int(H / PI2 * 255.0)
        S = int(S * 255.0)
        I = int(I * 255.0)
        ret[i,j] = [H,S,I]

for i in range(n):
    for j in range(m):
        H = ret[i,j,0] * PI2 / 255
        S = ret[i,j,1] / 255
        I = ret[i,j,2] / 255

        if(H <= PI2/3):
            R = I * (1 + S * cos(H) / cos(PI / 3 - H))
            B = I * (1 - S)
            G = 3 * I - (B + R)
        elif H <= PI2*2/3:
            R = I * (1 - S)
            G = I * (1 + S * cos(H - PI2 / 3) / cos(PI - H))
            B = 3 * I - R - G
        else:
            G = I * (1 - S)
            B = I * (1 + S * cos(H - 2*PI2/3)/cos(PI2*5/6-H))
            R = 3 * I - (G + B)
        R *= 255.0
        G *= 255.0
        B *= 255.0
        R = min(R,255); R = max(R,0)
        G = min(G,255); G = max(G,0)
        B = min(B,255); B = max(B,0)
        src[i,j] = [R,G,B]
cv.imshow("src",src)
cv.imshow("ret",ret)
cv.waitKey(0)
cv.destroyAllWindows()