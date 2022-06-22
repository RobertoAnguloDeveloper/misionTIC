ciclo = True
while(ciclo):
    try:
        num = int(input("Ingrese un numero entero: "))
        print(num**2)
        ciclo = False
    except ValueError:
        print("El valor ingresado no es un numero entero")
        ciclo = True