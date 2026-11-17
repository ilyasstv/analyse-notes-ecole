import pandas as pd 

df_etudiants = pd.read_csv("./data/etudiants.csv")
df_modules = pd.read_csv("./data/modules.csv")
df_notes = pd.read_csv("./data/notes.csv")

print("===== ETUDIANTS =====")
print(len(df_etudiants))
print(df_etudiants.head())
print(df_etudiants.isna().sum())
print(df_etudiants.duplicated().sum())
print()

print("===== NOTES =====")
print(len(df_notes))
print(df_notes.head())
print(df_notes.isna().sum())
print(df_notes.duplicated().sum())
print()

print("===== modules =====")
print(len(df_modules))
print(df_modules.head())
print(df_modules.isna().sum())
print(df_modules.duplicated().sum())
print()

print(df_notes["note"].unique())



