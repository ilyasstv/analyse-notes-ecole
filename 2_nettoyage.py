import pandas as pd

df_etudiant = pd.read_csv("./data/etudiants.csv")
df_modules = pd.read_csv("./data/modules.csv")
df_notes = pd.read_csv("./data/notes.csv")

df_etudiant["ville"] = df_etudiant["ville"].str.strip().str.title()
df_etudiant = df_etudiant.drop_duplicates()
df_etudiant["ville"] = df_etudiant["ville"].fillna("Inconnue")
df_notes = df_notes.drop_duplicates()
df_notes["note"] = pd.to_numeric(df_notes["note"], errors="coerce")
df_notes = df_notes.dropna()
df_notes = df_notes[(df_notes["note"] >= 0)& (df_notes["note"] <= 20)]

print(len(df_etudiant))
print(len(df_notes))
print(df_etudiant["ville"].unique())

df_etudiant.to_csv("./data/etudiants_clean.csv" , index= False)
df_notes.to_csv("./data/notes_clean.csv" , index= False)

