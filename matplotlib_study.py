import numpy as np
from matplotlib import pyplot as plt
fig = plt.figure(figsize=(10,10),dpi=300) #生成的图片大小 figsize = (a,b) dpi :c 则图片大小为 ：【a*c,b*c】
x = np.linspace(0, 2*np.pi, 1000)#注意，range函数只能用来生成整数序列
y = np.sin(x)
#设置x轴刻度
# plt.xticks() #把坐标的名字变掉，一般不常用
plt.plot(x,y)
plt.xlim([0,2*np.pi])
plt.ylim([-1,1])
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = sin(x)')
plt.savefig("./sin_wave.svg")#一定注意，保存要在show之前，因为show一下会生成新的幕布
plt.show()

#一个坐标轴下绘制多个图片
x = np.linspace(0, 2, 100)
# Note that even in the OO-style, we use `.pyplot.figure` to create the␣figure.
fig2, ax = plt.subplots() # Create a figure and an axes.
ax.plot(x, x, label='linear') # Plot some data on the axes.
ax.plot(x, x**2, label='quadratic') # Plot more data on the axes...
ax.plot(x, x**3, label='cubic') # ... and some more.
ax.set_xlabel('x label') # Add an x-label to the axes.
ax.set_ylabel('y label') # Add a y-label to the axes.
ax.set_title("Simple Plot") # Add a title to the axes.
ax.legend() # Add a legend.
plt.show()

