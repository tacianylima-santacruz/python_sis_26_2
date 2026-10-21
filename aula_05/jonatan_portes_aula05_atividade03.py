controle_servidores = 10    
print(controle_servidores)
def registrar_servidor(adicionarservidor):
    """Adiciona servidores na variável 'controle_sevidores através do parâmetro 'adicionarservidor'"""
    global controle_servidores
    controle_servidores = controle_servidores + adicionarservidor

registrar_servidor(2)
print(controle_servidores)
print(controle_servidores - 5)
print(controle_servidores + 5)

def gerenciar_conexoes():
    conexao_interna = 5
    def derrubar_conexao():
        nonlocal conexao_interna
        conexao_interna -= 1
    derrubar_conexao()
    derrubar_conexao()
    print(f"Conexões restantes: {conexao_interna}")

gerenciar_conexoes()

alterar_cota = lambda cota, ajuste: cota + ajuste
print(f"Nova cota: {alterar_cota(100, 50)} GB")
