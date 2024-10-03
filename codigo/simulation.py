import numpy as np

# Matriz de adyacencia del teclado numérico
matriz_adyacencia = np.array([
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],  # Desde el 0: va al 4 y al 6
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],  # Desde el 1: va al 6 y al 8
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],  # Desde el 2: va al 7 y al 9
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],  # Desde el 3: va al 4 y al 8
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],  # Desde el 4: va al 0, 3 y 9
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Desde el 5: no tiene movimientos
    [1, 1, 0, 0, 0, 0, 0, 1, 0, 0],  # Desde el 6: va al 0, 1 y 7
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],  # Desde el 7: va al 2 y al 6
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # Desde el 8: va al 1 y al 3
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],  # Desde el 9: va al 2 y al 4
])

def contar_rutas(pasos):
    # Potencia de la matriz de adyacencia
    matriz_potencia = np.linalg.matrix_power(matriz_adyacencia, pasos)
    
    # Sumar todas las rutas posibles desde cualquier dígito (0 a 9)
    total_rutas = np.sum(matriz_potencia)
    
    return total_rutas

# Leer el número de pasos
pasos = int(input("Número de pasos: "))

# Calcular y mostrar el número total de rutas posibles
print("Total de rutas posibles:", contar_rutas(pasos))
