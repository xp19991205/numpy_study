import numpy as np
from matplotlib import pyplot as plt
fig = plt.figure(figsize=(10,10),dpi=300) #生成的图片大小 figsize = (a,b) dpi :c 则图片大小为 ：【a*c,b*c】
x = np.linspace(0, 2*np.pi, 1000)#注意，range函数只能用来生成整数序列
y = np.sin(x)
plt.plot(x,y)
plt.savefig("./sin_wave.svg")#一定注意，保存要在show之前，因为show一下会生成新的幕布
plt.show()
