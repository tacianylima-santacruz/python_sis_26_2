# No Colab: !pip install psutil
import time

import psutil

arquivo_csv = "telemetria_sistema.csv"

# Etapa 3: criação do arquivo com o cabeçalho antes da coleta
with open(arquivo_csv, "w", encoding="utf-8") as arquivo:
    arquivo.write("Iteracao,Uso_CPU_Pct,Uso_RAM_Pct\n")

print("Iniciando a coleta de métricas...")

# Etapa 2: 5 coletas com pausa de 1 segundo entre elas
for iteracao in range(1, 6):
    # Etapa 1: uso de CPU e memória RAM no momento
    uso_cpu = psutil.cpu_percent(interval=1.0)
    uso_ram = psutil.virtual_memory().percent

    print(f"Iteração {iteracao}: CPU {uso_cpu}% | RAM {uso_ram}%")

    # Etapa 4: cada amostra é gravada no modo de anexação
    with open(arquivo_csv, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{iteracao},{uso_cpu},{uso_ram}\n")

    time.sleep(1)

print(f"Coleta finalizada. Dados salvos em {arquivo_csv}.")
