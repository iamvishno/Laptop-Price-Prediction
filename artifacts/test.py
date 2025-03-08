import pandas as pd
df = pd.read_csv('train.csv')

cat = df.select_dtypes(include='object').columns
num = df.select_dtypes(exclude='object').columns
d = {}
for colum in cat:
    d[colum] = df[colum].unique()
print(df.columns)

