#  Electricity Demand Forecast - RTE (France)

This project focuses on forecasting the **electricity consumption in France** one day in advance using open data from the French electricity transmission operator, **RTE**. The goal is to demonstrate applied skills in **time series forecasting**, **feature engineering**, and **machine learning pipelines**.

---

##  Project Objectives

- Predict electricity consumption **24 hours ahead**
- Explore and compare different modeling approaches
- Build a **clean and reusable preprocessing pipeline**

---

##  Dataset

- **Source**: [Open Data RTE (Opendatasoft)](https://data.opendatasoft.com/explore/dataset/consommation-quotidienne-brute%40reseaux-energies-rte/)
- **Format**: 30-minute resolution
- **Time range**: From 2012 to 2025
- **Target column**: `Consommation brute électricité (MW) - RTE`

---

##  Data Preprocessing

Implemented in `utils/preprocessing.py`:

- Convert timestamps and remove timezone info
- Interpolate missing values
- Generate time-based features (`hour`, `dayofweek`, `month`, `is_weekend`)
- Add a **target column shifted by 24 hours** (`conso_j1`) (to be done)
- Create multiple **lag features**: [1, 2, 3, 6, 12, 24, 48, 96] intervals (30-min steps)

Cleaned data is saved to: `data/df_preprocessed.csv`

---

##  Modeling

Notebook: `notebook/modelisation.ipynb`

### Models used:

- Linear Regression (baseline)
- Random Forest Regressor
- XGBoost Regressor

### Evaluation:

- Metrics: RMSE, R² score
- Chronological train/test split (80% train / 20% test)
- Visual comparison between actual and predicted values

---