def knight_dialer(N):
    # Posibles movimientos desde cada posicion
    moves = {
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

    # Creamos una tabla para guardar los resultados
    dp = [ [0]*10 for _ in range(N+1)]
    for digit in range(10):
        dp[0][digit] = 1

    # Ejecutamos el algoritmo el numero pedido de veces
    for n in range(1, N+1):
        for digit in range(10):
            dp[n][digit] = 0  # Initialize for current n
        for prev_digit in range(10):
            for digit in moves[prev_digit]:
                dp[n][digit] += dp[n-1][prev_digit]

    # Suma todos los valores de la tabla
    total_sequences = sum(dp[N][digit] for digit in range(10))
    return total_sequences

valid_values = [1,2,3,5,8,10,15,18,21,23,32,50]
for N in valid_values:
    total_sequences = knight_dialer(N)
    print(f"Posibilidades validas para {N} movimientos: {total_sequences}")

