from load_csv import *
from load_postgresql import *

while True:
    for ind in range(0, 7):
        if ind == 0:
            city = "recife pernambuco"
            print("===========================================================================")
            print("[SYSTEM LOGGING] CSV BACKUP:")
            load_csv(city)
            print("[SYSTEM LOGGING] POSTGRE DATABASE:")
            load_postgresql(city)
        elif ind == 1:
            city = "caruaru pernambuco"
            print("===========================================================================")
            print("[SYSTEM LOGGING] CSV BACKUP:")
            load_csv(city)
            print("[SYSTEM LOGGING] POSTGRE DATABASE:")
            load_postgresql(city)
        elif ind == 2:
            city = "arcoverde pernambuco"
            print("===========================================================================")
            print("[SYSTEM LOGGING] CSV BACKUP:")
            load_csv(city)
            print("[SYSTEM LOGGING] POSTGRE DATABASE:")
            load_postgresql(city)
        elif ind == 3:
            city = "serra talhada pernambuco"
            print("===========================================================================")
            print("[SYSTEM LOGGING] CSV BACKUP:")
            load_csv(city)
            print("[SYSTEM LOGGING] POSTGRE DATABASE:")
            load_postgresql(city)
        elif ind == 4:
            city = "salgueiro pernambuco"
            print("===========================================================================")
            print("[SYSTEM LOGGING] CSV BACKUP:")
            load_csv(city)
            print("[SYSTEM LOGGING] POSTGRE DATABASE:")
            load_postgresql(city)
        elif ind == 5:
            city = "ouricuri pernambuco"
            print("===========================================================================")
            print("[SYSTEM LOGGING] CSV BACKUP:")
            load_csv(city)
            print("[SYSTEM LOGGING] POSTGRE DATABASE:")
            load_postgresql(city)
        elif ind == 6:
            city = "petrolina pernambuco"
            print("===========================================================================")
            print("[SYSTEM LOGGING] CSV BACKUP:")
            load_csv(city)
            print("[SYSTEM LOGGING] POSTGRE DATABASE:")
            load_postgresql(city)
        else:
            print("[SYSTEM]: Configuration Looping Error!")
            pass