from cadernetaCódigo import Caderneta
from time import sleep

caderneta = Caderneta()

while True:
    print('''
Escolha uma opção a seguir:
1 - Inserir anotação.
2 - Editar anotação.
3 - Excluir anotação.
4 - Mostrar anotações.
5 - Limpar anotações.
6 - Fechar programa.
''')
    pergunta = input('---> ')
    if pergunta == '1':
        print('')
        titulo = input('Insira o título desejado: ')
        anotacao = input('Insira a anotação desejada: ')
        sleep(0.5)
        caderneta.inserirAnot(titulo, anotacao)
        sleep(0.75)
    elif pergunta == '2':
        print('\nSelecione a númeração de uma anotação a seguir que deseja alterar(ENTER PARA RETORNAR):\n')
        with open('caderneta.txt', 'r') as cadernetatxt:
            lista = cadernetatxt.readlines()
            for i in lista:
                print(i, end="")
        resposta = input('\n--->')
        try:
            if resposta == '':
                sleep(0.5)
            elif int(resposta) <= len(lista) and int(resposta) > 0:
                titulo = input('Insira o novo título desejado: ')
                anotacao = input('Insira a nova anotação desejada: ')
                sleep(0.5)
                caderneta.editarAnot(resposta, titulo, anotacao, lista)
                sleep(0.75)
            else:
                sleep(0.5)
                print('\nValor inválido.')
                sleep(0.75)
        except:
            sleep(0.5)
            print('\nValor inválido.')
            sleep(0.75)
    elif pergunta == '3':
        print('\nSelecione a númeração de uma anotação a seguir que deseja excluir(ENTER PARA RETORNAR):\n')
        with open('caderneta.txt', 'r') as cadernetatxt:
            lista = cadernetatxt.readlines()
            for i in lista:
                print(i, end="")
        resposta = input('\n--->')
        try:
            if resposta == '':
                sleep(0.5)
            elif int(resposta) <= len(lista) and int(resposta) > 0:
                sleep(0.5)
                caderneta.excluirAnot(resposta, lista)
                sleep(0.75)
            else:
                sleep(0.5)
                print('\nValor inválido.')
                sleep(0.75)
        except:
            sleep(0.5)
            print('\nValor inválido.')
            sleep(0.75)
    elif pergunta == '4':
        print('\nSelecione a númeração de uma anotação a seguir que deseja mostrar(ENTER PARA RETORNAR):\n')
        with open('caderneta.txt', 'r') as cadernetatxt:
            lista = cadernetatxt.readlines()
            for i in lista:
                print(i.split(':')[0])
        resposta = input('\n--->')
        try:
            if resposta == '':
                sleep(0.5)
            elif int(resposta) <= len(lista) and int(resposta) > 0:
                sleep(0.5)
                caderneta.mostrarAnot(resposta, lista)
                sleep(0.75)
            else:
                print('\nValor inválido.')
        except:
            print('\nValor inválido.')
    elif pergunta == '5':
        print('\nTem certeza que deseja limpar a caderneta?(Digite "S" para confirmar)')
        resposta = input('\n--->')
        if resposta.lower() == 's':
            sleep(0.5)
            caderneta.limpaCaderneta()
            sleep(0.75)
    elif pergunta == '6':
        sleep(0.5)
        print('\nVocê escolheu sair.')
        sleep(0.75)
        break
    else:
        sleep(0.5)
        print('\nValor inválido')
        sleep(0.75)