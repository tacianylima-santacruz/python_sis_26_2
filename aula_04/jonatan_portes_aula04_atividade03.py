nota = float(input("Qual foi sua nota: "))

if nota >= 9.0:
    print("Parabéns!")
elif nota > 7.0 and nota < 8.9:
    print("Muito bem!")
elif nota > 5.0 and nota < 6.9:
    print("Faltou atenção")
else:
    print("Precisa melhorar!")
