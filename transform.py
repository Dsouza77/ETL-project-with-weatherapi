import pandas as pd
from extract import *
from datetime import datetime
from zoneinfo import ZoneInfo

def get_transform(name):
    try:
        data = get_request(name)
        nome = data["location"]["name"] #nome da cidade
        state = data["location"]["region"] #estado
        #time_local = data["location"]["localtime"][11:16] #horário puxado pela API
        time_local = str(datetime.now(tz=ZoneInfo("America/Sao_Paulo")))[11:19] #horario puxado pelo datetime (horario real)
        date = data['current']["last_updated"][:10] #data último atualização
        climate = data["current"]["condition"]["text"] #descrição do clima
        temp = data["current"]["temp_c"] #temperatura em celsius
        if temp < 18:
            desc_temp = "Frio"
        elif temp >= 18 and temp <= 28:
            desc_temp = "Ameno"
        else:
            desc_temp = "Quente"
        humidity = float(data["current"]["humidity"]) #humidade do ar (%)
        pressure_mb = float(data["current"]["pressure_mb"]) #pressão atmosférica
        cloud = float(data["current"]["cloud"]) #porcentagem cobertura nuvens (%)
        wind_kph = data["current"]["wind_kph"] #velocidade vento km/h
        precip_mm = float(data["current"]["precip_mm"]) #quantidade precipitação chuva em mm
        chance_of_rain = data["current"]["chance_of_rain"] #chance de chuva (%)
        dewpoint_c = float(data["current"]["dewpoint_c"]) #ponto de orvalho em celsius
        uv = data["current"]["uv"] #índice UV
        gust_kph = data["current"]["gust_kph"] #velocidade rajadas de vento km/h
        condition = data["current"]["condition"]["code"] #codigo numerico condição climatica
        #print(name, state, time_local, date, climate, temp, humidity, pressure_mb, cloud, wind_kph, precip_mm, chance_of_rain, dewpoint_c, uv, gust_kph, condition)
        
        score = humidity * 0.4
        score += cloud * 0.3
        score += precip_mm * 2
        score += dewpoint_c * 0.2
        score -= (pressure_mb - 1025) * 0.25
        score = float(f"{score:.2f}")
        if score >= 100:
            score == 100
        if score < 0:
            score == 0

        data = {
            "Nome":nome,
            "Estado":state,
            "Hora":time_local,
            "Data":date,
            "Clima":climate,
            "Temperatura":temp,
            "Desc_temperatura":desc_temp,
            "Humidade":humidity,
            "Pressao_at":pressure_mb,
            "Cob_nuvens":cloud,
            "Velo_vento_kmh":wind_kph,
            "Precipitacao":precip_mm,
            "Chance_chuva":chance_of_rain,
            "Ponto_orvalho":dewpoint_c,
            "UV":uv,
            "Vel_raj_vento":gust_kph,
            "Cod_cond_climatica":condition,
            "Score":score
            }
        print("[SYSTEM]: Data transform successfully!")
        return data
    except Exception as Error:
        print(f"[SYSTEM]: Transform Error, code: {Error}")