# %%
import pandas as pd
base = pd.read_csv("../data/raw/base_chamados.csv", sep=";")
base.head()

# %%
base = base.drop_duplicates(subset=["id_chamado"])
# %%
base = base.dropna(subset="data_fechamento")
# %%
base["tecnico_responsavel"] = base["tecnico_responsavel"].fillna("nao_atribuido")
# %%
base["data_fechamento"] = pd.to_datetime(
    base["data_fechamento"],
    format='mixed',
)
# %%
base["data_abertura"] = pd.to_datetime(
    base["data_abertura"],
    format='mixed'
)
# %%
filtro = base["data_abertura"] < base["data_fechamento"]
base = base[filtro]
# %%
base["empresa"] = base["empresa"].str.lower().str.replace(" ", "_")
base["setor"] = base["setor"].str.lower()
base["categoria"] = base["categoria"].str.lower().str.replace(" ", "_")
base["prioridade"] = base["prioridade"].str.lower()
base["status"] = base["status"].str.lower()
base["tecnico_responsavel"] = base["tecnico_responsavel"].str.lower()
# %%
base.to_csv("../data/processed/base_tratada.csv", sep=";")
