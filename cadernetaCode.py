class Caderneta:
    
    def __init__(self):
        try:
            open('caderneta.txt', 'x')
        except:
            pass

    def inserirAnot(self, titulo, anot):
        with open('caderneta.txt', 'r') as caderneta:
            c = caderneta.readlines()
            contador = len(c) 
        with open('caderneta.txt', 'a') as cadernetatxt:
            cadernetatxt.write(f'{contador+1} - {titulo} : {anot} \n')
            print('\nAnotação inserida com sucesso.')

    def limpaCaderneta(self):
        open('caderneta.txt', 'w')
        print('\nTodas as anotações foram excluídas com sucesso.')

    def editarAnot(self, resposta, titulo, anot, lista):
        for p in lista:
            if resposta == p[:1]:
                lista[lista.index(p)] = f'{resposta} - {titulo} : {anot} \n'
                with open('caderneta.txt', 'w') as cadernetatxt:
                    for j in lista:
                        cadernetatxt.writelines(j)
                print('\nAlteração feita com sucesso.')
                break
    
    def excluirAnot(self, resposta, lista):
        for p in lista:
            if resposta == p[:1]:
                lista.remove(p)
                with open('caderneta.txt', 'w') as caderneta:
                    for j in range(len(lista)):
                        caderneta.writelines(f'{j+1} - {lista[j][4:]}')
                print('\nAnotação exluída com sucesso.')
                break

    def mostrarAnot(self, resposta, lista):
        for j in lista:
            if resposta == j[:1]:
                print(f'\n{j[4:]}')