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
plt.xticks(np.linspace(0,2*np.pi,5)) #x轴的定位点（标的点）
#同理，这里有plt.yticks一样的
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
#下面介绍的批量生成字符串的方法可以用在xtick 或者ytick中
print(['hello{}'.format(i) for i in x])

fig2 = plt.figure(figsize=(10,10),dpi=100)
plt.rcParams['font.sans-serif']=['SimHei'] #指定默认字体 SimHei为黑体
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
t = np.linspace(0,2,2000)
#第一种方式
plt.plot(t,np.sin(t),'r--',t,np.cos(t),'bo')
# 这里的第三个参数类似matlab中的线形，具体请看文档Controlling line properties
plt.legend(['sin(x)','cos(x)'])
# myfont = fm.FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
plt.title("三角函数曲线")
plt.xlabel('自变量x')
plt.ylabel("函数值")
#绘制网址
plt.grid(alpha = 0.8) #对应xticks的点数 alpha 对应这些网格的透明度
plt.show()

# #第二种方式
# lines = plt.plot(t, np.cos(t), t, np.sin(t))
# # use keyword args
# plt.setp(lines, color='r', linewidth=2.0)
# # or MATLAB style string value pairs
# plt.setp(lines, 'color', 'r', 'linewidth', 2.0)
# plt.show()

#下面开始绘制直方图
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)
# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()

#绘制散点图
plt.figure(figsize=(20,20),dpi= 60)
x = np.array([1,2,3,4])
y = np.array([1,2,3,4])
plt.scatter(x,y)
plt.show()
#bar:条形图
film_name = ['战狼2','绣春刀','机器侠','美人鱼','哆啦A梦']
film_score = [100,90,100,80,70]
plt.bar(film_name,film_score,color = 'r',width= 0.5)
plt.show()
#barh:横向的条形图
film_name = ['战狼2','绣春刀','机器侠','美人鱼','哆啦A梦']
film_score = [100,90,100,80,70]
plt.barh(film_name,film_score,color = 'orange',height= 0.5)
plt.show()

