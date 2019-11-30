import pandas  as pd
import numpy as np

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
# pd.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50
# pd.set_option('max_colwidth', 100)
df1 = pd.DataFrame({"id": [1001, 1003, 1002, 1004, 1005, 1006, 1007, 1008],
                    "gender": ['male', 'female', 'male', 'female', 'male ', 'female', 'male', 'female'],
                    "pay": ['Y', 'N', 'Y', 'Y', 'N', 'Y', 'N', 'Y', ],
                    "m-point": [10, 12, 20, 40, 40, 40, 30, 20]})
df = pd.DataFrame({"id": [1001, 1003, 1002, 1004, 1005, 1006], "date": pd.date_range('20130102', periods=6),
                   "city": ['beijing', 'shanghai', ' guangzhou ', 'Shen zhen', 'shanghai', 'beijing'],
                   "age": [23, 44, 54, 32, 34, 32], "category": ['100-A', '100-B', '110-A', '110-C', '2 10-A', '130-F'],
                   "price": [1200, np.nan, 2133, 5433, np.nan, 4432]},
                  columns=['id', 'date', 'city', 'category', 'age', 'price'])

df_inner = pd.merge(df, df1, how='inner')
print('# 重设索引')
print(df_inner.reset_index())
print('# 设置日期为索引')
df_inner = df_inner.set_index('date')
print(df_inner)

# 第7章 数据汇总
# 本章主要讲解如何对数据进行分类汇总。Excel中使用分类汇总
# 和数据透视可以按特定维度对数据进行汇总，Python中使用的主要函
# 数是groupby和pivot_table。下面分别介绍这两个函数的使用方法。
# 1. 分类汇总
# Excel的数据目录下提供了“分类汇总”功能，可以按指定的字段
# 和汇总方式对数据表进行汇总。Python中通过Groupby函数完成相应的
# 操作，并可以支持多级分类汇总。
# Groupby是进行分类汇总的函数，使用方法很简单，制定要分组
# 的列名称就可以，也可以同时制定多个列名称，groupby按列名称出
# 现的顺序进行分组。同时要制定分组后的汇总方式，常见的是计数和
# 求和两种。
# 对所有列进行计数汇总
print(df_inner.groupby('city').count())
# 可以在groupby中设置列名称来对特定的列进行汇总。下面的代
# 码中按城市对id字段进行汇总计数。
print('# 对特定的ID列进行计数汇总')
print(df_inner.groupby('city')['id'].count())

# 在前面的基础上增加第二个列名称，分布对city和size两个字段进
# 行计数汇总。
print('#对两个字段进行汇总计数')
print(df_inner.groupby(['city', 'gender'])['id'].count())

# 除了计数和求和外，还可以对汇总后的数据同时按多个维度进行
# 计算，下面的代码中按城市对price字段进行汇总，并分别计算price的
# 数量，总金额和平均金额。
print('#对city字段进行汇总并计算price的合计和均值。')
print(df_inner.groupby('city')['price'].agg([len, np.sum, np.mean]))
