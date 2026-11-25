import matplotlib.pyplot as plt
import pandas as pd

# Etapa 1: importação da base limpa da atividade 01
try:
    pinguins_biscoe = pd.read_csv("jonatan_portes_pinguins_biscoe.csv")
    print(pinguins_biscoe.head())

    # Etapa 2: pergunta: na ilha Biscoe, qual espécie de pinguim é mais pesada?
    massa_por_especie = pinguins_biscoe.groupby("species")["body_mass_g"].mean()
    massa_por_especie = massa_por_especie.sort_values(ascending=False)
    print("\nMassa corporal média por espécie (g):")
    print(massa_por_especie.round(2))

    # Etapa 3: gráfico de barras com título, rótulos e cores
    massa_por_especie.plot(kind="bar", figsize=(7, 5), color=["#2a9d8f", "#e9c46a"])
    plt.title("Massa Corporal Média dos Pinguins da Ilha Biscoe", fontsize=14)
    plt.xlabel("Espécie")
    plt.ylabel("Massa Corporal Média (g)")
    plt.xticks(rotation=0)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print("Erro: Rode a atividade 01 antes para gerar a base limpa.")
