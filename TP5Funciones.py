# # 1)
# def imprimir_hola_mundo():
#     print('Hola mundo')

# imprimir_hola_mundo()


# # 2) 
# def saludar_usuario(nombre):
#    print(f'Hola {nombre}')

# n = input('Ingresa tu nombre: ')
# saludar_usuario(n)


# # 3)
# def informacion_personal(nombre, apellido, edad, residencia):
#     print(f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}')

# n = input('Ingrese su nombre: ')
# a = input('Ingrese su apellido: ')
# e = input('Ingrese su edad: ')
# r = input('Ingrese su residencia: ')

# informacion_personal(n, a, e, r)


# # 4)
# import math

# def calcular_area_circulo(radio):
#     return math.pi * radio ** 2

# def calcular_perimetro_circulo(radio):
#     return 2 * math.pi * radio

# radio = float(input('Ingrese el radio del círculo: '))

# area = calcular_area_circulo(radio)
# perimetro = calcular_perimetro_circulo(radio)

# print(f'El área del círculo es: {area}')
# print(f'El perímetro del círculo es: {perimetro}')


# # 5)
# def segundos_a_horas(segundos):
#     return segundos/3600

# segundos = int(input('Ingrese la cantidad de segundos: '))
# horas = segundos_a_horas(segundos)
# print(f'Equivale a {horas} horas')


# # 6)
# def tabla_multiplicar(numero):
#     for i in range(1, 11):
#         print(f'{numero} x {i} = {numero * i}')

# num = int(input('Ingrese un número para ver su tabla de multiplicar: '))
# tabla_multiplicar(num)


# # 7)
# def operaciones_basicas(a, b):
#     suma = a + b
#     resta = a - b
#     mult = a * b
#     div = a / b 
#     print(f' Suma: {suma} \n Resta: {resta} \n Multiplicación: {mult} \n División: {div}')

# num1 = int(input('Ingresá el primer número: '))
# num2 = int(input('Ingresá el segundo número: '))

# operaciones_basicas(num1, num2)


# # 8)
# def calcular_imc(peso, altura):
#     imc = peso / (altura ** 2)
#     print(f'Tu índice de masa corporal es: {imc}')

# peso = float(input('Ingresa tu peso en kilogramos: '))
# altura = float(input('Ingresa tu altura en metros: '))

# calcular_imc(peso, altura)


# # 9)
# def celsius_a_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     print(f'{celsius}°C equivale a {fahrenheit}°F.')

# celsius = float(input('Ingresa la temperatura en grados Celsius: '))

# celsius_a_fahrenheit(celsius)


# # 10)
# def calcular_promedio(a, b, c):
#     promedio = (a + b + c) / 3
#     print(f'El promedio de los tres números es: {promedio}')

# a = float(input('Ingresa el primer número: '))
# b = float(input('Ingresa el segundo número: '))
# c = float(input('Ingresa el tercer número: '))

# calcular_promedio(a, b, c)
