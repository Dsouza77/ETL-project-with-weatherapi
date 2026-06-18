import psycopg2
from transform import *
import pprint

def load_postgresql(nome):
    try:
        data = get_transform(nome)
        try:
            conn = psycopg2.connect(
                host='localhost',
                database='AtmosFlow',
                user='postgres',
                password='1235'
            )
        except Exception as Connect_Error:
            print(f"[SYSTEM]: Database connection error, context: {Connect_Error}")
        
        try:
            with conn:
                with conn.cursor() as cursor:
                    query = """
                    INSERT INTO weather_data (cidade, estado, horario,
                    data_coleta, clima, desc_temp, temperatura, umidade,
                    pressao_atm, cob_nuvens, veloc_vento, precip_chuva_mm,
                    chance_chuva, ponto_orvalho, uv, rajada_vento_kph,
                    condicao_clim, score
                    )
                    VALUES (
                        %(Nome)s, %(Estado)s, %(Hora)s, %(Data)s, %(Clima)s, 
                        %(Desc_temperatura)s, %(Temperatura)s, %(Humidade)s, %(Pressao_at)s, %(Cob_nuvens)s, 
                        %(Velo_vento_kmh)s, %(Precipitacao)s, %(Chance_chuva)s, %(Ponto_orvalho)s, %(UV)s, 
                        %(Vel_raj_vento)s, %(Cod_cond_climatica)s, %(Score)s
                    );
                    """
                    cursor.execute(query, data)
                    conn.commit()
                    cursor.close()
                    print("[SYSTEM]: Data entry completed successfully!")
        except Exception as Insert_Error:
            print(f"[SYSTEM]: Insertion Error, context: {Insert_Error}")
        conn.close()
    except Exception as Error:
        print(f"[SYSTEM]: System error, context: {Error}")