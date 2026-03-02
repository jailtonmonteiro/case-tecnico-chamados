# %%
import pandas as pd

base =  pd.read_csv("../data/raw/base_chamados.csv", sep=";")
base.head()
# %%
base.info()
# %%
base.groupby(by="empresa", as_index=False).count()

# %%
base.info()

# %%
base["data_fechamento"].min()
# %%
base["data_fechamento"].max()
# %%
base.groupby(by="setor").count()
# %%
base.groupby(by="categoria").count()

# %%
base.groupby(by="status").count()
# %%
base.describe(include="all")
# %%
base.isna().sum()
# %%
base.duplicated().sum()
# %%
base.info()
# %%
len(base.columns)
# %%
base["data_fechamento"].dropna()
