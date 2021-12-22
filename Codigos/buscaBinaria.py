'''Caso a lista esteja ordenada a busca binaria é mais eficiente para encontrarmos um elemento na lista -> log(n)'''

# De maneira Recursiva
def buscaBinaria(lista, elemento,indiciIni = 0,indiciFim = None):

    if indiciFim is None:
        indiciFim = len(lista)-1

    if indiciIni <= indiciFim:
        meio = (indiciIni + indiciFim) // 2
        if (lista[meio] == elemento):
            return meio
        if elemento < lista[meio]:
            return buscaBinaria(lista,elemento,indiciIni,meio-1)
        else:
            return  buscaBinaria(lista,elemento,meio+1,indiciFim)

    return None

# De maneira Iterativa
def buscaBinariaIterativa(lista,elemento,indiciIni = 0,indiciFim = None):
    
    if indiciFim is None:
        indiciFim = len(lista)-1 

    while indiciIni <= indiciFim: 
        
        meio = (indiciIni + indiciFim) // 2 

        if(lista[meio]==elemento):
            return meio
        if (elemento<lista[meio]):
            indiciFim = meio-1
       
        if (elemento>lista[meio]):
            indiciIni = meio + 1
    
    return None
       
       

lista = [1,2,3,4,5,6,7,8,9]
elemento = 10
print('O elemnento {} está na posição {}'.format(elemento,buscaBinariaIterativa(lista,elemento)))
print('O elemnento {} está na posição {}'.format(elemento,buscaBinaria(lista,elemento)))