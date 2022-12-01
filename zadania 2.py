from copy import deepcopy
from random import randint
def lista_slownikow():
    n = int(input('n = '))
    lista = []
    for i in range(n):
        dic = {}
        dic.update({'Matematyka':[randint(1,6) for i in range(randint(3,9))]})
        dic.update({'Angielski':[randint(1,6) for i in range(randint(3,9))]})
        dic.update({'Informatyka':[randint(1,6) for i in range(randint(3,9))]})
        lista.append(dic)
    return lista
 
moja_lista_słowników_1 = lista_slownikow()

 
def zamiana(lista):
    lista = lista.copy()
    i = 0
    while i < len(lista):
        if lista[i] >= 2 and lista[i] <= 6:
            lista.pop(i)
            lista.insert(i,1)
        i+= 1
    return lista
 
moja_lista_słowników_2 = deepcopy(moja_lista_słowników_1)
for dic in moja_lista_słowników_2:
    for k,v in dic.items():
        if k == 'Matematyka':
                v = zamiana(v)
                dic.update({'Matematyka':v})
        elif k == 'Angielski':
                v = zamiana(v)
                dic.update({'Angielski':v})
        elif k == 'Informatyka':
                v = zamiana(v)
                dic.update({'Informatyka':v})
print(moja_lista_słowników_1)
print('-'*50)
print(moja_lista_słowników_2)




def remove_1_6 (lista):
    lista = lista.copy()
    i = 0
    while len(lista) > i:
        if lista[i] == 1 or lista[i] == 6:
            lista.pop(i)
            i = 0
        else:
            i += 1
    return lista
 
lista_wyników = []
for dic in moja_lista_słowników_1:
    sum_k = 0
    lista_sr = []
    for v,k in dic.items():
        k = remove_1_6(k)
        sum_k = sum(k)
        lista_sr.append(sum_k/len(k))
        sum_k = 0
    lista_wyników.append(sum(lista_sr)/len(lista_sr))
my_max = max(lista_wyników)
my_min = min(lista_wyników)
for i in range(len(lista_wyników)):
    print('Index {0} - średnia {1}'.format(i,lista_wyników[i]))
print('-'*40)
print(f'MAX! {lista_wyników.index(my_max)} \t {my_max}')
print(f'MIN! {lista_wyników.index(my_min)} \t {my_min}')