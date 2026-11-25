usuario_cadastrado = 'jonatan'
senha_cadastrada = '1234'
conta = True

usuario_digitado = input("Usuário: ")
senha_digitada = input("Senha: ")

conta = usuario_digitado == usuario_cadastrado and senha_digitada == senha_cadastrada

print(conta)
#if conta == True:
#   print(f"Acesso liberado!")
