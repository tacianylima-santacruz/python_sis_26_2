import os

def ticket_type():
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0:
                raise ValueError
        except ValueError:
            print("Idade inválida, digite novamente.")
        else:
            print("Bem-vindo ao museu!")
            if age < 12:
                print("You get in for free. Lucky you!")
            elif age < 18:
                print("You get a youth discount!")
            elif age < 65:
                print("That's a full-price ticket for you.")
            else:
                print("You get a senior discount!")
            break
        finally:
            input("Pressione Enter para continuar...")
            os.system("cls" if os.name == "nt" else "clear")

ticket_type()
