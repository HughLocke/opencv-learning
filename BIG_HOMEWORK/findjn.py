import cv2 as cv
import numpy as np
import random
import sys
import normal
import normalwb
#求出每个颜色的二维前缀和
def PreSum(src):
    ps = np.zeros(src.shape, dtype = int)
    n,m,ch = src.shape
    for i in range(n):
        for j in range(m):
            if src[i,j].sum() < 260 and src[i,j,0] > 250:
                ps[i,j,0] = 1
            if src[i,j].sum() < 260 and src[i,j,1] > 250:
                ps[i,j,1] = 2
            if src[i,j].sum() < 260 and src[i,j,2] > 250:
                ps[i,j,2] = 2
            if i > 0:
                ps[i,j] += ps[i - 1,j]
            if j > 0:
                ps[i,j] += ps[i,j - 1]
            if i > 0 and j > 0:
                ps[i,j] -= ps[i - 1,j - 1]
    return ps

def check(x,y,h,w,n,m,presum,threshold):
    x = int(x);y = int(y);h = int(h);w = int(w)
    Sum = presum[x + h - 1,y + w - 1].sum()
    if x > 0:
        Sum -= presum[x - 1,y + w - 1].sum()
    if y > 0:
        Sum -= presum[x + h - 1,y - 1].sum()
    if x > 0 and y > 0:
        Sum += presum[x - 1,y - 1].sum()
    #print(Sum,w*h)
    if Sum >= h * w * threshold / 100:
        return True
    return False
def BinarySearchWidth(x,y,h,n,m,presum,threshold):
    l = 10;r = m - y
    success = False;w = 0
    while l <= r:
        mid = (l + r) // 2
        #print(h,mid)
        if check(x,y,h,mid,n,m,presum,threshold) == True:
            w = mid
            l = mid + 1
            success = True
        else:
            r = mid - 1
    return success,w


def BinarySearchHeight(x,y,n,m,presum,threshold):
    l = 50;r = n - x;ans = 0;w = 0;success = False
    while l <= r - 1:
        mid = (l + r) // 2
        #print(l,r,mid)
        success,w = BinarySearchWidth(x,y,mid,n,m,presum,threshold)
        if success:
            l = mid + 1
            ans = mid
        else:
            r = mid - 1
    return success,w,ans
def solve(n,m,presum,threshold):
    xnum = 50; ynum = 20
    success = False
    X = 0;Y = 0;W = 0;H = 0
    anssum = 0
    for i in range(0,xnum):
        for j in range(0,ynum):
            x = n * i // xnum
            y = m * i // ynum
            s,w,h = BinarySearchHeight(x,y,n,m,presum,threshold)
            if anssum < w * h:
                success = True
                X = x;Y = y;W = w;H = h;
                anssum = w * h
    #print(anssum,success)
    return success,X,Y,W,H

"""
img = cv2.putText(img, "hello world!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)
cv2.putText(图像, 文字, (x, y), 字体, 大小, (b, g, r), 宽度)
"""
def findjn(s,jnsrc,threshold = 50):
    presum = PreSum(s)
    n,m,ch = s.shape
    success,x,y,w,h = solve(n,m,presum,threshold)
    if success:
        cv.rectangle(jnsrc,(y,x),(y + w - 1,x + h - 1),[0,0,255],5)
        jnsrc = cv.putText(jnsrc,"JNG",(y,x + h - 1),cv.FONT_HERSHEY_SIMPLEX,1.2,[255,255,255],2)
    return jnsrc

def main():
    for i in range(2):
        s = cv.imread(f"img/jn_1_{i + 1}.jpg")
        jnsrc = cv.imread(f"img/jn{i + 1}.jpg")
        jnsrc = findjn(s,jnsrc)
        cv.imshow(f"src{i + 1}", jnsrc)
        #cv.imwrite(f"img/jn_2_{i + 1}.jpg", jnsrc,[int(cv.IMWRITE_JPEG_QUALITY),100])

    cv.waitKey(0)
    cv.destroyAllWindows()
if __name__ == '__main__':
    main()