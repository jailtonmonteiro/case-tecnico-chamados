# %%
import pandas as pd
base = pd.read_csv("../data/processed/base_tratada.csv", sep=";", parse_dates=["data_abertura", "data_fechamento"])
base.info()
# %%
base["tempo_atendimento_dias"] = (base["data_fechamento"] - base["data_abertura"]).dt.days
# %%
def sla(linha):
    if linha["tempo_atendimento_dias"] <= 3 and linha["status"] == "fechado":
        return True
    else:
        return False

# %%
base["sla_cumprido"] = base.apply(sla, axis=1)
# %%
base.groupby("empresa").size()
# %%
base.groupby("sla_cumprido").size()
# %%
base.groupby("tecnico_responsavel").size()
# %%
base.groupby(["status", "empresa"]).size()
# %%
base
