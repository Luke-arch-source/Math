#Programa que permite que permite que o usuário escolha uma das operações ou outras ações matemáticas
# comuns disponíveis e também o tipo de número que será inserido. Após essas decisões, ele
# poderá inserir um ou mais números.

#Estrutura de repetição logo abaixo para permitir que o programa mesmo que ocorram alguns
#problemas.
#No decurso da leitura dos comentários do código, você poderá confundir conjunto com lista, mas
#são distintos. O conceito de conjunto usado aqui é simples: um ou mais números em um mesmo
#agrupamento aleatório ou específico, já o de lista é o seguinte: uma das variáveis compostas
#do Python cujo número de elementos é dado por len(nome_lista) e os seus itens são identificados
#por meio de índices, sendo que o primeiro começa por 0 os dos próximos aumentam de um em um.
#Eu usei os índices para poder somar os números quando for necessário nos momentos nos quais são criadas listas.

while True:
    #Eu usei tratamento de erros e exceções para impedir que a execução do programa seja interrompida
    #de modo indesejado quando houver algum problema.
    try:
        print('1 - ADIÇÃO')
        print('2 - SUBTRAÇÃO')
        print('3 - MULTIPLICAÇÃO')
        print('4 - DIVISÃO INTEIRA')
        print('5 - DIVISÃO')
        print('6 - Fatorial')
        print('7 - MÉDIA ARITMÉTICA SIMPLES')
        print('8 - MÉDIA HARMÔNICA')
        #Variável que recebe a escolha da ação matemática
        choice = int(input('Sua escolha: '))
        #EStrutura de repetição para impedir a inserção
        #de um número fora do intervalo das escolhas aceitas
        while choice < 1 or choice > 8:
            print('\033[32mNúmero fora do intervalo!\033[m')
            choice = int(input('Sua escolha: '))

        print('17 - TIPO INTEIRO')
        print('18 - TIPO COMPLEXO')
        #Estrutura condicional para auxiliar na inserção dos números de acordo
        #com a ação desejada
        if choice != 6 and choice != 4:
            # Variável para receber a escolha do tipo do(s) número(s)
            ch2 = int(input('Escolha do tipo: '))
            while ch2 != 17 and ch2 != 18:
                print('\033[35mNúmero fora do intervalo das escolhas aceitas!\033[m')
                ch2 = int(input('Escolha do tipo: '))
            if choice <= 5 and choice != 4:
                if ch2 == 17:
                    n1 = int(input('Primeiro número inteiro: '))
                    n2 = int(input('Segundo número inteiro: '))
                    if choice == 5 and type(n2) == int:
                        while n2 == 0:
                            print('\033[35mNão existe divisão por zero!\033[m')
                            n2 = int(input('Segundo número inteiro: '))
                elif ch2 == 18:
                    print('\nPrimeiro número complexo: ', end='')
                    n1 = complex(float(input('Parte real: ')), float(input('Parte imaginária: ')))
                    print('\nSegundo número complexo: ', end='')
                    n2 = complex(float(input('Parte real: ')), float(input('Parte imaginária: ')))
            elif choice >= 7:
                #Lista usada para armazenar os números para o cálculo de alguma das médias
                conj = []
                #Variável que receberá o número de elementos do conjunto da média aritmética simples
                #ou da harmônica
                qta = int(input('Quantos números vão compor o conjunto? '))
                #EStrutura de repetição que impede o usuário de inserir um número nulo ou negativo
                while qta <= 0:
                    print('\033[31mNúmeros nulos ou menores do que zero não podem ser usados nesse campo!\033[m')
                    qta = int(input('Quantos números vão compor o conjunto? '))
                if ch2 == 17:
                    for d in range(0, qta):
                        conj.insert(d, int(input(f'{d+1}º termo do conjunto: ')))
                elif ch2 == 18:
                    for h in range(0, qta):
                        conj.insert(h, complex(float(input(f'Parte real do {h+1}º termo: ')), float(input(f'Parte imaginária do {h+1}º termo: '))))



        elif choice == 6:
            print('O número cujo fatorial será calculado deve ser inteiro não negativo!')
            n = int(input('Número: '))
            while n < 0:
                print('Números negativos não têm fatorial!')
                n = int(input('Número: '))
        elif choice == 4:
            print('A divisão inteira não pode receber números complexos!')
            n1 = int(input('Primeiro número inteiro: '))
            n2 = int(input('Segundo número inteiro: '))
            while n2 == 0:
                print('\033[35mNão existe divisão por zero!\033[m')
                n2 = int(input('Segundo número inteiro: '))

    except (ValueError, TypeError):
        print('\033[31mVocê fez alguma inserção inválida quanto ao tipo!!!\033[m')
    else:
        #Tratamento de erros e exceções - Se ocorrer alguma divisão por zero, será exibida uma mensagem falando isso
        #O programa será encerrado caso ocorra ou não esse evento
        try:
            #Estrutura condicional para serem feitos os cálculos de acordo com as escolhas
            if choice == 6:
                fat = 1
                if n > 1:
                    for a in range(1, n + 1):
                        fat *= a
                        if a < n:
                            print(f'{a} x ', end='')
                        elif a == n:
                            print(f'{a} = {a}! = {fat}')
                else:
                    print(f'{n}! = {fat}')

            elif choice <= 5:
                if choice == 1:
                    #Variável para receber a soma dos dois números
                    total = n1 + n2
                    #Mensagem para exibir o resultado e conta armada
                    print(f'{n1} + {n2} = {total}')
                elif choice == 2:
                    #Variável para receber a diferença entre os dois números
                    diferenca = n1 - n2
                    #Estrutura condicional para mostrar a diferença entre os dois
                    #números com 2 casas decimais ou sem especificar conforme
                    #o tipo do resultado
                    if ch2 == 17:
                        if n2 >= 0:
                            print(f'{n1} - {n2} = {diferenca}')
                        elif n2 < 0:
                            print(f'{n1} - ({n2}) = {diferenca}')
                    else:
                        print(f'{n1} - {n2} = {diferenca}')
                elif choice == 3:
                    #Variável para receber o produto do valor contido em n1 pelo armazenado
                    #em n2
                    produto = n1 * n2
                    if ch2 == 17:
                        if n2 >= 0:
                            print(f'{n1} x {n2} = {produto}')
                        elif n2 < 0:
                            print(f'{n1} x ({n2}) = {produto}')
                    else:
                        print(f'{n1} x {n2} = {produto}')
                elif choice == 4:
                    #Variável para receber a divisão inteira entre os dois números
                    cociente_inteiro = n1 // n2
                    #Mensagem que exibe o resultado
                    print(f'{n1} // {n2} = {cociente_inteiro}')
                elif choice == 5:
                    #Variável para receber o cociente não arredondado em duas casas decimais
                    cociente = n1 / n2
                    #Estrutura condicional para exibir o resultado de acordo com o
                    #tipo do valor do quociente
                    if type(cociente) == float:
                        print(f'{n1} / {n2} = {cociente:.2f}')
                    else:
                        print(f'{n1} / {n2} = {cociente}')
            elif choice >= 7:
                #Estrutura condicional para calcular a média aritmética simples ou a harmônica
                if choice == 7:
                    #A média aritmética simples é calculada da seguinte forma: os números de um determinado
                    #conjunto são somados e o resultado é dividido pela quantidade de termos desse conjunto
                    #O sum(conj) é usado para todos os números serem somados e o len(conj) é utilizado
                    #para haver a divisão pelo número de termos
                    #OBS: Também poderia ser usado no lugar do len(conj) a variável qta, uma vez
                    #que armazenam valores iguais
                    media_arit = sum(conj) / len(conj)
                    #Estrutura condicional para exibir o resultado de acordo com o seu tipo
                    if type(media_arit) == float:
                        # Questão: ainda estou pensando em como indicar se o resultado
                        # é aproximado ou exato nesta condição
                        print(f'A média aritmética simples do conjunto {conj} é igual a {media_arit:.2f}')
                    elif type(media_arit) == complex:
                        print(f'A média aritmética simples do conjunto {conj} é igual a {media_arit}')
                elif choice == 8:
                    #As variáveis imediatamente abaixo recebem inicialmente o valor 0 para poderem
                    #cumprir os seus papéis de modo adequado no programa
                    #A variável soma_inversos é usada na estrutura condicional para somar os inversos numéricos dos elementos
                    #do conjunto
                    #A variável cont é utilizada para indicar o elemento que será somado aos demais por meio
                    #do  seu índice na lista
                    cont = soma_inversos = 0
                    while cont <= (len(conj) - 1):
                        soma_inversos += 1/conj[cont]
                        cont += 1
                    #Variável para receber a média harmônica
                    #Ela é calculada por meio da divisão do número de termos de um conjunto pela soma
                    #dos seus inversos numéricos
                    media_harm = len(conj) / soma_inversos
                    #Estrutura condicional para exibir o resultado de acordo com o seu tipo
                    if type(media_harm) == complex:
                        print(f'A média harmônica dos elementos do {conj} é igual a {media_harm}')
                    elif type(media_harm) == float:
                        #Questão: ainda estou pensando em como indicar se o resultado
                        #é aproximado ou exato nesta condição
                        print(f'A média harmônica dos elementos do {conj} é igual a {media_harm:.2f}')
        except ZeroDivisionError:
            print('Houve um problema: tentativa de divisão por zero')
        else:
            print('Não houve nenhum problema')

        finally:
            break