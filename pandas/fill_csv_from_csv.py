import pandas as pd

df = pd.read_csv(path, sep = ',')
df2 = pd.read_csv(path, sep = ',')


df2 = df2[(df2['ADDRESS'] != 'БРЕНД') & (df2['ADDRESS'].notnull())]

uniq_id = [ str(i) for i in df['ID_COMP'].tolist()

c = 0
for i in range(len(df3)):
    if str(df2.loc[i]['ID_COMP']) not in uniq_id:
    x = len(df)
    df.loc[x] = ''
    df.loc[x] = df2.loc[i]
    uniq_id.append(str(df2.loc[i]['ID_COMP']))

print(c)


df = df.fillna(0)

df.to_csv(path, index=False)
