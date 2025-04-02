# # 1)
# edad = int(input('Ingrese su edad: '))
# if edad >= 18:
#     print('Sos mayor de edad')


# # 2)
# aprobado = 6
# nota = float(input('Ingrese su nota: '))
# if nota >= aprobado:
#     print('Aprobado')
# else:
#     print('Desaprobado')


# # 3)
# num = int(input('Ingrese un número par: '))
# if num % 2 == 0:
#     print('Ha ingresado un número par')
# else:
#     print('Por favor, ingrese un número par')


# # 4)
# edad = int(input('Ingrese su edad: '))
# if edad < 12:
#     print('Eres un niño')
# elif edad >= 12 and edad < 18:
#     print('Eres un adolescente')
# elif edad >= 18 and edad < 30:
#     print('Eres un adulto joven')
# elif edad >= 30:
#     print('Eres un adulto')


# # 5)
# password = input('Ingrese una contraseña entre 8 y 14 caracteres: ')
# auth = len(password) >= 8 and len(password) <= 14
# if auth:
#     print('Ha ingresado una contraseña correcta')
# else: 
#     print('Por favor, ingrese una contraseña de entre 8 y 14 caracteres')


# # 6)
# from statistics import mode, median, mean
# import random

# num_random = [random.randint(1, 100) for i in range(50)]
# moda = mode(num_random)
# mediana = median(num_random)
# media = mean(num_random)

# if media > mediana > moda:
#     print('Hay sesgo positivo')
# elif media < mediana < moda:
#     print('Hay sesgo negativo')
# elif media == mediana == moda:
#     print('No hay sesgo')


# # 7)
# text = input('Ingrese una frase o palabra: ')
# vocal = 'aeiouAEIOU'

# if text[-1] in vocal: 
#     print(f'{text}!')
# else:
#     print(text)


# # 8)
# name = input('Ingrese su nombre: ')
# option = int(input(
#                 'Ingrese 1 si quiere su nombre en mayúsculas\n'
#                 'Ingrese 2 si quiere su nombre en minúsculas\n'
#                 'Ingrese 3 si queire su nombre con la primera letra en mayúscula\n'
#             ))

# if option == 1:
#     print(name.upper())
# elif option == 2:
#     print(name.lower())
# elif option == 3:
#     print(name.capitalize())


# # 9)
# magnitud = float(input('Ingrese la magnitud del terremoto: '))

# if magnitud < 3:
#     print('Muy leve (imperceptible)')
# elif magnitud < 4:
#     print('Leve (ligeramente perceptible)')
# elif magnitud < 5:
#     print('Moderado (sentido por personas, pero generalmente no causa daños)')
# elif magnitud < 6:
#     print('Fuerte (puede causar daños en estructuras débiles)')
# elif magnitud < 7:
#     print('Muy Fuerte (puede causar daños significativos)')
# else:
#     print('Extremo (puede causar graves daños a gran escala)')


# # 10)
# hemisferio = input('Ingrese el hemisferio en el que se encuentra (N/S): ').strip().upper()
# mes = int(input('Ingrese el número del mes (1-12): '))
# dia = int(input('Ingrese el día del mes: '))

# if hemisferio == 'N': 
#     if (mes == 12 and dia >= 21) or (1 <= mes <= 3 and not (mes == 3 and dia > 20)):
#         estacion = 'Invierno'
#     elif (mes == 3 and dia >= 21) or (4 <= mes <= 6 and not (mes == 6 and dia > 20)):
#         estacion = 'Primavera'
#     elif (mes == 6 and dia >= 21) or (7 <= mes <= 9 and not (mes == 9 and dia > 20)):
#         estacion = 'Verano'
#     else:
#         estacion = 'Otoño'
# elif hemisferio == 'S': 
#     if (mes == 12 and dia >= 21) or (1 <= mes <= 3 and not (mes == 3 and dia > 20)):
#         estacion = 'Verano'
#     elif (mes == 3 and dia >= 21) or (4 <= mes <= 6 and not (mes == 6 and dia > 20)):
#         estacion = 'Otoño'
#     elif (mes == 6 and dia >= 21) or (7 <= mes <= 9 and not (mes == 9 and dia > 20)):
#         estacion = 'Invierno'
#     else:
#         estacion = 'Primavera'

# print(f'La estación en la que te encuentras es: {estacion}')
