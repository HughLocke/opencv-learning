import cv2 as cv
import numpy as np
import random
import sys
sys.setrecursionlimit(40000)
def fushi(src,x,y,B):
    n,m = src.shape
    ret = src.copy()
    for i in range(1,n - 1):
        for j in range(1,m - 1):
            for p in range(0,3):
                for q in range(0,3):
                    if B[p][q] == 1 and src[i + p - 1,j + q - 1] != x: ret[i,j] = y
    return ret

def pengzhang(src,x,y,B):
    n,m = src.shape
    ret = src.copy()
    for i in range(1,n - 1):
        for j in range(1,m - 1):
            for p in range(0, 3):
                for q in range(0, 3):
                    if B[p][q] == 1 and src[i + p - 1, j + q - 1] == x: ret[i, j] = x
    return ret

def kai(src,x,y):
    ans = fushi(src,x,y)
    ans = pengzhang(ans,x,y)
    return ans

def bi(src,x,y):
    ans = pengzhang(src,x,y)
    ans = fushi(ans,x,y)
    return ans

#src1减去src2,相同的标为x,不同的标为y
def sub(src1,src2,x,y):
    n,m = src1.shape
    ans = src1.copy()
    for i in range(n):
        for j in range(m):
            if(ans[i,j] == src2[i,j]): ans[i,j] = x
    return ans
#src1中原本在src2中就是x的要标记为y
def subc(src1,src2,x,y):
    n,m = src1.shape
    for i in range(n):
        for j in range(m):
            if(src2[i,j] == x): src1[i,j] = y
    return src1


def equal(src1,src2):
    n,m = src1.shape
    for i in range(n):
        for j in range(m):
            x,y = int(src1[i,j]),int(src2[i,j])
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

ret = 1
def dfs(i,j,x,p,st):
    global ret
    if i - 1 >= 0 and ret[i - 1, j] == x:
        ret[i - 1,j] = p
        dfs(i - 1, j, x, p, st)
    if i + 1 < n and ret[i + 1, j] == x :
        ret[i + 1,j] = p
        dfs(i + 1, j, x, p,st)
    if j - 1 >= 0 and ret[i, j - 1] == x:
        ret[i,j - 1] = p
        dfs(i, j - 1, x, p,st)
    if j + 1 < m and ret[i, j + 1] == x:
        ret[i,j + 1] = p
        dfs(i, j + 1, x, p,st)

cnt = 0
def ltfl(x):
    global ret
    n,m = ret.shape
    for i in range(n):
        for j in range(m):
            if(ret[i,j] == x):
                p = random.randint(10,240)
                ret[i,j] = p
                dfs(i, j,x,p,0)

    return ret

#src = cv.imread("01_实验测试图_汇总/")
#src = cv.imread("01_实验测试图_汇总/05_数字形态学/Fig9.07(a).bmp")
src = cv.imread("01_实验测试图_汇总/01_01_24位图像/2.png")
ANS = src.copy()
cv.imshow("src",src)
src = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
n,m = src.shape
ANS = cv.cvtColor(ANS,cv.COLOR_RGB2HSV)
for i in range(n):
    for j in range(m):
        src[i,j] = ANS[i,j,1]

B = [[1,1,1],[1,1,1],[1,1,1]]
cv.imshow("hui",src)

x = 255
y = 0
#ans = tianchong(src,50,50,255,0,B)

for i in range(n):
    for j in range(m):
        if src[i,j] > 20: src[i,j] = 255
        else: src[i,j] = 0
cv.imshow("two",src)

src = fushi(src,255,0,B)
src = fushi(src,255,0,B)
src = fushi(src,255,0,B)
src = fushi(src,255,0,B)
src = fushi(src,255,0,B)
src = fushi(src,255,0,B)
src = pengzhang(src,255,0,B)
src = pengzhang(src,255,0,B)
src = pengzhang(src,255,0,B)
src = pengzhang(src,255,0,B)
src = pengzhang(src,255,0,B)
src = pengzhang(src,255,0,B)
src = pengzhang(src,255,0,B)


cv.imshow("pengzhang",src)
ret = src.copy()
#ans = ltfl(x)
'''
cv.imshow("tmp",ans)
for i in range(n):
    for j in range(m):
        ANS[i,j] = [0,0,0]
        if(ans[i,j] >= 10 and ans[i,j] <= 240):
            t = ans[i,j]
            ANS[i,j,0] = t * 123 % 255
            ANS[i, j, 1] = t * 234 % 255
            ANS[i, j, 2] = t * 345 % 255
        else:ANS[i,j,0] = ANS[i,j,1] = ANS[i,2] = ans[i,j]

cv.imshow("ans",ans)
cv.imshow("ANS",ANS)
'''
cv.waitKey(0)
cv.destroyAllWindows()