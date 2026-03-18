
#dado uma lista, some-a e traga o resultado

def sum_list(lista:list) -> int:
    
    soma = 0
    
    for i in lista:
        soma += i

    return soma  


print(sum_list([10,10,50,90.5]))
        
        


