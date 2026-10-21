texto_pergaminho = input("Digite o texto do pergaminho: ")
texto_limpo = texto_pergaminho.strip()
palavras = texto_limpo.split()

print(f"Total de caracteres: {len(texto_limpo)}")
print(f"Total de palavras: {len(palavras)}")
print(f"Primeira palavra: {palavras[0]}")
print(f"Última palavra: {palavras[-1]}")

ameaca = "Anel"
print(f"A palavra '{ameaca}' existe no texto? {ameaca.lower() in texto_limpo.lower()}")
print(f"Quantas vezes aparece: {texto_limpo.lower().count(ameaca.lower())}")
