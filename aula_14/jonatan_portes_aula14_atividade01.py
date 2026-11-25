# API escolhida: WeatherAPI (clima atual por cidade)
# Documentação: https://www.weatherapi.com/docs/
# No Colab: !pip install requests (já vem instalado)

# 1. Padrão nativo
import json
from getpass import getpass

# 2. Terceiros
import requests

# Etapa 1: chave da API digitada na hora, sem ficar salva no código
API_KEY = getpass("Digite sua chave da WeatherAPI: ")
link_api = "http://api.weatherapi.com/v1/current.json"

cidades = [
    "Sao Paulo", "Rio de Janeiro", "Curitiba", "Porto Alegre", "Florianopolis",
    "Salvador", "Recife", "Manaus", "Belem", "Brasilia"
]

resultados = []

# Etapa 2: uma consulta para cada cidade da lista
for cidade in cidades:
    parametros = {"key": API_KEY, "q": cidade, "lang": "pt"}

    try:
        resposta = requests.get(link_api, params=parametros, timeout=10)
        print(f"{cidade}: status {resposta.status_code}")
        resposta.raise_for_status()

        # Etapa 3: resposta convertida para dicionário
        dados = resposta.json()
        print(f"Chaves principais: {list(dados.keys())}")
        resultados.append(dados)

    except requests.exceptions.HTTPError:
        # 400 costuma ser cidade inválida e 401/403 chave errada
        print(f"Erro na consulta de {cidade}: código {resposta.status_code}")

    except requests.exceptions.RequestException as erro:
        print(f"Falha de rede ao consultar {cidade}: {erro}")

print("\n--- CLIMA ATUAL ---")
for registro in resultados:
    nome = registro["location"]["name"]
    temperatura = registro["current"]["temp_c"]
    condicao = registro["current"]["condition"]["text"]
    print(f"{nome}: {temperatura} °C, {condicao}")

# Os resultados ficam salvos para a atividade 02 usar
with open("clima_cidades.json", "w", encoding="utf-8") as arquivo:
    json.dump(resultados, arquivo, indent=4)

print(f"\n{len(resultados)} cidades salvas em clima_cidades.json")
