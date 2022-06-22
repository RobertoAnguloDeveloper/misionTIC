cantidadBicicletas = int(input())

bicicletas = []
biciCorrecta = 0

for i in range(cantidadBicicletas):
    pedalier, biela, sillin, manilar, precio = input().split()

    pedalier = int(pedalier)
    biela = int(biela)
    sillin = int(sillin)
    manilar = int(manilar)
    precio = int(precio)

    bicicleta = []

    bicicleta.append(pedalier)
    bicicleta.append(biela)
    bicicleta.append(sillin)
    bicicleta.append(manilar)
    bicicleta.append(precio)

    bicicletas.append(bicicleta)

for i in range(len(bicicletas)):
    if bicicletas[i][0] > 240 and bicicletas[i][0] < 300:
        if bicicletas[i][1] >= 160 and bicicletas[i][1] <= 180:
            if bicicletas[i][2] >= 240 and bicicletas[i][2] <= 275:
                if bicicletas[i][3] <= 50:
                    biciCorrecta = bicicletas[i][4]

if biciCorrecta != 0:
    print(biciCorrecta)
else:
    print("NO DISPONIBLE")