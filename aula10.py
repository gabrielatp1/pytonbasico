'''ENDSWITH'''
'''frutas = {"manga", "amora", "morango"}
for f in frutas:
    if f.endswith("a"):
        print(f)
        print("TERMINA com A \n")'''

'''TUPLA COM COUNT = conta quantas vezes apareceu'''
'''tupla = (1, 1, 2, 4)
quantidade = tupla.count(1)
print(tupla)
print(quantidade)'''

'''INDEX = retorna o índice"
tupla = (1, 1, 2, 4)
quantidade = tupla.index(1)
print(tupla)
print(quantidade)'''

'''MAX e MIN'''
'''tupla = (1, 1, 2, 4)
máximo = max(tupla)
print(tupla)
print(máximo)'''

'''tupla = (1, 1, 2, 4)
print(f'o menor número é {min(tupla)}')'''

'''FUNÇÕES / MODULAÇÕES'''
'''def soma(a, b):
    print("Adição: ")
    print(a+b)
soma(2, 9)
soma(7, 8)
soma(10, 15)'''

'''def sub(a, b):
    print("Subtração: ")
    print(a-b)
sub(9, 2)
sub(7, 8)
sub(10, 15)'''

'''ARGUMENTO = valor à função'''
'''RETORNO = toda função retorna alguma coisa!'''
'''def soma(a,b):
    return a+b
soma(1, 2)
print(soma(1, 2))'''

'''def pesquisa(lista, valor):
    for x,e in enumerate(lista):
        if e == valor:
            return x
    return None
L =[10, 20, 25, 30]
print(pesquisa(L, 25))
print(pesquisa(L, 30))'''

def soma(L):
    total=0
    for e in L:
        total+=e
    return total
def media(L):
    return(soma(L)/len(L))
L = (1, 2, 3, 4)
print(soma(L))
print(media(L))