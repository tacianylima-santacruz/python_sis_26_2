import os

arquivo = "acessos.log"

try:
    with open("servidor_inexistente.log", "r", encoding="utf-8") as arquivo_teste:
        conteudo = arquivo_teste.read()

except FileNotFoundError:
    print("Aviso: O arquivo de teste não foi encontrado. Continuando o programa.")

except Exception as erro:
    print(f"Erro inesperado ao abrir o arquivo de teste: {erro}")

finally:
    print("Verificação do arquivo de teste finalizada.\n")


try:
    with open(arquivo, "w", encoding="utf-8") as arquivo_1:
        arquivo_1.write("Sistema inicializado\n")

    print(f"Arquivo '{arquivo}' criado com sucesso!\n")

except PermissionError:
    print("Erro: Sem permissão para criar ou escrever no arquivo.")

except OSError as erro:
    print(f"Erro ao criar o arquivo: {erro}")


eventos = [
    "[LOGIN] Usuário 'admin' conectou ao painel.\n",
    "[INFO] Sincronização de banco de dados concluída.\n",
    "[ERRO] Falha de conexão com a API externa.\n",
    "[LOGIN] Usuário 'suporte_02' efetuou login.\n",
    "[ERRO] Tentativa de acesso negada para IP 192.168.1.50.\n"
]

try:
    with open(arquivo, "a", encoding="utf-8") as arquivo_2:
        arquivo_2.writelines(eventos)

    print("5 novos eventos adicionados com sucesso!\n")

except PermissionError:
    print("Erro: Sem permissão para adicionar eventos ao arquivo.")

except OSError as erro:
    print(f"Erro durante a gravação dos eventos: {erro}")


try:
    with open(arquivo, "r", encoding="utf-8") as arquivo_3:
        primeira_linha = arquivo_3.readline().strip()
        print(f"Cabeçalho do arquivo: {primeira_linha}")

        todas_as_linhas = arquivo_3.readlines()

        if todas_as_linhas:
            ultimo_evento = todas_as_linhas[-1].strip()
            print(f"Último evento registrado: {ultimo_evento}")

except FileNotFoundError:
    print("Erro: O arquivo de log não foi encontrado para leitura.")

except UnicodeDecodeError:
    print("Erro: Não foi possível decodificar o arquivo usando UTF-8.")

except PermissionError:
    print("Erro: Sem permissão para ler o arquivo.")

finally:
    print("Etapa de leitura finalizada.\n")


palavra_chave_1 = "LOGIN"
palavra_chave_2 = "ERRO"
contador_alertas = 0

try:
    with open(arquivo, "r", encoding="utf-8") as arquivo_4:
        for linha in arquivo_4:
            if palavra_chave_1 in linha or palavra_chave_2 in linha:
                print(f" -> {linha.strip()}")
                contador_alertas += 1

    print(
        f"\nTotal de alertas "
        f"({palavra_chave_1}/{palavra_chave_2}) encontrados: "
        f"{contador_alertas}"
    )

except FileNotFoundError:
    print("Erro: Não foi possível encontrar o arquivo para auditoria.")

except UnicodeDecodeError:
    print("Erro: Falha na decodificação do arquivo durante a auditoria.")

except PermissionError:
    print("Erro: Sem permissão para realizar a auditoria.")

except Exception as erro:
    print(f"Erro inesperado durante a auditoria: {erro}")

finally:
    print("Auditoria finalizada. Recursos de arquivo liberados.")