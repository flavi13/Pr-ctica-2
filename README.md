# Práctica-2

[Link del Repositorio](https://github.com/flavi13/Pr-ctica-2.git)


## Solucion

| Nº pasos | Simulacion        | Resolución matematica |
|----------|-------------------|-----------------------|
| 1        | 20                | 20.0                  |
| 2        | 46                | 46.0                  |
| 3        | 104               | 104.0                 |
| 5        | 544               | 544.0                 |
| 8        | 6576              | 6576.0                |
| 10       | 34432             | 34432.0               |
| 15       | 2140672           | 2140672.0             |
| 18       | 25881088          | 25881088.0            |
| 21       | 307302400         | 307302400.0           |
| 23       | 1609056256        | 1609056256.0          |
| 32       | 2792668987392     | 5235212288.0          |


### Primera aproximacion
Para plantear mejor el problema y verlo desde una prespectiva diferente al papel, lo primero que hemos hecho ha sido crear un algoritmo recursivo que simula los movimientos del caballo.

[simulation.py](codigo/simulation.py)

Salida:
```
Posibilidades validas para 1 movimientos: 20
Posibilidades validas para 2 movimientos: 46
Posibilidades validas para 3 movimientos: 104
Posibilidades validas para 5 movimientos: 544
Posibilidades validas para 8 movimientos: 6576
Posibilidades validas para 10 movimientos: 34432
Posibilidades validas para 15 movimientos: 2140672
Posibilidades validas para 18 movimientos: 25881088
Posibilidades validas para 21 movimientos: 307302400
Posibilidades validas para 23 movimientos: 1609056256
Posibilidades validas para 32 movimientos: 2792668987392
```

Como los resultados coinciden con la muestra del enunciado. Hemos tomado el resultado como bueno y hemos usado eso como base para plantear la formula matematica.

### Resolucion Matematica
![Matriz](/imagenes/matriz.jpg)

### Resolucion final
Ya con la formual matematica la hemos implementado en codigo para confirmar que los valores coinciden hasta los 32

[comprobacion.py](codigo/comprobacion.py)
Salida
```
Total de movimientos posibles en 1 pasos desde todas las casillas: 20.0
Total de movimientos posibles en 2 pasos desde todas las casillas: 46.0
Total de movimientos posibles en 3 pasos desde todas las casillas: 104.0
Total de movimientos posibles en 5 pasos desde todas las casillas: 544.0
Total de movimientos posibles en 8 pasos desde todas las casillas: 6576.0
Total de movimientos posibles en 10 pasos desde todas las casillas: 34432.0
Total de movimientos posibles en 15 pasos desde todas las casillas: 2140672.0
Total de movimientos posibles en 18 pasos desde todas las casillas: 25881088.0
Total de movimientos posibles en 21 pasos desde todas las casillas: 307302400.0
Total de movimientos posibles en 23 pasos desde todas las casillas: 1609056256.0
Total de movimientos posibles en 32 pasos desde todas las casillas: 5235212288.0
```

#### Desajuste
Como se puede observar en los resultados del cálculo matemático, el valor para 32 pasos no es preciso y parece encontrar una barrera que limita su crecimiento. Se realizaron simulaciones para valores más altos, y la simulación sigue el patrón de crecimiento exponencial esperado, mientras que el cálculo matemático no lo hace. Por esta razón, para valores mayores confiamos más en los resultados de la simulación. Esta imprecisión se debe al sistema que utilizan los ordenadores para realizar operaciones numéricas, y si no está adecuadamente preparado para manejar grandes cantidades, puede generar errores de precisión.