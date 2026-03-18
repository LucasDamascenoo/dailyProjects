


def idx_list(lista:list) -> list:
    
    resultado = [(valor,i) for i,valor in enumerate(lista)]
    
    return resultado
    


print(idx_list(['lucas','tiane','bruce']))