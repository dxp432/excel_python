import pandas as pd
import numpy as np

# 第3章 数据表清洗
# 本章介绍的是对数据表中的问题进行清洗，主要内容包括对空
# 值、大小写问题、数据格式和重复值的处理。这里不包含对数据间的
# 逻辑验证。
# 1. 处理空值(删除或填充)
# 我们在创建数据表的时候在price字段中故意设置了几个NA值。
# 对于空值的处理方式有很多种，可以直接删除包含空值的数据，也可
# 以对空值进行填充，比如用0填充或者用均值填充。还可以根据不同
# 字段的逻辑对空值进行推算。
# Excel中可以通过“查找和替换”功能对空值进行处理，将空值统
# 一替换为0或均值。也可以通过“定位”空值来实现。
# Python中处理空值的方法比较灵活，可以使用 Dropna函数用来删
df = pd.DataFrame({"id": [1001, 1002, 1003, 1004, 1005, 1006],
                   "date": pd.date_range('20130102', periods=6),
                   "city": ['Beijing ', 'SH', ' guangzhou ', 'Shenzhen', 'shanghai', 'BEIJING '],
                   "age": [23, 44, 54, 32, 34, 32], "category": ['100-A', '100-B', '110-A', '110-C', '210-A', '130-F'],
                   "price": [1200, np.nan, 2133, 5433, np.nan, 4432]},
                  columns=['id', 'date', 'city', 'category', 'age', 'price'])
# 除数据表中包含空值的数据，也可以使用fillna函数对空值进行填充。
# 下面的代码和结果中可以看到使用dropna函数后，包含NA值的两个
# 字段已经不见了。返回的是一个不包含空值的数据表。
# 原数据
print(df.head(10))
# 删除数据表中含有空值的行
print(df.dropna(how='any').head(10))
# 删除数据表中含有空值的列：axis=1
print(df.dropna(axis=1, how='any').head(10))

# 除此之外也可以使用数字对空值进行填充，下面的代码使用fillna
# 函数对空值字段填充数字0。
# 使用数字0填充数据表中空值
print(df.fillna(value=0).head(10))
# 使用文字‘空’填充数据表中空值
print(df.fillna(value='空').head(10))

# 我们选择填充的方式来处理空值，使用price列的均值来填充NA
# 字段，同样使用fillna函数，在要填充的数值中使用mean函数先计算
# price列当前的均值，然后使用这个均值对NA进行填充。可以看到两
# 个空值字段显示为3299.5
# 使用price均值对NA进行填充，只显示price列
print(df['price'].fillna(df['price'].mean()))
# 使用price均值对NA进行填充，显示所有数据
print(df.fillna(df['price'].mean()))
# 2. 清理空格
# 除了空值，字符中的空格也是数据清洗中一个常见的问题，下面
# 是清除字符中空格的代码。
# 清除city字段中的字符空格
df['city'] = df['city'].map(str.strip)
print(df.head(10))
# 3. 大小写转换
# 在英文字段中，字母的大小写不统一也是一个常见的问题。
# Excel中有UPPER，LOWER等函数，Python中也有同名函数用来解决
# 大小写的问题。在数据表的city列中就存在这样的问题。我们将city列
# 的所有字母转换为小写。下面是具体的代码和结果。
# city列大小写转换
df['city'] = df['city'].str.lower()
print(df.head(10))

