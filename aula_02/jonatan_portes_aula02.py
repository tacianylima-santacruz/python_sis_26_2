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
