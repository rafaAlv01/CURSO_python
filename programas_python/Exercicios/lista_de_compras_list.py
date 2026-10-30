'''
    Faça uma lista de compras com listas.
    O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista.
    Não permita que o programa quebre com erros de índices inexistentes na lista.
'''
import os
import msvcrt #modulo que lida com teclado e o buffer do console

#FUNÇAO CRIADA PARA LIMPAR BUFFER DE ENTRADA DE DADOS.
def aguardar_tecla():
    while msvcrt.kbhit(): #enquanto houver teclas acumuladas no buffer
        msvcrt.getch() #cada uma será consumida.
    msvcrt.getch()

entradas_validas = "ial"
lista_compras = []

while True:
    os.system("cls")
    print('Selecione uma opção')
    entrada = input('[i]nserir [a]pagar [l]istar : ')

    if(entrada not in entradas_validas):
        print('[entrada inválida!]')
        aguardar_tecla()
        continue

    if entrada == 'i' :
        lista_compras.append(input('Valor: '))
    elif entrada == 'a':
        indice_apagar = input('Escolha um índice para apagar: ')
        try:
            indice_apagar_int = int(indice_apagar)
            
            if indice_apagar_int < 0 :
                print('índice inválido.')
                aguardar_tecla()
                continue
            
            lista_compras.pop(indice_apagar_int)

            print('Item apagado com sucesso.')
            aguardar_tecla()

        except ValueError:
            print('Por favor, digite um número inteiro.')
            aguardar_tecla()
            continue
        except IndexError:
            print('Índice não existe na lista.')
            aguardar_tecla()
            continue
    else:
        if not lista_compras:
            print('Lista vazia.')
            aguardar_tecla()
            continue

        for indice, item in enumerate(lista_compras):
            print(indice, item)

        print('Pressione qualquer tecla para voltar...')
        aguardar_tecla()
        
