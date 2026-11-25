# Etapa 1: instalação (no Colab: !pip install openpyxl)
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill

wb_inventario = Workbook()
ws_inventario = wb_inventario.active
ws_inventario.title = "Servidores"

ws_inventario.append(["Hostname", "IP", "Memória (GB)", "Uso de Disco (%)", "Status"])

for celula in ws_inventario[1]:
    celula.font = Font(bold=True)

servidores = [
    ["srv-app-01", "192.168.1.10", 16, 45, "Ativo"],
    ["srv-db-01", "192.168.1.20", 64, 92, "Ativo"],
    ["srv-web-01", "192.168.1.30", 8, 80, "Manutenção"],
    ["srv-backup-01", "192.168.1.40", 32, 60, "Ativo"]
]

for servidor in servidores:
    ws_inventario.append(servidor)

# Etapa 2: destaque e alerta para disco com uso igual ou acima de 80%
for linha in range(2, ws_inventario.max_row + 1):
    celula_disco = ws_inventario.cell(row=linha, column=4)

    if celula_disco.value >= 80:
        celula_disco.fill = PatternFill(
            start_color="FF9999",
            end_color="FF9999",
            fill_type="solid"
        )
        hostname = ws_inventario.cell(row=linha, column=1).value
        print(f"Alerta: o servidor {hostname} precisa de expansão de armazenamento "
              f"({celula_disco.value}% de disco em uso).")

wb_inventario.save("inventario_servidores.xlsx")
print("Planilha inventario_servidores.xlsx salva com sucesso!\n")

# Criação do log.txt da aula 09
with open("log.txt", "w", encoding="utf-8") as log:
    log.write("""2026-10-14 08:30:15 - INFO - Sistema inicializado com sucesso
2026-10-14 08:31:02 - INFO - Usuario 'admin' realizou login
2026-10-14 08:35:22 - AVISO - Tentativa de acesso com senha incorreta: usuario 'bat'
2026-10-14 08:35:40 - SUCESSO - Usuario 'bat' realizou login
2026-10-14 08:40:11 - ERRO - Falha ao conectar ao banco de dados: timeout
2026-10-14 08:42:00 - INFO - Conexao reestabelecida
""")

# Etapa 3: abertura do log e extração do nível de cada evento
registros = []

try:
    with open("log.txt", "r", encoding="utf-8") as arquivo_log:
        for linha in arquivo_log:
            partes = linha.strip().split(" - ")

            if len(partes) == 3:
                data_hora, tipo_evento, mensagem = partes
                registros.append([data_hora, tipo_evento, mensagem])
                print(f"{tipo_evento}: {mensagem}")

except FileNotFoundError:
    print("Erro: O arquivo log.txt não foi encontrado.")

# Etapa 4: planilha separada com os eventos do log
wb_logs = Workbook()
ws_logs = wb_logs.active
ws_logs.title = "Auditoria"

ws_logs.append(["Data/Hora", "Tipo de Evento", "Mensagem"])

for celula in ws_logs[1]:
    celula.font = Font(bold=True)

for registro in registros:
    ws_logs.append(registro)

wb_logs.save("auditoria_logs.xlsx")
print(f"\nPlanilha auditoria_logs.xlsx salva com {len(registros)} eventos.")
