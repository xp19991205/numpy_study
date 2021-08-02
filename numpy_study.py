# ===================================
#numpy、scipy、matplotlib三大工具可以认为是替代matlab的常用工具箱
# ===================================
import numpy as np
# 矩阵运算
I = np.eye(3) #生成三阶单位矩阵
print(I)
A = np.array([[1,2,3],[4,5,6],[7,8,9]]);
A.transpose() #或者直接使用转置属性T
print(np.dot(A,A))
print(A[1,1]) #读取a11处的元素
print(A[[2,2,2],[0,1,2]]) #读取a31,a32,a33处的元素
#矩阵元素
# ===================================
#在下面的函数前面加上arg就可以获取到对应值的索引index
#1.最大最小numpy.amin()和numpy.amax():如果不指定axis，默认是求所有矩阵元素的最大最小值，axis=0：求列的最大最小，axis=1,求行的最大最小
print(np.amax(A,axis= 0 ))
print(np.amin(A,axis= 1))
#2.最大最小之差numpy.ptp()如果不指定axis，默认是求所有矩阵元素的最大最小值，axis=0：求列的最大最小，axis=1,求行的最大最小
print(np.ptp(A))
print(np.ptp(A,axis=0))
#3.计算平均值，仍然有axis这个参数：numpy.mean()
B = np.array([[100,90,90],[90,80,80],[85,80,80]])
print(np.mean(B,axis=0))#按列求均值
print(np.mean(B,axis=1))#按行求均值
#4.计算加权平均值，仍然有axis这个参数：numpy.mean()
print(np.average(B,weights=[1/6,1/3,1/2],axis=1)) #1/6*a[i,0]+1/3*a[i,1]+1/2*a[i,2]
#5.计算标准差，仍然有axis这个参数:numpy.std() 标准差定义:std = sqrt(mean((x - x.mean())**2))
print(np.std(B,axis=0))
#5.计算方差，仍然有axis这个参数:numpy.std() 方差定义: mean((x - x.mean())** 2)。
#这里的方差和标准差都采用的是除以N的方式，ddof=1对于matlab除以N-1的情况
#6.数据排序：numpy中的数据排序与我们excel中的排序有不同，排序单纯按照行或按照列进行
print(np.var(B,axis=0,ddof=1))
B.sort(axis=0)#按列进行排序，按行排序可以选择axis =1这个参数
print(B)
C = np.array([[100,90,90],[90,80,80],[85,80,80]])
print(np.argmin(C,axis=0))
#===================================================
#线性代数函数库
#1.矩阵乘法
#numpy.dot(): 计算一维向量内积，二维矩阵乘积
#numpy.matmul():矩阵乘法
#2.矩阵行列式
#numpy.linalg.XXX
#包括 det：行列式 SVD分解
#求解线性方程组
#===================================================
C1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
C2 = C1;
C3 = np.matmul(C1,C2)
print(C3)
C4 = np.dot(C1,C2);
print(C4)
print(np.linalg.det(C4))
print(np.linalg.svd(C4))
numpy.linalg.solve()