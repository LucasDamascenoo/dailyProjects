

guote = 'o rato roeu o a roupa do rei de roma aqui vemos que nao mas o que pode ter acontecido'


qtd_sentences = 0
palavras = guote.split()
total_char = len(guote)
total_words = len(palavras)


for char in guote:
    if char in '.!?':
        qtd_sentences +=1
        
average_word_length = total_char / total_words

if qtd_sentences > 0:
    average_sentences = total_char / qtd_sentences
else:
    average_sentences = 0
    

print(f'Total characters:  {total_char}')
print(f'Total Words: {total_words}')
print(f'Total Sentences: {qtd_sentences}')
print(f'Average word Lenght: {average_word_length}')
print(f'Average sentence Lenght: {average_sentences}')