from database.database import db, Usuario

db.connect()

def deletar_usuario():

    def pelo_nome():
        try:
            nome_usuario = input('Digite o nome do usuário que deseja deletar: ')
            usuario = Usuario.get(Usuario.nome == nome_usuario)
            usuario.delete_instance()
            print('Usuário deletado.')
        except:
            print('Usuário apagado ou inexistente!')

    def pelo_email():
        try:
            email_usuario = input('Digite o email do usuário que deseja deletar: ')
            usuario = Usuario.get(Usuario.email == email_usuario)
            usuario.delete_instance()
            print('Usuário deletado.')
        except:
            print('Usuário já apagado ou inexistente!')

    print('---------------------------------------------------------------------')
    print('Deseja deletar por qual meio? ')
    print('1 - Pelo nome')
    print('2 - Pelo email')

    escolha = int(input('Digite sua escolha: '))

    if escolha == 1:
        pelo_nome()
    if escolha == 2:
        pelo_email()
    else:
        print('Nome não encontrado!')
    print('---------------------------------------------------------------------')

db.close()
