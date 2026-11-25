# Etapa 1: importações seguindo a ordem da PEP 8
# 1. Padrão nativo
import os
import xml.etree.ElementTree as ET

# 2. Terceiros (no Colab: !pip install openpyxl)
from openpyxl import Workbook
from openpyxl.styles import Font

# Etapa 2: criação da pasta com 3 notas fiscais simuladas (código da professora)
os.makedirs("notas_xml", exist_ok=True)

notas_amostra = [
    {"num": "1001", "data": "2026-10-10", "fornecedor": "Tech Solutions LTDA", "cnpj": "12.345.678/0001-90", "total": "4500.00"},
    {"num": "1002", "data": "2026-10-12", "fornecedor": "Cloud Cloud Servicos", "cnpj": "98.765.432/0001-11", "total": "1280.50"},
    {"num": "1003", "data": "2026-10-15", "fornecedor": "Hardware & Redes SA", "cnpj": "45.123.890/0001-55", "total": "8900.00"}
]

# O "&" do nome "Hardware & Redes SA" quebra o XML, por isso troquei por "&amp;"
for n in notas_amostra:
    conteudo = f"""<?xml version="1.0" encoding="UTF-8"?>
<nfeProc xmlns="http://www.portalfiscal.inf.br/nfe">
    <NFe>
        <infNFe>
            <ide>
                <nNF>{n['num']}</nNF>
                <dhEmi>{n['data']}T14:30:00-03:00</dhEmi>
            </ide>
            <emit>
                <CNPJ>{n['cnpj']}</CNPJ>
                <xNome>{n['fornecedor'].replace('&', '&amp;')}</xNome>
            </emit>
            <total>
                <ICMSTot>
                    <vNF>{n['total']}</vNF>
                </ICMSTot>
            </total>
        </infNFe>
    </NFe>
</nfeProc>"""
    with open(f"notas_xml/nfe_{n['num']}.xml", "w", encoding="utf-8") as f:
        f.write(conteudo)

print("Amostras criadas na pasta 'notas_xml'!")

# A NF-e usa namespace, então as tags são buscadas com o prefixo "nfe"
namespace = {"nfe": "http://www.portalfiscal.inf.br/nfe"}
pasta = "notas_xml"
notas = []

# Etapa 3: leitura de cada arquivo e extração dos dados
for nome_arquivo in os.listdir(pasta):
    if not nome_arquivo.endswith(".xml"):
        continue

    caminho = os.path.join(pasta, nome_arquivo)

    try:
        arvore = ET.parse(caminho)
        raiz = arvore.getroot()

        numero = raiz.find(".//nfe:ide/nfe:nNF", namespace).text
        data_emissao = raiz.find(".//nfe:ide/nfe:dhEmi", namespace).text[:10]
        fornecedor = raiz.find(".//nfe:emit/nfe:xNome", namespace).text
        cnpj = raiz.find(".//nfe:emit/nfe:CNPJ", namespace).text
        valor_total = float(raiz.find(".//nfe:ICMSTot/nfe:vNF", namespace).text)

        notas.append([numero, data_emissao, fornecedor, cnpj, valor_total])
        print(f"Nota {numero} lida com sucesso.")

    except ET.ParseError:
        print(f"Erro: O arquivo {nome_arquivo} não é um XML válido.")

    except AttributeError:
        print(f"Erro: Faltam informações na nota {nome_arquivo}.")

    except ValueError:
        print(f"Erro: Valor total inválido na nota {nome_arquivo}.")

# Etapa 4: geração da planilha com o valor formatado em duas casas decimais
wb = Workbook()
ws = wb.active
ws.title = "Notas Fiscais"

ws.append(["Número", "Data de Emissão", "Fornecedor", "CNPJ", "Valor Total (R$)"])

for celula in ws[1]:
    celula.font = Font(bold=True)

for numero, data_emissao, fornecedor, cnpj, valor_total in notas:
    ws.append([numero, data_emissao, fornecedor, cnpj, f"{valor_total:.2f}"])

wb.save("notas_fiscais.xlsx")
print(f"Planilha notas_fiscais.xlsx salva com {len(notas)} notas.")
