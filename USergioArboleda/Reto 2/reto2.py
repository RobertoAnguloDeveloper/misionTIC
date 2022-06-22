distancia, velMax, tiempo = input().split()
distancia = float(distancia)
velMax = float(velMax)
tiempo = float(tiempo)

velocidad = (3.6)*(distancia/tiempo)

if velocidad < 0 or velMax < 0 or tiempo < 0:
    print("ERROR")
elif velocidad > velMax:
    porcenExceso = 100*(velocidad - velMax)/velMax
    
    if porcenExceso >= 20:
        print("CURSO SENSIBILIZACION")
    else:
        print("MULTA")
else:
    print("OK")