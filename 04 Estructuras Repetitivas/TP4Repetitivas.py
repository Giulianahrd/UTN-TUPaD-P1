# # 1)
# for i in range(101):
#     print(i)


# # 2)
# for i in range(1):
#     num = input('Ingrese un número: ')
#     print(f'El número ingresado tiene {len(num)} digitos.')


# # 3)
# a = int(input(Ingrese el primer número: '))
# b = int(input('Ingrese el segundo número: '))

# inicio = min(a, b) + 1
# fin = max(a, b)

# suma = 0
# for i in range(inicio, fin):
#     suma += i
# print('La suma de los números entre', a, 'y', b, 'es:', suma)


# # 4)
# num = 1
# suma = 0
# while num != 0:
#     num = int(input('Ingrese un número: '))
#     suma += num
#     print(suma) 


# # 5)
# import random

# numero_aleatorio = random.randint(0, 9)
# intentos = 0
# num = -1  

# while num != numero_aleatorio:
#     num = int(input('Adivina el número entre 0 y 9: '))
#     intentos += 1

# print(f'Adivinaste el número en {intentos} intentos.')


# # 6)
# for numero in range(100, -1, -2):
#     print(numero)

# # 7)
# a = 0
# b = int(input('Ingrese un número: '))
# suma = 0

# for i in range(a, b + 1):
#     suma += i
# print('La suma de los números entre', a, 'y', b, 'es:', suma)


# # 8)
# cantidad = 100  

# pares = 0
# impares = 0
# positivos = 0
# negativos = 0

# for i in range(cantidad):
#     numero = int(input(1'Ingrese un número: '))
#     i+=1
#     if numero % 2 == 0:
#         pares += 1
#     else:
#         impares += 1
    
#     if numero > 0:
#         positivos += 1
#     elif numero < 0:
#         negativos += 1

# print('\nResumen:')
# print('Cantidad de pares:', pares)
# print('Cantidad de impares:', impares)
# print('Cantidad de positivos:', positivos)
# print('Cantidad de negativos:', negativos)



# # 9)
# suma = 0
# cantidad = 100

# for i in range(cantidad):
#     numero = int(input('Ingrese el número: '))
#     suma += numero  

# media = suma / cantidad
# print('La media es:', media)


# # 10)
# numero = input('Ingrese un número: ')
# invertido = ''

# for i in range(len(numero)-1, -1, -1):
#     invertido += numero[i]

# print('Número invertido:', invertido)
