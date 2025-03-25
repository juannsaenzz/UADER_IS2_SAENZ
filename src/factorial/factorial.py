#!/usr/bin/python  
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

# Función para manejar el rango "desde-hasta" o "hasta"
def procesar_rango(rango):
    # Si el rango tiene el formato "desde-" o "-hasta"
    if '-' in rango:
        partes = rango.split('-')
        if partes[0] == '':  # Caso para rango "-hasta"
            try:
                fin = int(partes[1])
                return 1, fin  # Desde 1 hasta el número indicado
            except ValueError:
                print("Error en el rango especificado. Ejemplo: '-10'.")
                sys.exit()
        elif partes[1] == '':  # Caso para rango "desde-"
            try:
                inicio = int(partes[0])
                return inicio, 60  # Desde el número indicado hasta 60
            except ValueError:
                print("Error en el rango especificado. Ejemplo: '5-'.")
                sys.exit()
    else:  # Si el rango tiene el formato "desde-hasta"
        try:
            inicio, fin = map(int, rango.split('-'))
            if inicio > fin:
                print("El valor 'desde' no puede ser mayor que 'hasta'.")
                sys.exit()
            return inicio, fin
        except ValueError:
            print("Formato de rango incorrecto. Debe ser 'desde-hasta' (por ejemplo, 4-8) o '-hasta' o 'desde-'.")
            sys.exit()

# Verificar si se ha pasado el argumento como número
if len(sys.argv) == 1:  # Si no se ha pasado ningún argumento
    # Solicitar el rango al usuario
    rango = input("Por favor ingrese un rango de números (desde-hasta o -hasta o desde-): ")
    inicio, fin = procesar_rango(rango)
else:
    # Si el argumento fue pasado como 'desde-hasta'
    rango = sys.argv[1]
    inicio, fin = procesar_rango(rango)

# Calcular y mostrar los factoriales para el rango
for num in range(inicio, fin + 1):
    print(f"Factorial de {num}! es {factorial(num)}")
