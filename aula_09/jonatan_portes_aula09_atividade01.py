import os

arquivo = "acessos.log"

with open(arquivo, "w", encoding="utf-8") as arquivo_1:
    arquivo_1.write("Sistema inicializado\n")
print(f"Arquivo '{arquivo}' criado com sucesso!\n")

eventos = [
    "[LOGIN] Usuário 'admin' conectou ao painel.\n",
    "[INFO] Sincronização do banco de dados concluída.\n",
    "[ERRO] Falha de conexão com a API externa.\n",
    "[LOGIN] Usuário 'suporte_02' efetuou login.\n",
    "[ERRO] Tentativa de acesso negada para IP 192.168.1.50.\n"
]

with open(arquivo, "a", encoding="utf-8") as arquivo_2:
    arquivo_2.writelines(eventos)
print("5 novos eventos adicionados com sucesso!")

with open(arquivo, "r", encoding="utf-8") as arquivo_3:
    primeira_linha = arquivo_3.readline().strip()
    print(f"Cabeçalho do arquivo: {primeira_linha}")
    
    todas_as_linhas = arquivo_3.readlines()
    if todas_as_linhas:
        ultimo_evento = todas_as_linhas[-1].strip()
        print(f"Último evento registrado: {ultimo_evento}")

palavra_chave_1 = "LOGIN"
palavra_chave_2 = "ERRO"
contador_alertas = 0

with open(arquivo, "r", encoding="utf-8") as arquivo_4:
    for linha in arquivo_4:
        if palavra_chave_1 in linha or palavra_chave_2 in linha:
            print(f"  -> {linha.strip()}")
            contador_alertas += 1

print(f"\n T otal de alertas ({palavra_chave_1}/{palavra_chave_2}) encontrados: {contador_alertas}")