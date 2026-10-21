def para_binario(n):
    if n < 2:
        return str(n)
    return para_binario(n // 2) + str(n % 2)

DIGITOS = "0123456789ABCDEF"

def para_hexa(n):
    if n < 16:
        return DIGITOS[n]
    return para_hexa(n // 16) + DIGITOS[n % 16]

numero = int(input("Digite um número decimal: "))
print(f"Binário: {para_binario(numero)}")
print(f"Hexadecimal: {para_hexa(numero)}")
