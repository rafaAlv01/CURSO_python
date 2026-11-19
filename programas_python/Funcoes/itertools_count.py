#count é um iterador sem fim
#A diferença entre count e range é que count conta até o infinito, não tem como delimitar um fim.

from itertools import count

c1 = count()

for i in c1:
    if i > 100:
        break
    #print(i)

#Note que c1(102), mas esse 102 é o proximo valor que o iterador vai retornar. O ultimo gerado foi o 101, que foi o valor de parada do comando de repetição acima.
print(f'O valor do count() depois de passar pelo for: {c1}\n')
print(f'O valor de c1 depois de chamar next() : {c1.__next__(), c1}\n') 

c2 = count(50, 10) #Aqui a contagem começa do valor 50 e pula de 10 em 10.

for i in c2:
    if i > 100:
        break

print(f'c1 = {c1}, c2(com start and step) = {c2}\n')