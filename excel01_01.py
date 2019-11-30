import pandas as pd
import numpy as np

# 1. 导入数据表
# df = pd.DataFrame(pd.read_csv('lemon.csv', header=1))
# 这个会直接默认读取到这个Excel的第一个表单
df = pd.DataFrame(pd.read_excel('lemon.xlsx'))

# 默认读取前5行的数据
data = df.head()

print(data)
