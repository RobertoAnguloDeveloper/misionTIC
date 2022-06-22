distancia, velocidadMaxima, tiempo = input().split()
distancia = int(distancia)
velocidadMaxima = int(velocidadMaxima)
tiempo = int(tiempo)

distancia = distancia/1000 #En kilometros
tiempo = tiempo/3600 #En horas

velocidadMedia = distancia/tiempo

if velocidadMedia < velocidadMaxima and velocidadMedia > 0:
    print("OK")
elif velocidadMedia < 0:
    print("ERROR")
else:
    porcentajeExceso = ((velocidadMedia - velocidadMaxima)*(100))/velocidadMaxima
    if porcentajeExceso < 20:
        print("MULTA")
    else:
        print("CURSO SENSIBILIZACION")