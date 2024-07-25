from database import db, Usuario

db.connect()

def procurar_usuario():

    def pelo_nome():
        try: 
            nome_usuario = input('Qual o nome do usuário? ')
            usuario = Usuario.get(Usuario.nome == nome_usuario)
            print('Usuário encontrado: ', usuario.nome, usuario.email, usuario.senha)
        except:
            print('Usuário apagado ou inexistente!')


    def pelo_email():
        try:
            email_usuario = input('Qual o email do usuário? ')
            usuario = Usuario.get(Usuario.email == email_usuario)
            print('Usuário encontrado: ', usuario.nome, usuario.email, usuario.senha )
        except:
            print('Usuário apagado ou inexistente!')

    def mostrar_todos():
        lista_usuarios = Usuario.select()
        print('Usuários cadastrados: ')
        for u in lista_usuarios:
            print('-', u.id, u.nome, u.email)

    print('De qual forma você quer procurar o usuário? ')
    print('1 - Pelo nome')
    print('2 - Pelo email')
    print('3 - Mostrar todos')

    escolha = int(input('Digite sua escolha: '))

    if escolha == 1:
        pelo_nome()
    elif escolha == 2:
        pelo_email()
    elif escolha == 3:
        mostrar_todos()
    else:
        print('Escolha nula ou inexistente!')

