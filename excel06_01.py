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
                   "city": ['beijing', 'SH', ' guangzhou ', 'Shen zhen', 'shanghai', 'BEIJING '],
                   "age": [23, 44, 54, 32, 34, 32], "category": ['100-A', '100-B', '110-A', '110-C', '2 10-A', '130-F'],
                   "price": [1200, np.nan, 2133, 5433, np.nan, 4432]},
                  columns=['id', 'date', 'city', 'category', 'age', 'price'])

df_inner = pd.merge(df, df1, how='inner')
print('# 重设索引')
print(df_inner.reset_index())
print('# 设置日期为索引')
df_inner = df_inner.set_index('date')
print(df_inner)

# 第6章 数据筛选
# 使用与，或，非三个条件配合大于，小于和等于对数据进行筛
# 选，并进行计数和求和。与Excel中的筛选功能和countifs和sumifs功能
# 相似。
# 按条件筛选（与、或、非）
# Excel数据目录下提供了“筛选”功能，用于对数据表按不同的条
# 件进行筛选。Python中使用loc函数配合筛选条件来完成筛选功能。配
# 合sum和count函数还能实现Excel中sumif和countif函数的功能。
# 使用“与”条件进行筛选，条件是年龄大于25岁，并且城市为
# beijing。筛选后只有一条数据符合要求。
# 使用“与”条件进行筛选
print('# 使用“与”条件进行筛选')
print(
    df_inner.loc[(df_inner['age'] > 22) & (df_inner['city'] == 'beijing'), ['id', 'city', 'age', 'category', 'gender']])

# 使用“或”条件进行筛选，年龄大于25岁或城市为beijing。筛选后
# 有6条数据符合要求。
print('#使用“或”条件筛选')
print(df_inner.loc[
          (df_inner['age'] > 25) | (df_inner['city'] == 'beijing'), ['id', 'city', 'age', 'category', 'gender']])
# 在前面的代码后增加price字段以及sum函数，按筛选后的结果将
# price字段值进行求和，相当于Excel中sumifs的功能。
print('# 对筛选后的数据按price字段进行求和')
print(df_inner.loc[(df_inner['age'] > 23) | (df_inner['city'] == 'beijing'), ['id', 'city', 'age', 'category', 'gender',
                                                                              'price']].price.sum())

# 使用“非”条件进行筛选，城市不等于beijing。符合条件的数据有
# 39
# 异步社区会员 lizhimiao(18926120246) 专享 尊重版权
# 4条。将筛选结果按id列进行排序。
print('# 使用“非”条件进行筛选')
print(df_inner.loc[(df_inner['city'] != 'beijing'), ['id', 'city', 'age',
                                                     'category', 'gender']].sort_values(['id']))
# 在前面的代码后面增加city列，并使用count函数进行计数。相当
# 于Excel中的countifs函数的功能。
print('# 对筛选后的数据按city列进行计数')
print(df_inner.loc[(df_inner['city'] != 'beijing'), ['id', 'city', 'age',
                                                     'category', 'gender']].sort_values(['id']).city.count())
# 4
# 还有一种筛选的方式是用query函数。下面是具体的代码和筛选
# 结果。
print('# 使用query函数进行筛选')
print(df_inner.query('city == ["beijing", "shanghai"]'))

# 在前面的代码后增加price字段和sum函数。对筛选后的price字段
# 进行求和，相当于Excel中的sumifs函数的功能。
print('# 对筛选后的结果按price进行求和')
print(df_inner.query('city == ["beijing", "shanghai"]').price.sum())
