import pandas  as pd
import numpy as np

df = pd.DataFrame({"id": [1001, 1002, 1003, 1004, 1005, 1006], "date": pd.date_range('20130102', periods=6),
                   "city": ['Beijing ', 'SH', ' guangzhou ', 'Shen zhen', 'shanghai', 'BEIJING '],
                   "age": [23, 44, 54, 32, 34, 32], "category": ['100-A', '100-B', '110-A', '110-C', '2 10-A', '130-F'],
                   "price": [1200, np.nan, 2133, 5433, np.nan, 4432]},
                  columns=['id', 'date', 'city', 'category', 'age', 'price'])
print(df.head(10))
# 使用price均值对NA进行填充
df['price'] = df['price'].fillna(df['price'].mean())
# Python中dtype是查看数据格式的函数，与之对应的是astype函 数，用来更改数据格式。下面的代码中将price字段的值修改为int格 式。
# 更改数据格式
print(df['price'].astype('int').head(10))

# 5. 更改列名称
# Rename是更改列名称的函数，我们将来数据表中的category列更 改为category-size。下面是具体的代码和更改后的结果。
# 更改列名称
print("#更改列名称 ")
print(df.head(10))
df = df.rename(columns={'category': 'category-size'})
print(df.head(10))

print('city列大小写转换 ')
df['city'] = df['city'].str.lower()

# 6. 删除重复值

# 很多数据表中还包含重复值的问题，Excel的数据目录下有“删除 重复项”的功能，可以用来删除数据表中的重复值。默认Excel会保留 最先出现的数据，删除后面重复出现的数据。
# Python中使用drop_duplicates函数删除重复值。我们以数据表中的 city列为例，city字段中存在重复值。默认情况下drop_duplicates()将删 除后出现的重复值(与Excel逻辑一致)。
# 增加keep='last'参数后将删除 最先出现的重复值，保留最后的值。下面是具体的代码和比较结果。
# 原始的city列中beijing存在重复，分别在第一位和最后一位。
# 使用默认的drop_duplicates()函数删除重复值，从结果中可以看到 第一位的beijing被保留，最后出现的beijing被删除。
print('# 删除后出现的重复值')
print(df['city'].drop_duplicates())

# 22
# 设置keep='last‘’参数后，与之前删除重复值的结果相反，第一位 出现的beijing被删除，保留了最后一位出现的beijing。
print('# 删除先出现的重复值')
print(df['city'].drop_duplicates(keep='last'))

# 7. 数值修改及替换
# 数据清洗中最后一个问题是数值修改或替换，Excel中使用“查找 和替换”功能就可以实现数值的替换。
# Python中使用replace函数实现数据替换。数据表中city字段上海存 在两种写法，分别为shanghai和SH。我们使用replace函数对SH进行替 换。
print('#数据替换 ')
print(df['city'].replace('sh', 'shanghai'))

