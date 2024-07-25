from database.database import db, Usuario

db.connect()

def atualizar_usuário():

    def atualizar_nome():
        try:
            nome_usuario = input('Digite o nome atual do usuário que deseja atualizar: ')
            novo_nome_usuario = input('Digite o novo nome do usuário: ')
            usuario = Usuario.get(Usuario.nome == nome_usuario)
            usuario.nome = novo_nome_usuario
            usuario.save()
            print('Nome atualizado.')
        except:
            print('Não foi possível atualizar o nome!')

    def atualizar_email():
        try:
            email_usuario = input('Digite o email atual do usuário que deseja atualizar: ')
            novo_email_usuario = input('Digite o novo email do usuário: ')
            usuario = Usuario.get(Usuario.email == email_usuario)
            usuario.nome = novo_email_usuario
            usuario.save()
            print('Email atualizado.')
        except:
            print('Não foi possível atualizar o email!')

    def atualizar_senha():

        def atualizar_senha_nome():
            try:
                nome_usuario = input('Digite o nome atual do usuário: ')
                nova_senha = input('Digite a nova senha: ')
                usuario = Usuario.get(Usuario.nome == nome_usuario)
                usuario.senha = nova_senha
                usuario.save()
                print('Senha atualizada.')
            except:
                print('Não foi possível atualizar a senha!')

        def atualizar_senha_email():
            try:
                email_usuario = input('Digite o email atual do usuário: ')
                nova_senha = input('Digite a nova senha: ')
                usuario = Usuario.get(Usuario.email == email_usuario)
                usuario.senha = nova_senha
                usuario.save()
                print('Senha atualizada.')
            except:
                print('Não foi possível atualizar a senha!')

        print('Deseja atualizar a senha por qual meio? ')
        print('1 - Pelo nome')
        print('2 - Pelo email')

        opcao = int(input('Digite sua escolha: '))

        if opcao == 1:
            atualizar_senha_nome()
        elif opcao == 2:
            atualizar_senha_email()
        else:
            print('Escolha nula ou inexistente!')

    print('---------------------------------------------------------------------')
    print('Qual dado você deseja atualizar? ')
    print('1 - Nome')
    print('2 - Email')
    print('3 - Senha')

    escolha = int(input('Digite sua escolha: '))

    if escolha == 1:
        atualizar_nome()
    elif escolha == 2:
        atualizar_email()
    elif escolha == 3:
        atualizar_senha()
    else:
        print('Escolha nula ou inexistente!')
    print('---------------------------------------------------------------------')

db.close()