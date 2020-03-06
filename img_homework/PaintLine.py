import matplotlib.pyplot as plt
import matplotlib
matplotlib.rc("font", family="AR PL UKai CN")
def paint(rule):
    X = []
    for i in range(256):
        X.append(i)
    plt.plot(X,X,color='b')
    plt.plot(X, rule,color='r')
    plt.title("灰度映射",fontsize = 25)
    plt.xlabel("原始值",fontsize = 20)
    plt.ylabel("目标值",fontsize = 20)
    plt.show()