import pandas as pd

def preprocess_conso_elec(df):
    """
    Nettoie et prépare les données de consommation électrique pour la modélisation.

    Paramètres :
        df (pd.DataFrame) : Le DataFrame brut contenant une colonne 'Date - Heure' et 'Consommation brute électricité (MW) - RTE'

    Retour :
        pd.DataFrame : Données prétraitées avec colonnes temporelles et index datetime
    """
    # 1. Convertir les dates
    df['date_heure'] = pd.to_datetime(df['Date - Heure'], errors='coerce')
    df = df.dropna(subset=['date_heure'])

    # 2. Supprimer les fuseaux horaires s'il y en a
    df['date_heure'] = df['date_heure'].apply(lambda x: x.replace(tzinfo=None) if x.tzinfo else x)

    # 3. Mettre en index
    df = df.set_index('date_heure')
    df = df.sort_index()

    # 4. Renommer la target pour plus de clarté
    df = df.rename(columns={'Consommation brute électricité (MW) - RTE': 'conso_elec_MW'})

    # 5. Garder uniquement la colonne cible
    df = df[['conso_elec_MW']]

    # 6. Interpolation des valeurs manquantes
    df['conso_elec_MW'] = df['conso_elec_MW'].interpolate(method='time')

    # 7. Création de features temporelles
    df['hour'] = df.index.hour
    df['dayofweek'] = df.index.dayofweek
    df['month'] = df.index.month
    df['is_weekend'] = df['dayofweek'].isin([5, 6]).astype(int)

    df['is_working_hour'] = df['hour'].between(9, 18).astype(int)

    print(f"[INFO] PREPROCESSED DATA : {df.shape[0]} lignes, de {df.index.min()} à {df.index.max()}")

    return df
