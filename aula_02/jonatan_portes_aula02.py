personagem = 'Jack'
nivel = 36
altura = 1.80
possui_arma = True
dano = 25
vida = 100
xp = 0 # Necessário 0/50


inimigo = 'Goblin'
nivelg = 20
danog = 12
vidag = 37
xpdrop = 50

print(f"{personagem} encontrou um {inimigo} nivel {nivelg}!")

if dano >= vidag:
    print(f"{inimigo} derrotado! {personagem} ganhou {xpdrop} de XP")
    xp = xp + xpdrop
    if xp >= 50:
        nivel = nivel + 1
        print(f"{personagem} subiu para o nivel {nivel}!")
else:
    print(f"{inimigo} ficou com {vidag - dano} de HP!")


class Guerreiro:
    """Personagem de classe Guerreiro: forte em combate corpo a corpo e com muita vida."""


# nome do personagem
# nivel: nível atual do personagem
# altura: altura em metros
# possui_arma: indica se está armado
help(Guerreiro)

# Atividade 02 - input() e print()
nome_jogador = input("Digite o nome do personagem: ")
idade_jogador = int(input("Digite a idade: "))
altura_jogador = float(input("Digite a altura (m): "))
tem_armadura = input("Possui armadura? (s/n): ").lower() == "s"

print("----- FICHA DO PERSONAGEM -----")
print(f"Nome: {nome_jogador}")
print(f"Idade: {idade_jogador}")
print(f"Altura: {altura_jogador}m")
print(f"Armadura: {tem_armadura}")

# Atividade 03 - operadores e conversão
anos_para_aposentar = 65 - idade_jogador
altura_cm = altura_jogador * 100
e_maior_de_idade = idade_jogador >= 18

print(f"Anos até os 65: {anos_para_aposentar}")
print(f"Altura em cm: {altura_cm}")
print(f"É maior de idade? {e_maior_de_idade}")
