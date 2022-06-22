nombreEstudiante = input("Ingrese su nombre completo: ")
nombreAsignatura = input("Ingrese el nombre de la asignatura: ")
promedio = 0.0
suma = 0.0

nota = float(input("Ingrese la nota [1]: "))
suma += nota
nota = float(input("Ingrese la nota [2]: "))
suma += nota
nota = float(input("Ingrese la nota [3]: "))
suma += nota


promedio = suma / 3

print("Hola "+nombreEstudiante+" el promedio de "+nombreAsignatura+" es:",promedio)

if promedio > 3.5 and promedio < 4.0:
    print("Aprobaste", nombreAsignatura)
elif promedio > 4.0:
    print("Excelente "+nombreEstudiante+" eres sobresaliente en", nombreAsignatura)
else:
    print("Reprobaste", nombreAsignatura)