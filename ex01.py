import pandas as pd

df1 = pd.DataFrame([['a', 1], ['b', 2]],
                   columns=['letter', 'number'])
df2 = pd.DataFrame([['c', 1], ['d', 2]],
                   columns=['letter', 'number'])

concat = pd.concat([df1, df2], ignore_index=True)

print(concat)