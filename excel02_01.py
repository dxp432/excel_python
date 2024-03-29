import pandas as pd
import numpy as np

# 第2章 数据表检查
# 本章主要介绍对数据表进行检查。Python中处理的数据量通常会
# 比较大，比如纽约的出租车数据和Citibike的骑行数据，其数据量都
# 在千万级，我们无法一目了然地了解数据表的整体情况，必须要通过
# 一些方法来获得数据表的关键信息。数据表检查的另一个目的是了解
# 数据的概况，例如整个数据表的大小、所占空间、数据格式、是否有
# 空值和重复项和具体的数据内容，为后面的清洗和预处理做好准备。
# 1. 数据维度(行列)
# Excel中可以通过CTRL+向下的光标键，和CTRL+向右的光标键
# 来查看行号和列号。Python中使用shape函数来查看数据表的维度，也
# 就是行数和列数，函数返回的结果(6,6)表示数据表有6行，6列。下面
# 是具体的代码。
# #查看数据表的维度
# df.shape
# (6, 6)
df = pd.DataFrame({"id": [1001, 1002, 1003, 1004, 1005, 1006],
                   "date": pd.date_range('20130102', periods=6),
                   "city": ['Beijing ', 'SH', ' guangzhou ', 'Shenzhen', 'shanghai', 'BEIJING '],
                   "age": [23, 44, 54, 32, 34, 32], "category": ['100-A', '100-B', '110-A', '110-C', '210-A', '130-F'],
                   "price": [1200, np.nan, 2133, 5433, np.nan, 4432]},
                  columns=['id', 'date', 'city', 'category', 'age', 'price'])

print(df.shape)
# 2. 数据表信息
# 使用info函数查看数据表的整体信息，这里返回的信息比较多，
# 包括数据维度、列名称、数据格式和所占空间等信息。
print(df.info())
# 3. 查看数据格式
# Excel中通过选中单元格并查看开始菜单中的数值类型来判断数
# 据的格式。Python中使用dtypes函数来返回数据格式。
# Dtypes是一个查看数据格式的函数，可以一次性查看数据表中所
# 有数据的格式，也可以指定一列来单独查看。
print(df.dtypes)
# 4. 查看空值
# Excel中查看空值的方法是使用“定位条件”功能对数据表中的空
# 值进行定位。“定位条件”在“开始”目录下的“查找和选择”目录中。
# Isnull是Python中检验空值的函数，返回的结果是逻辑值，包含空
# 值返回True，不包含则返回False。用户既可以对整个数据表进行检
# 查，也可以单独对某一列进行空值检查。
print(df.isnull())
# 5. 查看唯一值(去除重复）
# Excel中查看唯一值的方法是使用“条件格式”对唯一值进行颜色
# 标记。Python中使用unique函数查看唯一值。
# Unique是查看唯一值的函数，只能对数据表中的特定列进行检
# 查。下面是代码，返回的结果是该列中的唯一值。类似与Excel中删
# 除重复项后的结果。
print(df['city'].unique())
# 6. 查看数据表数值
# Python中的Values函数用来查看数据表中的数值。以数组的形式
# 返回，不包含表头信息。
print(df.values)
# 7. 查看列名称
# Columns函数用来单独查看数据表中的列名称。
print(df.columns)
# 8. 查看前10行数据
# Head函数用来查看数据表中的前N行数据，默认head()显示前10
# 行数据，可以自己设置参数值来确定查看的行数。下面的代码中设置
# 查看前3行的数据。
# 查看前3行数据
print(df.head(3))
# 9. 查看后10行数据
# Tail行数与head函数相反，用来查看数据表中后N行的数据，默认
# tail()显示后10行数据，可以自己设置参数值来确定查看的行数。下面
# 的代码中设置查看后3行的数据。
# 查看最后3行
print(df.tail(3))

