agenda_telefonica = {
    "Adriana Silva": "(11) 98888-0001",
    "Bruno Medeiros": "(21) 97777-0002",
    "Camila Oliveira": "(31) 96666-0003",
    "Diego Santos": "(41) 95555-0004",
    "Elena Ribeiro": "(51) 94444-0005",
    "Felipe Costa": "(61) 93333-0006",
    "Gabriel Almeida": "(71) 92222-0007",
    "Heloísa Fernandes": "(81) 91111-0008",
    "Ícaro Carvalho": "(85) 90000-0009",
    "Julia Martins": "(91) 98765-0010",
    "Lucas Pereira": "(19) 97654-0011",
    "Mariana Souza": "(47) 96543-0012",
    "Natália Lima": "(62) 95432-0013",
    "Otávio Gomes": "(84) 94321-0014",
}

print(agenda_telefonica.get("Chai", "Contato não encontrado"))

agenda_telefonica["Chai"] = "(11) 99123-4567"
print(agenda_telefonica)
print(agenda_telefonica.get("Chai", "Contato não encontrado"))

agenda_telefonica.pop("Elena Ribeiro", None)
print(agenda_telefonica)
