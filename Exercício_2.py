# Questão 1 
import random
lista_aleatoria = [random.randint(1,100) for i in range(50)]
print (lista_aleatoria)

#Copiar a Lista anterior utilizando o laço for
lista_aleatoria2 = list()
for i in lista_aleatoria:
    lista_aleatoria2.append(i)

# Questão 2

# Plotar um Histograma do vetor aleatório criado
import matplotlib as plt
plt.hist(lista_aleatoria)
plt.show()


# Questão 3

# Receber uma lista como parâmetro e retorna uma lista em ordem crescente
def ordenaLista (lista):
    for i in range(1, len(lista)):
        x = lista[i]
        k = i
        while k > 0 and x < lista[k-1]:
            lista[k] = lista[k-1]
            k = k-1
        lista[k] = x
    return lista

print(lista_aleatoria)
lista_ordenada = ordenaLista(lista_aleatoria)
print(lista_ordenada)

# Questão 4

# Medidas de Tendência Central

# Cálculo da Média
soma = 0
for i in lista_aleatoria:
    soma += i

media = soma/(len(lista_aleatoria))

# Cálculo da Mediana 
mediana = 0
if len(lista_ordenada) % 2 == 1:
    mediana = lista_ordenada[(len(lista_ordenada) - 1)//2]
else:
    mediana = (lista_ordenada[(len(lista_ordenada) - 1)//2] + 
               lista_ordenada[len(lista_ordenada)//2])//2
    
# Cálculo da Moda - Não estamos levando em conta caso multimodais
valorAtual = lista_ordenada[0]
moda = lista_ordenada[0]
cont = 1
max_cont = 0

for x in lista_ordenada[1:]:
    if x == valorAtual:
        cont += 1
        if cont > max_cont:
            max_cont = cont
            if x != moda:
                moda = x
    else:
        cont = 1
        valorAtual = x

# Cálculo do Desvio Padrão
import math

media = sum(lista_ordenada)/len(lista_ordenada)
dif_media = [(media - x)**2 for x in lista_ordenada]
devpad = math.sqrt(sum(dif_media)/len(dif_media))

# Cálculo da Variância
var = devpad**2

# Dicionário
valores_centrais = {"media": media, 
                    "mediana": mediana, 
                    "moda": moda, 
                    "desvio padrão": devpad, 
                    "variância": var
                    }

# Salvando em um arquivo o dicionário
arquivo = open("informacoes.txt", "w")
arquivo.write(str(valores_centrais))
arquivo.close()



