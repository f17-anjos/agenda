from contato import Contato


def main():
    print(" opção 1 cadastrar, \n"
          " 2 opção atualizar \n"
          " 3 opção pesquisar \n"
          " 4 opção deletar \n "
          " 5 mostrar registros \n")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        nome = input("Digite o seu nome :")
        telefone = input("Digite o seu telefone :")
        email = input("Digite o seu email :")
        blog = input("Digite o seu blog :")
        print(nome, telefone, email, blog)
        contato = Contato(nome, telefone, email, blog)
        contato.salvar()

    elif opcao == 5:
       print(Contato.tudo())



main()
