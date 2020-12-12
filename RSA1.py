import Calculos
import chavepublica as cp
import interface

while (True):

    interface.main()
    opcao = input("----------| DIGITE SUA OPCAO: ")

    if opcao == '1':

        cp.chave_publica()

        Calculos.limpar_terminal()
        continue

    while opcao == '2':

        interface.cp()
        x = input('-> ')

        chave = open('chave_publica.txt')
        lst = list()

        for line in chave:
            line = line.rstrip()
            numbers = line.split()
            lst.extend(numbers)

        n = int(lst[0])
        e = int(lst[1])

        if x == '1':
            print('-----| CHAVE PÚBLICA:{} {} |---------'.format(n, e))

        verificador = lst[0] +' '+lst[1]

        print('---------| DIGITE A CHAVE PUBLICA RECEBIDA PREVIAMENTE: |--------')

        chave2 = input("--> ")

        if(chave2 != verificador):
            print("A chave pública digitada está incorreta")
            continue

        print("DIGITE UMA MENSAGEM PARA ENCRIPTAR:")

        msgn = input("-->")

        msgn.upper()

        Calculos.codificar(msgn, e, n)

        Calculos.limpar_terminal()

        break

    while opcao == '3':


        interface.p_and_q()

        escolha = int(input('--> '))

        if escolha == 1:
            fh = open('p_and_q.txt')

            lista = list()

            for line in fh:
                line.rstrip()
                line = line.split()
                lista.extend(line)
            print('(p):{},(q):{},(e): {}'.format(int(lista[0]), int(lista[1]), int(lista[2]) ) )

        p = int(input('Digite (p): '))
        q = int(input('digite (q): '))
        e = int(input('Digite (e): '))

        phi = (int(p) - 1) * (int(q) - 1)
        e = int(e)
        n = int(p) * int(q)
        arquivo = open('mensagem_encriptada.txt')

        d = Calculos.linear(e, phi, array = list())

        Calculos.descriptografar(arquivo, d, n)
        break

    if int(opcao) > 3 or int(opcao) < 1 :
        break