#pandas这个库是专门用来数据分析处理的python工具箱
#Series:带标签的一维数组(index)
import numpy as np
import pandas as pd
t = pd.Series([1,12,21,33,22], index= list("abcde"))
print(t)
t = t.astype(float) #改变数值类型，这里不用返回值是变不了的
print(t)
temp_dict = {'name':'Xupeng','telphone_num':'15823489261'}
t_dict = pd.Series(temp_dict)
print(t_dict)
print(t[[0,1]]) #用位置索引
print(t[0])
print(t['a']) #用index进行索引
print(t>10)
print(t[t>10]) #布尔运算得到
print(type(t.values))
print(type(t.index))
df = pd.read_excel('./20210801.xlsx',index_col=0)
print(np.array((df)))
df2 = pd.read_excel('./score_01911701.xlsx',index_col=0,sheet_name=0) #需要表格第一列作为索引，那么选择index_col =0,否则不加这个参数，只读取表格数据
df2 = df2.sort_values(by='C')
print(df2)
data = np.array(df2)
data = data [:,0:3]
print(data)