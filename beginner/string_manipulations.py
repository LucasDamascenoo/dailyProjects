


def text_analizer(name:str) -> str:
    
    nome_minusculo = name.lower()
    nome_maisculo = name.upper()
    total_char = len(name.replace(' ',''))
    
    return nome_minusculo,nome_maisculo,total_char


nome = input('Digite seu nome para analise: ')

minusculo, maiusculo, total = text_analizer(nome)

print(f"Nome em minúsculo: {minusculo}")
print(f"Nome em maiúsculo: {maiusculo}")
print(f"Total de caracteres (sem espaço): {total}")
    
    