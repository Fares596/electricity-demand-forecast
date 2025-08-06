import pandas as pd
from utils.preprocessing import preprocess_conso_elec

# 1. Charger les données brutes
raw_df = pd.read_csv("data/rte_consommation_electrique_30min_fr.csv", delimiter= ";")

print(print("Colonnes disponibles :", raw_df.columns.tolist())
      )
# 2. Appliquer le préprocessing
df_clean = preprocess_conso_elec(raw_df)

# 3. Sauvegarder les données prétraitées
df_clean.to_csv("data/df_preprocessed.csv")
print("Données sauvegardées dans data/df_preprocessed.csv")
