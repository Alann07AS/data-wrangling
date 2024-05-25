import pandas as pd
import numpy as np

def winsorize(df, quantiles):
    """
    df: pd.DataFrame
    quantiles: list
        ex: [0.05, 0.95]
    """
    lower_limit, upper_limit = np.quantile(df, quantiles)
    print(lower_limit, upper_limit)
    return df.clip(lower_limit, upper_limit)

df = pd.DataFrame(range(1,11), columns=['sequence'])
print(winsorize(df, [0.20, 0.80]).to_markdown())


groups = np.concatenate([np.ones(10), np.ones(10)+1,  np.ones(10)+2, np.ones(10)+3, np.ones(10)+4])

df = pd.DataFrame(data= zip(groups,
                            range(1,51)),
                columns=["group", "sequence"])

# # Group by 'group' and apply winsorize to each group
df_grouped_winsorized = df.groupby('group')['sequence'].apply(lambda x: winsorize(x, [0.05, 0.95]))

print(df_grouped_winsorized)
