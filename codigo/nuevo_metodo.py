from functools import lru_cache

movimientos = {
    0: [6, 4],
    1: [6, 8],
    2: [7, 9],
    3: [4, 8],
    4: [3, 9, 0],
    5: [],
    6: [1, 7, 0],
    7: [2, 6],
    8: [1, 3],
    9: [2, 4]
}

# Usamos lru_cache para memorizar los resultados de calcular()
@lru_cache(None)
def calcular(inicio, pasos):
    if pasos == 0:
        return 0
    
    movs = 0
    for siguiente in movimientos[inicio]:
        movs += 1 + calcular(siguiente, pasos - 1)

    return movs

def totalizar(pasos):
    total = 0
    _total = 0
    
    for i in range(10):
        total += calcular(i, pasos)
        if pasos > 1:
            _total += calcular(i, pasos - 1)
        else: _total += 1
    
    return total - _total


#print('Options: '.format(totalizar(input('Steps: '))))

print('Options: {}'.format(str(totalizar(int(input('Steps: '))))))

