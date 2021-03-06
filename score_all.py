#这里我们编写一个程序做excel表数据的合并
import numpy as np
import pandas as pd
df = pd.DataFrame()
print("初始的dff")
print(df)
filename_1 = './score_all/'
filename_2 = '.xls'
for k in range(6):
    filename = filename_1 + str(k+1) +filename_2
    print(filename)
    for l in range(2):
        try:
            # df_temp =  pd.read_excel('./score_all/1.xls',index_col= 0,sheet_name=k)
            df_temp = pd.read_excel(filename, index_col=0, sheet_name=l)
            # df_temp = pd.read_excel(filename, index_col=None, sheet_name=l)
            # print('yes')
        except:
            message = filename +'sheet'+str(l)+'读取失败'
            print(message)
            # print('excel‘+str(k+1)+ ’Sheet‘ + str(l) + ‘读取excel失败')
        df = df.append(df_temp)

print(df)
# df1 = df.groupby(['学号','姓名']).mean()
df1 = df.drop_duplicates(subset=None, keep='first', inplace=False)
#subset是根据字段去除重复，多个字段就写成列表形式，默认是所有列
#keep first就是保留第一个，last就是最后
#inplace 默认为False，不直接进行修改
df1 = df1.dropna(axis=0,how='all')
#这里做了一个数据的缺失值处理，这里删除了那些一行都是NAN的值
print(df1)
df2 = df1.sort_values("智育成绩",inplace=False,ascending= False)
#这里的inplace是对下面的操作进行选择，False原Dataframe不变，如果True原Dataframe发生改变
#这里的ascending是对升序降序的选择
#第一个是by参数，按照什么列进行排序


df1.to_excel('output.xlsx',sheet_name='全部数据')
df2.to_excel('output_ranked.xlsx',sheet_name="排名统计")
df3 = df2
rank = np.array(range(df3.shape[0])).T
rank = rank+1
df3['智育成绩排名'] = rank
print(df3)
# df3["智育成绩排名"]
# df1 = pd.read_excel('./score_all/1.xls',index_col= 0,sheet_name=0)
# df2 = pd.read_excel('./score_all/1.xls',index_col= 0,sheet_name=1)
# print(df1)
# print(df1[:,2])
#直接给出数据的一些统计特征
#均值 mean 标准差std 最小值min 百分位数 max最大值
print(df3.describe())
print('data_filtered')
print(df3.loc[((df3['智育成绩'] > 90) & (df3['综合排序'] <5))])#这里做的一个d多条件数据的筛选
print(df3.loc[df3['智育成绩'] > 90]) #这里做一个单条件的筛选
# print(df3.iloc[[0,1],:]) #按行号列号进行求解
# print(df3.iloc[:,[0,1]]) #按行号列号进行求解
#查看数据缺失情况，做出对应的调整
# print(df3.info())
# df3.dropna(axis=0,how='all')
#pandas计算均值等的时候，可以自动忽略NAN，比numpy方便的多

print(df1.dropna(axis = 0,how = 'all'))