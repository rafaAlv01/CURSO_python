a = 'A'
b = 'B'
c = 1.1

formato = 'a={}'.format(a, b, c)

#note que aqui que nas chaves de c={} há a expressão :.2f -> tradução: 
# : -> separa o índice ou nome do argumento das regras de formatação.
# .2f -> especifica a precisão em exatamente duas casas decimais (flutuante)
formatos = 'a={} b={} c={:.2f}'.format(a, b, c)

#Aqui, indica explicitamente a posição (índice) dos argumentos que você passa dentro do método .format()
string = 'a={0} b={1} c={nome3:.3f}'
formatao = string.format(a, b, nome3=c) #note que aqui há um parametro(nome3) e o argumento, que é o valor de c.

print(formato)
print(formatos)
print(formatao)

usuario = "admin"
tentativas = 3
tempo_bloqueio = 15.558

# Usando o formato posicional que vimos antes
mensagem = "Usuário {0} bloqueado após {1} tentativas. Tente novamente em {2:.1f} minutos.".format(
    usuario, tentativas, tempo_bloqueio
)
print(mensagem)