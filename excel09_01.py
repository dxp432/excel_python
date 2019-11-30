import pandas  as pd
import numpy as np

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
# pd.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50
# pd.set_option('max_colwidth', 100)
df1 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})

print(df1)
# 第9章 数据输出
# 处理和分析完的数据可以输出为xlsx格式和csv格式。
# 1. 写入Excel
# 输出到Excel格式
df1.to_excel('Excel_to_Python.xls', sheet_name='bluewhale_cc')
# 2. 写入csv
# # 输出到CSV格式
df1.to_csv('Excel_to_Python.csv')
