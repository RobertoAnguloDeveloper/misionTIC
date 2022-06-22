cantidadBicicletas = int(input())
baseDeDatos = []
precioBicicletaDisponible = 0

for i in range(cantidadBicicletas):
    bicicleta = input().split()

    for j in range(len(bicicleta)):
        bicicleta[j] = int(bicicleta[j])

    baseDeDatos.append(bicicleta)

for i in range(len(baseDeDatos)):
    if baseDeDatos[i][0] > 240 and baseDeDatos[i][0] < 300:
        if baseDeDatos[i][1] > 160 and baseDeDatos[i][1] < 180:
            if baseDeDatos[i][2] >= 240 and baseDeDatos[i][2] <= 275:
                if baseDeDatos[i][3] <= 50:
                    precioBicicletaDisponible = baseDeDatos[i][4]
    
if precioBicicletaDisponible != 0:
    print(precioBicicletaDisponible)
else:
    print("NO DISPONIBLE")