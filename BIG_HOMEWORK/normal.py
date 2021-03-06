#库函数
import cv2 as cv
import numpy as np
def fushi(src,x,B):
    n,m,ch = src.shape
    ret = src.copy()
    x = np.array(x)
    for i in range(1,n - 1):
        for j in range(1,m - 1):
                for p in range(0,3):
                    for q in range(0,3):
                        if B[p][q] == 1 and (src[i + p - 1,j + q - 1] == x).all() == False:
                            ret[i,j] = src[i + p - 1,j + q - 1]
    return ret

def pengzhang(src,x,B):
    n,m,ch = src.shape
    ret = src.copy()
    x = np.array(x)
    for i in range(1,n - 1):
        for j in range(1,m - 1):
                for p in range(0, 3):
                    for q in range(0, 3):
                        if B[p][q] == 1 and (src[i + p - 1, j + q - 1] == x).all():
                            ret[i, j] = x
    return ret

def kai(src,x,B):
    ans = fushi(src,x,B)
    ans = pengzhang(ans,x,B)
    return ans

def bi(src,x,y):
    ans = pengzhang(src,x,y)
    ans = fushi(ans,x,y)
    return ans

#src1减去src2,相同的标为x,不同的标为y
def sub(src1,src2,x,y):
    n,m,ch = src1.shape
    ans = src1.copy()
    for i in range(n):
        for j in range(m):
            if(ans[i,j] == src2[i,j]): ans[i,j] = x
    return ans
#src1中原本在src2中就是x的要标记为y
def subc(src1,src2,x,y):
    n,m,ch = src1.shape
    for i in range(n):
        for j in range(m):
            if(src2[i,j] == x): src1[i,j] = y
    return src1


def equal(src1,src2):
    n,m,ch = src1.shape
    for i in range(n):
        for j in range(m):
            for k in range(ch):
                x,y = int(src1[i,j,ch]),int(src2[i,j,ch])
                if(x != y): return False
    return True
#图src的x,y点填充为c,背景为b
def tianchong(src,x,y,c,b,B):
    ans = src.copy()
    ans = subc(ans, src, c, b)
    la = ans.copy()
    ans[x,y] = c
    num = 0
    while(equal(ans,la) == False):
        num += 1
        if(num % 10 == 0):
            cv.imshow(f"{num}", ans)
        print(num)
        la = ans.copy()
        ans = pengzhang(ans, c, b, B)
        ans = subc(ans,src,c,b)
    return subc(ans,src,c,c)


if __name__ == '__main__':
    s = cv.imread(f"img/pkq1.jpg")
    cv.imshow("s",s)
    cv.waitKey(0)
    cv.destroyAllWindows()
