total = 0
produto = 1

while True:
    preco = (int(input(f"Digite o preço do {produto}º produto: ")))
    if preco == 0:
        print("Compra finalizada!")
        break
    produto = produto + 1
    total = total + preco

for parcelas in range(1, 13):
    valor_parcela = total / parcelas
    print(f"{parcelas}x de R$ {valor_parcela:.2f}")


          