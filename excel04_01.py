import pandas  as pd
import numpy as np

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
# pd.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50
# pd.set_option('max_colwidth', 100)

# 第4章 数据预处理
# 本章主要讲的是数据的预处理，对清洗完的数据进行整理以便后
# 期的统计和分析工作。主要包括数据表的合并，排序，数值分列，数
# 据分组及标记等工作。
# 1. 数据表合并
# 首先是对不同的数据表进行合并，我们这里创建一个新的数据表 df1，并将df和df1两个数据表进行合并。
# 在Excel中没有直接完成数据 表合并的功能，可以通过VLOOKUP函数分步实现。在Python中可以 通过merge函数一次性实现。下面建立df1数据表，用于和df数据表进 行合并。
df1 = pd.DataFrame({"id": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
                    "gender": ['male', 'female', 'male', 'female', 'male ', 'female', 'male', 'female'],
                    "pay": ['Y', 'N', 'Y', 'Y', 'N', 'Y', 'N', 'Y', ],
                    "m-point": [10, 12, 20, 40, 40, 40, 30, 20]})
df = pd.DataFrame({"id": [1001, 1002, 1003, 1004, 1005, 1006], "date": pd.date_range('20130102', periods=6),
                   "city": ['Beijing ', 'SH', ' guangzhou ', 'Shen zhen', 'shanghai', 'BEIJING '],
                   "age": [23, 44, 54, 32, 34, 32], "category": ['100-A', '100-B', '110-A', '110-C', '2 10-A', '130-F'],
                   "price": [1200, np.nan, 2133, 5433, np.nan, 4432]},
                  columns=['id', 'date', 'city', 'category', 'age', 'price'])
print(df1.head(10))
print(df.head(10))
# 使用merge函数对两个数据表进行合并，合并的方式为inner，将 两个数据表中共有的数据匹配到一起生成新的数据表。并命名为 df_inner。
print('# 数据表匹配合并')
print('inner')
print(pd.merge(df, df1, how='inner'))
print('left')
print(pd.merge(df, df1, how='left'))
print('right')
print(pd.merge(df, df1, how='right'))
print('outer')
print(pd.merge(df, df1, how='outer'))

# 2. 设置索引列
# 完成数据表的合并后，我们对df_inner数据表设置索引列，索引
# 列的功能很多，可以进行数据提取，汇总，也可以进行数据筛选等。
# 设置索引的函数为set_index。
# 设置索引列

df_inner = pd.merge(df, df1, how='inner')

print('排序')
print(df_inner.sort_values(by=['age']))
# 按索引列排序
df_inner.set_index('id')
df_inner.sort_index()
print(df_inner.head(10))

# 4. 数据分组
# Excel中可以通过VLOOKUP函数进行近似匹配来完成对数值的分
# 组，或者使用“数据透视表”来完成分组。相应的 Python中使用where
# 函数完成数据分组。
# Where函数用来对数据进行判断和分组，下面的代码中我们对
# price列的值进行判断，将符合条件的分为一组，不符合条件的分为另
# 一组，并使用group字段进行标记。
print('# 如果price列的值>3000，group列显示high，否则显示low')
df_inner['group'] = np.where(df_inner['price'] > 3000, 'high', 'low')
print(df_inner.head(10))
# 除了where函数以外，还可以对多个字段的值进行判断后对数据
# 进行分组，下面的代码中对city列等于beijing并且price列大于等于
# 4000的数据标记为1。
print('# 对复合多个条件的数据进行分组标记')
print(df_inner.head(10))
df_inner.loc[(df_inner['age'] == 23) & (df_inner['date'] == '2013-01-02'), 'sign'] = 1
print(df_inner.head(10))

# 5. 数据分列
# 与数据分组相反的是对数值进行分列，Excel中的数据目录下提
# 供“分列”功能。在Python中使用split函数实现分列。
# 在数据表中category列中的数据包含有两个信息，前面的数字为
# 类别id，后面的字母为size值。中间以连字符进行连接。我们使用split
# 函数对这个字段进行拆分，并将拆分后的数据表匹配回原数据表中。
print('# #对category字段的值依次进行分列，并创建数据表，索引值为df_inner的索引列，列名称为category和size')
print(pd.DataFrame((x.split('-') for x in df_inner['category']), index=df_inner.index, columns=['category', 'size']))

print('# 将完成分列后的数据表与原df_inner数据表进行匹配')
split = pd.DataFrame((x.split('-') for x in df_inner['category']), index=df_inner.index, columns=['category', 'size'])
df_inner = pd.merge(df_inner, split, right_index=True, left_index=True)
print(df_inner)
