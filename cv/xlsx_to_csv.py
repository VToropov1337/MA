import pandas as pd


file = 'tools.xlsx'
xl = pd.ExcelFile(file)
print(xl.sheet_names)
df1 = xl.parse('Sheet')


df1.to_csv('tools.csv')
