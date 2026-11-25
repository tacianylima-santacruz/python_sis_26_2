# 1. Padrão nativo
import json

# 2. Terceiros
import matplotlib.pyplot as plt
import pandas as pd

try:
    with open("clima_cidades.json", "r", encoding="utf-8") as arquivo:
        resultados = json.load(arquivo)

except FileNotFoundError:
    print("Erro: Rode a atividade 01 antes para gerar o clima_cidades.json.")
    resultados = []

if resultados:
    # Etapa 1: lista de dicionários para DataFrame, com as colunas em português
    df_clima = pd.json_normalize(resultados, sep="_")

    colunas = {
        "location_name": "Cidade",
        "location_region": "Estado",
        "location_localtime": "Data_Hora",
        "current_temp_c": "Temperatura_C",
        "current_feelslike_c": "Sensacao_Termica_C",
        "current_humidity": "Umidade_Pct",
        "current_condition_text": "Condicao"
    }
    df_tratado = df_clima[list(colunas.keys())].rename(columns=colunas)

    # Etapa 2: tratamento e tipagem
    df_tratado = df_tratado.drop_duplicates(subset=["Cidade"])
    df_tratado["Data_Hora"] = pd.to_datetime(df_tratado["Data_Hora"], errors="coerce")
    df_tratado["Temperatura_C"] = pd.to_numeric(df_tratado["Temperatura_C"], errors="coerce")
    df_tratado["Sensacao_Termica_C"] = pd.to_numeric(df_tratado["Sensacao_Termica_C"], errors="coerce")
    df_tratado["Umidade_Pct"] = pd.to_numeric(df_tratado["Umidade_Pct"], errors="coerce")

    print(df_tratado)
    df_tratado.info()
    print("\n--- RESUMO ESTATÍSTICO ---")
    print(df_tratado.describe())

    # Etapa 3: pergunta: em quais cidades a sensação térmica fica longe da temperatura real?
    df_grafico = df_tratado.set_index("Cidade")[["Temperatura_C", "Sensacao_Termica_C"]]

    ax = df_grafico.plot(kind="bar", figsize=(10, 5), color=["#1d3557", "#e76f51"])
    ax.set_title("Temperatura Real x Sensação Térmica nas Capitais", fontsize=14)
    ax.set_xlabel("Cidade", fontsize=12)
    ax.set_ylabel("Graus (°C)", fontsize=12)
    ax.legend(["Temperatura real", "Sensação térmica"])
    plt.xticks(rotation=45, ha="right")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

    df_tratado.to_csv("jonatan_portes_clima_tratado.csv", index=False, encoding="utf-8")
    print("Arquivo jonatan_portes_clima_tratado.csv exportado com sucesso!")
