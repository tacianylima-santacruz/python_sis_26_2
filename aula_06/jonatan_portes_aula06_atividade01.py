animais = ["cachorro", "gato", "passarinho", "hamster", "coelho"]
animais_favoritos = ["passarinho", "coelho"]

print(f"Animais favoritos: {animais_favoritos}")
print(f"Quantidade de animais: {len(animais)}")
print(f"Quantidade de animais favoritos: {len(animais_favoritos)}")

primeiro_favorito = animais_favoritos[0]
ultimo_favorito = animais_favoritos[-1]

print(f"Primeiro animal favorito: {primeiro_favorito}")
print(f"Último animal favorito: {ultimo_favorito}")

animais.pop()
print(animais)

animais.append("girafa")
print(len(animais))

print(f"Favoritos por ordem de preferência: {animais_favoritos}")

    
