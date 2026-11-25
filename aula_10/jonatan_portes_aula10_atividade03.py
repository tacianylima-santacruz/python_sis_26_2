from openpyxl import Workbook
from openpyxl.styles import Font

# Etapa 1: abertura do log.txt da aula 09
linhas_log = []

try:
    with open("log.txt", "r", encoding="utf-8") as arquivo_log:
        linhas_log = arquivo_log.readlines()

except FileNotFoundError:
    print("Erro: O arquivo log.txt não foi encontrado.")

# Etapa 2: extração da data/hora, do nível do evento e da mensagem
registros = []

for linha in linhas_log:
    partes = linha.strip().split(" - ")

    if len(partes) == 3:
        data_hora, tipo_evento, mensagem = partes
        registros.append([data_hora, tipo_evento, mensagem])
        print(f"{tipo_evento}: {mensagem}")

# Etapa 3: criação da planilha com as colunas do log
wb = Workbook()
ws = wb.active
ws.title = "Auditoria"

ws.append(["Data/Hora", "Tipo de Evento", "Mensagem"])

for celula in ws[1]:
    celula.font = Font(bold=True)

# Etapa 4: preenchimento e gravação no diretório de execução
for registro in registros:
    ws.append(registro)

wb.save("auditoria_logs.xlsx")
print(f"Planilha auditoria_logs.xlsx salva com {len(registros)} eventos.")
