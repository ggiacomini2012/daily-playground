def calcular_fatorial_for(n):
    """
    Calcula o fatorial de um número inteiro não negativo (n!) usando um laço 'for'.

    O fatorial de um número n é o produto de todos os inteiros positivos menores
    ou iguais a n.
    Fatorial de 0 é definido como 1.

    Args:
        n (int): O número inteiro não negativo cujo fatorial será calculado.
                 Recomendado para números pequenos (ex: n <= 15).

    Returns:
        int: O valor do fatorial de n.

    Raises:
        ValueError: Se n for um número negativo.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("O fatorial é definido apenas para números inteiros não negativos.")

    if n == 0:
        return 1
    
    # Inicializa o resultado com 1
    fatorial = 1
    
    # O laço 'for' itera de 1 até n (inclusive)
    for i in range(1, n + 1):
        # Multiplica o resultado pelo número atual
        fatorial *= i  # É o mesmo que: fatorial = fatorial * i
        
    return fatorial

# Exemplos de uso:
print(f"O fatorial de 5 é: {calcular_fatorial_for(5)}")
print(f"O fatorial de 0 é: {calcular_fatorial_for(0)}")
print(f"O fatorial de 7 é: {calcular_fatorial_for(7)}")

# Exemplo de número maior (o resultado cresce rapidamente):
print(f"O fatorial de 10 é: {calcular_fatorial_for(10)}")

# Exemplo de erro (número negativo):
try:
    print(f"O fatorial de -1 é: {calcular_fatorial_for(-1)}")
except ValueError as e:
    print(f"Erro: {e}")