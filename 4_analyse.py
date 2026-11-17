import pandas as pd
import matplotlib.pyplot as plt
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["ecole"]

pipline = [ { "$group" : {"_id":"$id_module" , "moyenne" :{ "$avg":"$note"}}} , { "$lookup" : {"from":"modules" , "localField":"_id" , "foreignField" : "id_module" , "as":"infos"}} , { "$unwind" : "$infos" } , {"$project" :{"_id":0 , "nom_module" :"$infos.module" , "moyenne":{"$round":["$moyenne",2]}}},{"$sort":{"moyenne":-1}} ]

resultat = list(db["notes"].aggregate(pipline))
print(resultat)
df = pd.DataFrame(resultat)
print(df)

plt.bar(df["nom_module"], df["moyenne"])
plt.title("Moyenne par Module")
plt.axhline(10, color="red")
plt.savefig("moyenne_module_2.png")
plt.show()
