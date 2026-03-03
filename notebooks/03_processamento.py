# %%
import pandas as pd
base = pd.read_csv("../data/processed/base_tratada.csv", sep=";", parse_dates=["data_abertura", "data_fechamento"])
base.info()
# %%
base["tempo_atendimento_dias"] = (base["data_fechamento"] - base["data_abertura"]).dt.days
# %%
base["sla_cumprido"] = base["tempo_atendimento_dias"] > 3
# %%
base.info()
# %%
