distancia, velocidadMaxima, tiempo = input().split()

distancia = int(distancia)
velocidadMaxima = int(velocidadMaxima)
tiempo = int(tiempo)

distancia = distancia/1000 #En kilometros
tiempo = (tiempo/60)/60 #En horas

velocidadMedia = distancia/tiempo

if velocidadMedia < velocidadMaxima and velocidadMedia > 0:
    print("OK")
elif velocidadMedia < 0 or distancia < 0 or velocidadMaxima < 0 or tiempo < 0:
    print("ERROR")
else:
    exceso = velocidadMedia - velocidadMaxima
    porcentaje = (exceso*100)/velocidadMaxima

    if porcentaje < 20:
        print("MULTA")
    elif porcentaje >= 20:
        print("CURSO SENSIBILIZACION")