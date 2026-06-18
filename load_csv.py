import pandas as pd
from transform import *
import os

def load_csv(name):
    try:
        if os.path.exists("data_backup.csv"):
            if os.path.getsize("data_backup.csv") >= 0 and os.path.getsize("data_backup.csv") <= 3:
                comparador = ["Nome","Estado","Hora","Data","Clima","Temperatura",
                            "Desc_temperatura","Humidade","Pressao_at","Cob_nuvens",
                            "Velo_vento_kmh","Precipitacao","Chance_chuva","Ponto_orvalho",
                            "UV","Vel_raj_vento","Cod_cond_climatica","Score"]
                cbc = pd.DataFrame(columns=comparador)
                cbc.to_csv("data_backup.csv", mode="w", index=False)
            elif os.path.getsize("data_backup.csv") > 0:
                indicador = pd.read_csv("data_backup.csv", nrows=0)
                comparador = ["Nome","Estado","Hora","Data","Clima","Temperatura",
                            "Desc_temperatura","Humidade","Pressao_at","Cob_nuvens",
                            "Velo_vento_kmh","Precipitacao","Chance_chuva","Ponto_orvalho",
                            "UV","Vel_raj_vento","Cod_cond_climatica","Score"]
                if list(indicador.columns) == comparador:
                    pass
                else:
                    cbc = pd.DataFrame(columns=comparador)
                    cbc.to_csv("data_backup.csv", mode="w", index=False)
        #a = get_transform("Recife")
        df = pd.DataFrame([get_transform(name)])
        df.to_csv("data_backup.csv", mode="a", header=not os.path.exists("data_backup.csv"), index=False)
        print("[SYSTEM]: Data saved in csv file backup successfully!")
    except Exception as Error:
        print(f"[SYSTEM]: Error loading CSV file, code: {Error}.")
#print(data)