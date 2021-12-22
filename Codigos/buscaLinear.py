''' Função para buscar um elemento em uma determinada Lista linerar(se não sabemos nada sobre essa lista)'''
def busca(lista,elem):

    for i in range(len(lista)):
        if lista[i] == elem:
            return i
    return None;



elemento = 'vitoria'
lista = [1,'vitor',2,3,4,5]

indice = busca(lista,elemento)

if indice is not None: 

    print('O elemnto {} está na posição {}'.format(elemento,indice))
else:
    print('O elemento {} não etá na lista'.format(elemento))