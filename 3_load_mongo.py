import pandas as pd
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

df_etudiants = pd.read_csv("data/etudiants_clean.csv")
df_modules   = pd.read_csv("data/modules.csv")
df_notes     = pd.read_csv("data/notes_clean.csv")

try:
 client = MongoClient("mongodb://localhost:27017", serverSelectionTimeoutMs=3000)
 client.server_info()
 print("SERVER WORKING")

except ServerSelectionTimeoutError:
 print("SERVER OFF")
 exit()

db = client["ecole"]
col = db["etudiants"]
col.delete_many({})
col.insert_many(df_etudiants.to_dict("records"))
print("etudiants:", col.count_documents({}))

db = client["ecole"]
col_2 = db["notes"]
col_2.delete_many({})
col_2.insert_many(df_notes.to_dict("records"))
print("notes:", col_2.count_documents({}))

db = client["ecole"]
col_3 = db["modules"]
col_3.delete_many({})
col_3.insert_many(df_modules.to_dict("records"))
print("modules:", col_3.count_documents({}))


