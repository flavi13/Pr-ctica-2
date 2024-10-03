import numpy as np

class Knight():    
    ALLOWED_MOVES = {
        0: [4, 6],
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [0, 3, 9],
        5: [],
        6: [0, 1, 7],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4],
    }
    
    def __init__(self):
        # Default Movement Matrix
        self.dmm = np.zeros((10, 10), dtype=int)
        
        # Rellenar la matriz de adyacencia
        for key, moves in Knight.ALLOWED_MOVES.items():
            for move in moves:
                self.dmm[key][move] = 1  
    
    def general_formula(self, f1, N):
        # Calcular la transpuesta de la matriz A
        A_T = np.transpose(self.dmm)
        
        # Elevar A_T a la potencia N-1
        A_T_power = np.linalg.matrix_power(A_T, N-1)
        
        # Multiplicar la matriz resultante por el vector f1
        f_N = np.dot(A_T_power, f1)
        
        return f_N
    
    def calculate_movements(self, steps):
        total_movements = 0
        
        # Iterar sobre las 10 posibles casillas iniciales (0 al 9)
        for start_position in range(10):
            # Vector f1 inicial, empezando en la casilla actual
            f1 = np.zeros(10)
            f1[start_position] = 1  # El caballo empieza en la casilla actual
            
            # Calcular movimientos posibles desde esta casilla
            result_vector = self.general_formula(f1, steps+1)
            
            # Sumar los movimientos posibles desde esta casilla
            total_movements += np.sum(result_vector)
        
        # Devolver el total de movimientos desde todas las casillas
        return total_movements

if __name__ == '__main__':
    example_values = [1,2,3,5,8,10,15,18,21,23,32]
    
    for steps in example_values:
        knight = Knight()
        total_movements = knight.calculate_movements(steps)
        print(f"Total de movimientos posibles en {steps} pasos desde todas las casillas: {total_movements}")