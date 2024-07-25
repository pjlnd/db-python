from funcao.atualizar import atualizar_usuário;
from funcao.criar import criar_usuario;
from funcao.deletar import deletar_usuario;
from funcao.procurar import procurar_usuario;


while True:
    print('Qual das açõs abaixo você deseja realizar? ')
    print('1 - Criar usuário')
    print('2 - Atualizar usuário')
    print('3 - Procurar usuario')
    print('4 - Deletar usuário')
    print('0 - Sair')

    escolha = int(input('Digite sua escolha: '))

    if escolha == 1:
        criar_usuario()
    elif escolha == 2:
        atualizar_usuário()
    elif escolha == 3:
        procurar_usuario()
    elif escolha == 4:
        deletar_usuario()
    elif escolha == 0:
        print('Você saiu do programa!')
        break
    else: 
        print('Escolha nula ou inexistente!')