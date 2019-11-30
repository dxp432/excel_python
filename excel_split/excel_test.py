import pandas  as pd
import numpy as np

# 读取
pf = pd.DataFrame(pd.read_excel('excel.xls', sheet_name='Sheet1'))
print(pf.head(10))

# # 将所有gender为male的值改为0，female改为1
# # https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
# pf.loc[pf['gender'] == 'male', 'gender'] = 0
# pf.loc[pf['gender'] == 'female', 'gender'] = 1
# print(pf.head(10))
#
# # 增加行数据，在第5行新增
# pf.loc[5] = ['James', 32, 'male']
# print(pf.head(10))
#
# # # 增加列数据，给定默认值None
# pf['profession'] = None
# print(pf.head(10))
#
# # 删除gender列，需要指定axis为1，当删除行时，axis为0
# pf = pf.drop('gender', axis=1)
# print(pf.head(10))
#
# # 删除第3,4行，这里下表以0开始，并且标题行不算在类
# pf = pf.drop([1, 2], axis=0)
# print(pf.head(10))
# pf = pf.iloc[:, [0]]
# pf = pf.str.split()
pf = pf['    name  age  gender'].str.split(expand=True)
print(pf.head(10))
pf.columns = ['num', 'name', 'age', 'gender']  #
print(pf.head(10))

# 写入
filepath = 'excel01.xls'
writer = pd.ExcelWriter(filepath)
pf.to_excel(excel_writer=writer, index=False, sheet_name='Sheet1')
# pf.to_excel(excel_writer=writer, sheet_name='表1')
writer.save()
writer.close()
