# Etapa 1: importação e carga da base real (pinguins do arquipélago Palmer, Antártida)
import pandas as pd

url_base = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
dataframe_pinguins = pd.read_csv(url_base)
print("Base de dados carregada com sucesso!")

# Etapa 2: inspeção da base
print("\n--- Primeiras linhas ---")
print(dataframe_pinguins.head())

print("\n--- Informações da Base ---")
dataframe_pinguins.info()

print("\nValores nulos por coluna:")
print(dataframe_pinguins.isnull().sum())

# Linhas sem as medidas do pinguim não servem para a análise, então são removidas
dataframe_pinguins = dataframe_pinguins.dropna(subset=["body_mass_g"])

# Quando falta só o sexo, preencho com um valor padrão para não perder a linha
dataframe_pinguins["sex"] = dataframe_pinguins["sex"].fillna("NAO INFORMADO")

print("\nValores nulos depois do tratamento:")
print(dataframe_pinguins.isnull().sum())

# Etapa 3: filtro com apenas os pinguins da ilha Biscoe
pinguins_biscoe = dataframe_pinguins[dataframe_pinguins["island"] == "Biscoe"]
print(f"\nQuantidade de pinguins na ilha Biscoe: {len(pinguins_biscoe)}")
print(pinguins_biscoe[["species", "island", "body_mass_g", "sex"]].head())

pinguins_biscoe.to_csv("jonatan_portes_pinguins_biscoe.csv", index=False)
print("\nArquivo jonatan_portes_pinguins_biscoe.csv salvo com sucesso!")
