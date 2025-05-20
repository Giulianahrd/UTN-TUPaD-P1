## 1)
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# num = int(input("Ingresa un número entero mayor que 0: "))

# for i in range(1, num + 1):
#     print(f"Factorial de {i} es {factorial(i)}")



# # 2)
# def fibonacci_recursivo(pos):
#     if pos == 0:
#         return 0
#     elif pos == 1:
#         return 1
#     else:
#         return fibonacci_recursivo(pos - 1) + fibonacci_recursivo(pos - 2)

# n = int(input("Ingresa la posición hasta la cual deseas ver la serie de Fibonacci: "))

# print("Serie de Fibonacci:")
# for i in range(n + 1):
#     print(fibonacci_recursivo(i))




# # 3)
# def potencia(base, exponente):
#     if exponente == 0:
#         return 1
#     else:
#         return base * potencia(base, exponente - 1)

# base = int(input("Ingresa la base: "))
# exponente = int(input("Ingresa el exponente: "))

# resultado = potencia(base, exponente)
# print(f"{base} elevado a la {exponente} es: {resultado}")




# 4)
# def decimal_a_binario(n):
#     if n == 0:
#         return ""
#     else:
#         return decimal_a_binario(n // 2) + str(n % 2)

# def convertir_a_binario(n):
#     if n == 0:
#         return "0"
#     return decimal_a_binario(n)

# numero = int(input("Ingresa un número entero positivo: "))
# binario = convertir_a_binario(numero)
# print(f"El número {numero} en binario es: {binario}")




# # 5)
# def es_palindromo(palabra):
#     if len(palabra) <= 1:
#         return True

#     if palabra[0] != palabra[-1]:
#         return False

#     return es_palindromo(palabra[1:-1])




# # 6)
# def suma_digitos(n):
#     if n < 10:
#         return n
#     else:
#         return n % 10 + suma_digitos(n // 10)





# # 7)
# def contar_bloques(n):
#     if n == 0:
#         return 0
#     else:
#         return n + contar_bloques(n - 1)





# # 8)
# def contar_digito(numero, digito):
#     if numero == 0:
#         return 0
#     else:
#         ultimo = numero % 10
#         contador = 1 if ultimo == digito else 0
#         return contador + contar_digito(numero // 10, digito)

