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

# Verificar si se ha pasado el argumento como número
if len(sys.argv) == 1:  # Si no se ha pasado ningún argumento
    # Solicitar el número al usuario
    num = int(input("Por favor ingrese un número: "))
else:
    num = int(sys.argv[1])  # Si el número fue pasado como argumento

print(f"Factorial de {num}! es {factorial(num)}")


