numRegistros = int(input())
lista = []
disponibles = []
noDisponibles = []


for i in range(numRegistros):
    altura, bielas, sillin, manilar, valor = input().split()
    altura = int(altura)
    bielas = int(bielas)
    sillin = int(sillin)
    manilar = int(manilar)
    valor = int(valor)
    lista.append([altura, bielas, sillin, manilar, valor])

for i in range(len(lista)):
    if (lista[i][0] >= 240 and lista[i][0] <= 300) and (lista[i][1] >= 160 and lista[i][1] <= 180) \
        and (lista[i][2] >= 240 and lista[i][2] <= 275) and (lista[i][3] >= 0 and lista[i][3] <= 50):
        disponibles.append(lista[i][4])
    else:
        noDisponibles.append(lista[i][4])

if len(lista) == len(noDisponibles):
    print("NO DISPONIBLE")
else:
    print(disponibles[0])