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
                   "city": ['Beijing', 'SH', ' guangzhou ', 'Shen zhen', 'shanghai', 'BEIJING '],
                   "age": [23, 44, 54, 32, 34, 32], "category": ['100-A', '100-B', '110-A', '110-C', '2 10-A', '130-F'],
                   "price": [1200, np.nan, 2133, 5433, np.nan, 4432]},
                  columns=['id', 'date', 'city', 'category', 'age', 'price'])
#
# 第5章 数据提取
# 数据提取，也是数据分析中最常见的一个工作。这部分主要使用
# 3个函数，即loc、iloc和ix。loc函数按标签值进行提取，iloc函数按位
# 置进行提取，ix函数可以同时按标签和位置进行提取。下面介绍每一
# 种函数的使用方法。
# 1. 按标签提取(loc)
# Loc函数按数据表的索引标签进行提取，下面的代码中提取了索
# 引列为3的单条数据。


df_inner = pd.merge(df, df1, how='inner')
print(df_inner)
print('#按索引提取单行的数值')
print(df_inner.loc[3])

# 使用冒号可以限定提取数据的范围，冒号前面为开始的标签值，
# 后面为结束的标签值。下面提取了0到3的数据行。
print('# 按索引提取区域行数值')
print(df_inner.loc[0:3])

# Reset_index函数用于恢复索引，这里我们重新将date字段的日期
# 设置为数据表的索引，并按日期进行数据提取。
print('# 重设索引')
print(df_inner.reset_index())
print('# 设置日期为索引')
df_inner = df_inner.set_index('date')
print(df_inner)

# 使用冒号限定提取数据的范围，冒号前面为空表示从0开始。提
# 取所有2013年1月4日以前的数据。
print('# 提取4日之前的所有数据')
print(df_inner[:'2013-01-04'])

# 2. 按位置提取(iloc)
# 使用iloc函数按位置对数据表中的数据进行提取，这里冒号前后
# 的数字不再是索引的标签名称，而是数据所在的位置，从0开始。
print('# 使用iloc按位置区域提取数据')
print(df_inner.iloc[:4, :5])

# iloc函数除了可以按区域提取数据，还可以按位置逐条提取，前
# 面方括号中的0,2,5表示数据所在行的位置，后面方括号中的数表示所
# 在列的位置。
# 使用iloc按位置单独提取数据
print(df_inner.iloc[[0, 2, 5], [4, 5]])

# 3. 按标签和位置提取（ix）
# ix是loc和iloc的混合，既能按索引标签提取，也能按位置进行数
# 据提取。下面代码中行的位置按索引日期设置，列按位置设置。
print('# 使用ix按索引标签和位置混合提取数据')
print(df_inner.ix[:'2013-01-05', :4])

# 4. 按条件提取（区域和条件值）
# 除了按标签和位置提起数据以外，还可以按具体的条件进行数
# 据。下面使用loc和isin两个函数配合使用，按指定条件对数据进行提
# 取。
# 使用isin函数对city中的值是否为beijing进行判断。
print('# 判断city列的值是否为beijing')
print(df_inner['city'].isin(['Beijing']))

# 将isin函数嵌套到loc的数据提取函数中，将判断结果为Ture数据
# 提取出来。这里我们把判断条件改为city值是否为beijing和shanghai。
# 如果是就把这条数据提取出来。
print('# 先判断city列里是否包含beijing和shanghai，然后将复合条件的数据提取出来。')
print(df_inner.loc[df_inner['city'].isin(['Beijing', 'shanghai'])])

print('数值提取还可以完成类似数据分列的工作，从合并的数值中提取出制定的数值。')
category = df_inner['category']
print(category)

print('#提取前三个字符，并生成数据表')
print(pd.DataFrame(category.str[:3]))
