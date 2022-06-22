# import os
# archivo = open("prueba.txt", "w")
# archivo.write("Hola Mundo\nQue nota\nCiao")
# archivo.close()

# os.remove("prueba.txt")

# lista = input().split()
# listaInvertida = []
# for i in range(len(lista)-1, -1, -1):
#     listaInvertida.append(lista[i])

# print("Lista original")
# print(lista)
# print("Lista invertida")
# print(listaInvertida)

# listaNueva = []

# for i in lista:
#     for j in lista:
#         listaNueva.append(i+j)

# print(listaNueva)

# cadena = input("Digite la cadena: ").split()
# j = 0
# cadenaNew = ""
# for i in cadena:
#     cadena[j]=i.capitalize()
#     cadenaNew += cadena[j] + " "
#     j += 1
# print(cadenaNew)

# longitud = int(input("Ingrese la longitud de la serie fibonacci: "))
# fibonacci = [0,1]

# for i in range(2, longitud):
#     fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

# print(fibonacci)

# # Build fibonacci program using recursion
# def fibonacci(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(10))  

# nombre = input()
# print(len(nombre))

# longitud = int(input())

# ultimo = 0
# penultimo = 1
# aux = 0

# for i in range(longitud):
#     print(aux, end=" ")
#     aux = ultimo + penultimo
#     penultimo = ultimo
#     ultimo = aux

# a = 0
# print(a)
# a += 1
# a += 1
# print(a)
# a =+ 1
# a =+ 1
# print(a)