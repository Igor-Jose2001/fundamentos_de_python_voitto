# Questão 1 - Lista dos Quadrados dos números pares de 1 a 10
lista_pares = []
for i in range(1,11):
    if i%2 == 0:
        lista_pares.append(i**2)
print(lista_pares)

# Questão 1 - Utilizando List Comprehension
lc_pares = [i**2 for i in range(1,11) if i%2 == 0]

# Questão 2 - Raízes dos Números de 10 a 20
def raizes(numeros, f):
    num_raizes = []
    for i in numeros:
        num_raizes.append(f(i))
    return num_raizes

lista_num = range(10,21)
r = raizes(lista_num, lambda x:x**(1/2))
print(r)

# Questão 3 - Plotar Gráficos
def quadrados(inicio, fim):
    l = range(inicio, fim+1)
    #Quadrados
    q = [i**2 for i in l]
    return l,q

num, quad = quadrados(1,10)
print(list(num),quad)

import matplotlib.pyplot as plt
plt.plot(num)
plt.plot(quad)
plt.show()
