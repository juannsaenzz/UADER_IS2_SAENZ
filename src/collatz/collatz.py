import matplotlib.pyplot as plt

def collatz_iterations(n):
    """
    Función que calcula el número de iteraciones para que un número 'n'
    converja a la secuencia repetitiva 4, 2, 1 según la conjetura de Collatz.
    """
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2  # Si el número es par, lo dividimos entre 2
        else:
            n = 3 * n + 1  # Si el número es impar, lo multiplicamos por 3 y sumamos 1
        count += 1
    return count

# Almacenar los resultados
numeros = []
iteraciones = []

for i in range(1, 10001):
    iteraciones.append(collatz_iterations(i))
    numeros.append(i)

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(iteraciones, numeros, 'b.', markersize=1)  # Graficar los resultados
plt.title('Número de iteraciones de la Conjetura de Collatz (1-10000)')
plt.xlabel('Número de iteraciones')
plt.ylabel('Número inicial (n)')
plt.grid(True)
plt.show()
