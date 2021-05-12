from contato import Contato

def main():
    print(" 1 opção cadastrar : \n"
          " 2 opção pesquisar : \n"
          " 3 opção atualizar : \n"
          " 4 opção deletar : \n "
          "5 mostrar registros : \n")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        nome = input("Digite o seu nome:")
        telefone = input("Digite o seu telefone :")
        email = input("Digite o seu email :")
        blog = input("Digite o seu blog :")
        print(nome, telefone, email, blog)
        contato = Contato(nome, telefone, email, blog)
        contato.salvar()

    elif opcao == 2:
        usuario = input("Qual usuário que deseja pesquisar :")
        contato = Contato.pesquisar_nome(usuario)
        print(contato)


    elif opcao == 3:
        usuario = input("Digite o usuário que deseja atualizar :")
        contato_procurado = Contato.pesquisar(usuario)
        if contato_procurado:
            nome = input("Digite o seu nome: ")
            telefone = input("Digite o seu telefone: ")
            email = input("Digite o seu email :")
            blog = input("Digite o seu blog :")
            contato = Contato(nome, telefone, email, blog)
            Contato.atualizar(usuario, contato)
            print(f'O contato foi atualizado ')
        else:
            print("O contato não existe na agenda! ")


    elif opcao == 4:
        usuario = input("Qual usuário deseja remover :")
        contato = Contato.remover(usuario)
        if contato:
            print("O contato foi removido :")
        else:
            print("O contato não existe!")

    elif opcao == 5:
        contato = Contato.tudo()
        contato.mostrar_registros(contato)



main()



