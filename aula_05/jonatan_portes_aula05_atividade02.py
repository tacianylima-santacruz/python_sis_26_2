def registro_heroi(nome, classe, reino="Rivia"):
    informacoes_heroi = [nome, classe, reino]
    print(informacoes_heroi)

registro_heroi("jow", "mago", "rivia")
registro_heroi("jow", "mago")

def chamada_das_armas(nome,*itens):
    print(f"{nome}")
    for item in itens:
        print(f'- {item}')

chamada_das_armas("jow", "Poção de cura", "Cajado", "Livro")

def ficha_detalhada(nome, **atributos):
    print(f'{nome}: ')
    for atributo, valor in atributos.items():
        print(f'{atributo} = {valor}')

ficha_detalhada("jow", forca = 43, velocidade = 78, inteligência = 98, destreza = 81)

"""Desafio: """

def reacao_perigo(*perigos):
    for perigo in perigos:
        if perigo == "Nevoeiro":
            pass
        elif perigo == "Balrog":
            print("Gandalf avisa para fugir!")
            break

reacao_perigo("Nevoeiro", "Goblin", "Balrog")