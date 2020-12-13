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

    if opcao == '2':

        interface.cp()


        public_key = input("DIGITE O NOME DO ARQUIVO(SEM A EXTENSÃO): ")
        public_key = public_key + '.txt'
        chave = open(public_key)


        lst = list()

        for line in chave:
            line = line.rstrip()
            numbers = line.split()
            lst.extend(numbers)

        n = int(lst[0])
        e = int(lst[1])

        print("DIGITE UMA MENSAGEM PARA ENCRIPTAR:")

        msgn = input("--> ")

        msgn.upper()

        Calculos.codificar(msgn, e, n)

        Calculos.limpar_terminal()

        continue

    if opcao == '3':


        interface.p_and_q()

        escolha = int(input('-> '))

        if escolha == 1:

            fop = input('DIGITE O NOME DO ARQUVO(SEM EXTENSÕES): --> ')
            fop = fop + '.txt'
            fh1 = open(fop)

            lista = list()

            for line in fh1:
                line.rstrip()
                line = line.split()
                lista.extend(line)
            p = lista[0]
            q = lista[1]
            e = lista[2]

            print('\n')

        else:
            p = int(input('Digite (p): '))
            q = int(input('digite (q): '))
            e = int(input('Digite (e): '))

        phi = (int(p) - 1) * (int(q) - 1)
        e = int(e)
        n = int(p) * int(q)

        fh = input('DIGITE O NOME DO ARQUIVO(SEM A EXTENSÃO) A SER DESCRIPTADO: --> ')

        fh = fh + '.txt'
        arquivo = open(fh)

        d = Calculos.linear(e, phi)

        Calculos.descriptografar(arquivo, d, n)

        Calculos.limpar_terminal()
        continue

    if int(opcao) > 3 or int(opcao) < 1 :
        break
