pacotes = [12, 0, 25, 40, -1, 18, 50]

for num in pacotes:
    if num == 0:
        pass
    elif num < 0:
        print("Falha de segurança!")
        break
    else:
        print(f"Pacote de {num} MB processado com sucesso.")


