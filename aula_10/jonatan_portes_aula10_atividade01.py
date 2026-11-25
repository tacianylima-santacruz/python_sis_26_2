import csv
import json

# Etapa 1: dicionário com as configurações do cluster
cluster = {
    "nome_cluster": "cluster-producao",
    "versao_so": "Ubuntu Server 24.04",
    "servidores": [
        {"nome": "srv-app-01", "ip": "192.168.1.10", "portas": [80, 443]},
        {"nome": "srv-db-01", "ip": "192.168.1.20", "portas": [3306, 22]},
        {"nome": "srv-web-01", "ip": "192.168.1.30", "portas": [80, 443, 22]}
    ]
}

# Etapa 2: exportação para JSON
try:
    with open("cluster_config.json", "w", encoding="utf-8") as arquivo_json:
        json.dump(cluster, arquivo_json, indent=4)
    print("Arquivo cluster_config.json criado com sucesso!")

except PermissionError:
    print("Erro: Sem permissão para criar o arquivo JSON.")

# Etapa 3: exportação para CSV usando ; como delimitador
try:
    with open("servidores_cluster.csv", "w", newline="", encoding="utf-8") as arquivo_csv:
        escritor = csv.writer(arquivo_csv, delimiter=";")
        escritor.writerow(["Servidor", "IP", "Portas"])

        for servidor in cluster["servidores"]:
            portas = []
            for porta in servidor["portas"]:
                portas.append(str(porta))
            portas_texto = ", ".join(portas)
            escritor.writerow([servidor["nome"], servidor["ip"], portas_texto])

    print("Arquivo servidores_cluster.csv criado com sucesso!")

except PermissionError:
    print("Erro: Sem permissão para criar o arquivo CSV.")
