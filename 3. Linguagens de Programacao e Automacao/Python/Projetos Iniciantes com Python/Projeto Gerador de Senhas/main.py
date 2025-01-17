def gerador_de_senha():
    import random

    characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '#', '$', '%', '&', '*', '+',
                '-', '.', '*', '=', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 'u', 'v', 't', 'm', 'n', 'z', 'x']

    num_list = int(len(characters)+1)

    num_char = int(input("Escreva o número de caracteres da sua senha: "))

    i = 0

    n_list = []

    while i < num_char:
        n_list.append(characters[random.randint(0, num_list)]) 
        #append usada para adicionar um novo item ao final de uma lista
        #randint função do módulo random que gera um número inteiro aleatório
        #  de um intervalo fechado
        i += 1

    password = "".join(n_list) #cria uma string única contendo os caracteres gerados
    
    return password

print ("A sua senha é:", gerador_de_senha())
