'''
‘r’ -> Usado somente para ler algo
‘w’ -> Usado somente para escrever algo
‘r+’ -> Usado para ler e escrever algo
‘a’ -> Usado para acrescentar algo
'''



# Abre um arquivo em modo de escrita ('w')
'''with open('Novo.txt', 'w', encoding='utf-8') as arquivo:
    # Escreve no arquivo
    arquivo.write('Lorem ipsum is placeholder. \n')'''

# Acrescenta um arquivo em modo de escrita ('a')
'''with open('Novo.txt', 'a', encoding='utf-8') as arquivo:
    # Escreve no arquivo
    arquivo.write('Lorem ipsum dolor sit amet. \n')'''

# Lê um arquivo e adiciona em modo de escrita ('r+')
'''with open('Novo.txt', 'r+', encoding='utf-8') as arquivo:
    for valor in arquivo:
        print()
    arquivo.write(str('\nmurilo'))'''

