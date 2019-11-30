import pandas as pd
import numpy as np

# 创建数据表
# 另一种方法是通过直接写入数据来生成数据表，Excel中直接在
# 单元格中输入数据就可以，Python中通过下面的代码来实现。生成数
# 据表的函数是pandas库中的DateFrame函数，数据表一共有6行数据，
# 每行有6个字段。在数据中我们特意设置了一些NA值和有问题的字
# 段，例如包含空格等。后面将在数据清洗步骤进行处理。后面我们将
# 统一以DataFrame的简称df来命名数据表。
df = pd.DataFrame({"id": [1001, 1002, 1003, 1004, 1005, 1006],
                   "date": pd.date_range('20130102', periods=6),
                   "city": ['Beijing ', 'SH', ' guangzhou ', 'Shenzhen', 'shanghai', 'BEIJING '],
                   "age": [23, 44, 54, 32, 34, 32], "category": ['100-A', '100-B', '110-A', '110-C', '210-A', '130-F'],
                   "price": [1200, np.nan, 2133, 5433, np.nan, 4432]},
                  columns=['id', 'date', 'city', 'category', 'age', 'price'])


# 默认读取前5行的数据
data = df.head()

print(data)
