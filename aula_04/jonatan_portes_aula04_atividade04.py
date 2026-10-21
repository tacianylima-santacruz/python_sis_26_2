numero = int(input("Digite um número correspondente ao seu problema: \n 1 - Problema com Computador/Hardware \n 2 - Instalação de Software \n 3 - Sem acesso à Internet/Rede \n 4 - Reset de Senha Qualquer outra opção.\n Número: "))

match numero:
    case 1:
        print("Direcionar para: Manutenção")
    case 2:
        print("Direcionar para: Equipe de Suporte")
    case 3:
        print("Direcionar para: Infraestrutura")
    case 4:
        print("Direcionar para: Atendimento Automático (Envio de link de redefinição)")
    case _:
        print("Opção inválida. Chamado encaminhado para a Triagem Geral.")