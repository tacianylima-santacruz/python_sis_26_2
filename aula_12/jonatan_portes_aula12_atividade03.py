import matplotlib.pyplot as plt
import pandas as pd

# Etapa 1: leitura do CSV gerado na atividade 02
try:
    df_telemetria = pd.read_csv("telemetria_sistema.csv")
    print(df_telemetria)

    # Etapa 2: médias de CPU e RAM
    media_cpu = df_telemetria["Uso_CPU_Pct"].mean()
    media_ram = df_telemetria["Uso_RAM_Pct"].mean()

    print("\n--- RESUMO DA TELEMETRIA ---")
    print(f"Amostras coletadas: {len(df_telemetria)}")
    print(f"Média de uso da CPU: {media_cpu:.2f}%")
    print(f"Média de uso da RAM: {media_ram:.2f}%")

    # Etapa 3: gráfico de linha com CPU e RAM ao longo das iterações
    plt.figure(figsize=(8, 5))
    plt.plot(df_telemetria["Iteracao"], df_telemetria["Uso_CPU_Pct"],
             marker="o", color="navy", label="CPU (%)")
    plt.plot(df_telemetria["Iteracao"], df_telemetria["Uso_RAM_Pct"],
             marker="o", color="green", label="RAM (%)")
    plt.title("Uso de CPU e RAM por Iteração")
    plt.xlabel("Iteração")
    plt.ylabel("Uso (%)")
    plt.ylim(0, 100)
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print("Erro: Rode a atividade 02 antes para gerar o telemetria_sistema.csv.")
