# Etapa 1: instalação (no Colab: !pip install openpyxl)
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill

# Etapa 2: criação da planilha com a aba de servidores
wb = Workbook()
ws = wb.active
ws.title = "Servidores"

ws.append(["Hostname", "IP", "Memória (GB)", "Uso de Disco (%)", "Status"])

for celula in ws[1]:
    celula.font = Font(bold=True)

# Etapa 3: inserção dos dados simulados
servidores = [
    ["srv-app-01", "192.168.1.10", 16, 45, "Ativo"],
    ["srv-db-01", "192.168.1.20", 64, 92, "Ativo"],
    ["srv-web-01", "192.168.1.30", 8, 80, "Manutenção"],
    ["srv-backup-01", "192.168.1.40", 32, 60, "Ativo"]
]

for servidor in servidores:
    ws.append(servidor)

# Etapa 4: avisos para disco com uso igual ou acima de 80%
for linha in range(2, ws.max_row + 1):
    celula_disco = ws.cell(row=linha, column=4)

    if celula_disco.value >= 80:
        celula_disco.fill = PatternFill(
            start_color="FF9999",
            end_color="FF9999",
            fill_type="solid"
        )
        hostname = ws.cell(row=linha, column=1).value
        print(f"Alerta: o servidor {hostname} está com {celula_disco.value}% de disco "
              f"e precisa de expansão de armazenamento.")

wb.save("inventario_servidores.xlsx")
print("Planilha inventario_servidores.xlsx salva com sucesso!")
