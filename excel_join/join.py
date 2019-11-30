import pandas  as pd
import numpy as np

# 读取
pf = pd.DataFrame(pd.read_excel('original.xls', sheet_name='Sheet1'))
print(pf.head(10))

# 读取
pf_person = pd.DataFrame(pd.read_excel('person.xls', sheet_name='Sheet1'))
print(pf_person.head(10))

pf_result = pd.merge(pf_person, pf, how='left', on=['name'])
print(pf_result.head(10))

# 写入
filepath = 'result.xls'
writer = pd.ExcelWriter(filepath)
pf_result.to_excel(excel_writer=writer, index=False, sheet_name='Sheet1')
# pf.to_excel(excel_writer=writer, sheet_name='表1')
writer.save()
writer.close()
