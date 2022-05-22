import pandas as pd
import glob

folder_path = '../Resources/lactancia_historica'
file_list = glob.glob(folder_path + "/*.csv")
print(file_list)

import sys
def calculate_lacta(df):
    out = []
    for id in df["id"].unique():
        id_df=df[(df.id==id)]
        lactancias = list(id_df['lactation'].unique())
        for lacta in lactancias:
            vaca = {}
            vaca['id'] = str(id)
            vaca['lacta'] = lacta
            df_lactancia=id_df[(id_df.lactation==lacta)]
            print(df_lactancia)
            print('==================================================')
            total_produccion = df_lactancia['daily_production'].sum()
            dias_leche = df_lactancia.iloc[-1]['milk_days']
            print(dias_leche)
            vaca['lactation_total'] = str(total_produccion)
            vaca['milk_days'] = str(dias_leche)
            out.append(vaca)
    return out

df = pd.DataFrame()
for i in range(len(file_list)):
    print(file_list[i])
    data = pd.read_csv(file_list[i])
    data.columns = ["id", "date", "lactation", "milk_days", "daily_production"]
    res = calculate_lacta(data)

    res=pd.DataFrame.from_dict(res, orient='columns')
    res.columns = ["id", "lactation","daily_production", "milk_days"]
    df = pd.concat([df,res])

df = df.to_dict('records')
print('export')
import json
# Serializing json 
json_object = json.dumps(df, indent = 4)
# Writing to sample.json
with open("../Resources/full.json", "w") as outfile:
    outfile.write(json_object)
