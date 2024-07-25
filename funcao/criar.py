from database.database import db, Usuario

db.connect()

db.create_tables([Usuario])

def criar_usuario():
    print('---------------------------------------------------------------------')
    try:
        nome = input('Digite seu nome de usuário: ')
        email = input('Digite seu email: ')
        senha = input('Digite uma senha: ')
        user = Usuario.create(nome = nome, email = email, senha = senha)
        print('Usuário criado!')
    except:
        print('Falha ao criar usuário!')
    print('---------------------------------------------------------------------')

db.close()
