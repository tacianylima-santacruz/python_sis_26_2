"""
nome_heroi = "Batman"
print("O herói que vai salvar a cidade é o " + nome_heroi_cidade)

NameError: name 'nome_heroi_cidade' is not defined

Variavel chamada de forma incorreta, trocar para print("O herói que vai salvar a cidade é o " + nome_heroi)
"""

"""
idade_pet = 5
mensagem = "A idade do meu cachorro é " + idade_pet + " anos."
print(mensagem)

TypeError: can only concatenate str (not "int") to str

Não é possível somar inteiros com strings, trocar para -> print = mensagem = (f"A idade do meu cachorro é " + {idade_pet} + " anos.")
"""

"""
print("Calculadora de Dobro!")
# Simulando alguém que digitou a palavra 'dez' em vez do número 10
numero_digitado = "dez"
dobro = int(numero_digitado) * 2
print("O dobro é:", dobro)

ValueError: invalid literal for int() with base 10: 'dez'

'dez' não é um número e sim uma string, trocar para 0
"""

"""
cat_attributes = {
    "name": "Zia",
    "age": 1,
    "color": "grey"
}

# Tentando descobrir a raça (breed) da gata
raca_gato = cat_attributes["breed"]
print("A raça da gata é:", raca_gato)

KeyError: 'breed'

Tentou acessar uma chave que não existe
"""
some_numbers = [10, 20, 30]


"""
# Tentando acessar o quarto número da lista
quarto_numero = some_numbers[3]
print("O número escolhido foi:", quarto_numero)

IndexError: list index out of range

Não existe quarto indice/posicao 10 = 0, 20 = 1, 30 = 2
"""

"""
tesouro_moedas = 100
aventureiros_sobreviventes = 0

print("Calculando a divisão do tesouro...")

moedas_por_pessoa = tesouro_moedas / aventureiros_sobreviventes

print("Cada aventureiro vai receber:", moedas_por_pessoa)

ZeroDivisionError: division by zero

Não existe divisão por 0
"""

"""
print("=== Sistema do Zoológico ===")
# horário, alimento, quantidade
dieta_axolote = ("08:00", "minhocas", 50)

print("O axolote enjoou de minhocas. Vamos alterar a dieta para pizza!")

dieta_axolote[1] = "pizza de calabresa"

print("Nova dieta:", dieta_axolote)

TypeError: 'tuple' object does not support item assignment

Tuplas não aceitam alteração é necessário substituir () por [] ->lista
"""

"""
def contagem_regressiva(tempo):


    print(f"Faltam {tempo} segundos...")

    # Passo Recursivo: A função chama a si mesma
    contagem_regressiva(tempo - 1)

print("Iniciando contagem para a explosão do Anel...")
contagem_regressiva(3)
     
RecursionError: maximum recursion depth exceeded

looping infinito, trocar para:

def contagem_regressiva(tempo):
    if tempo < 0:
        return

    print(f"Faltam {tempo} segundos...")

    # Passo Recursivo: A função chama a si mesma
    contagem_regressiva(tempo - 1)
  
print("Iniciando contagem para a explosão do Anel...")
contagem_regressiva(3)
"""

