import random

try:
    # Código que pode gerar um erro: tentando converter uma string não numérica
    numero_randomico = random.randint(1, 2)
    if numero_randomico == 1:
        numero_inteiro = int('ABC')
    else:
        numero_inteiro = int('123')


    # Se a conversão for bem-sucedida (o que não será neste caso)
    print(f"Conversão bem-sucedida! O número é: {numero_inteiro}")

except ValueError:
    # O bloco 'except' é executado se um ValueError for gerado
    print("Ocorreu um erro!")
    print("Não é possível converter a string 'ABC' para um número inteiro (int).")
    print("O ValueError é capturado quando a função int() recebe um valor inválido.")
    
# Opcional: bloco 'else' é executado SE NENHUM erro ocorrer
else:
    print("Nenhum erro foi capturado no bloco try.")

# Opcional: bloco 'finally' é sempre executado, com ou sem erro
finally:
    print("Fim da tentativa de conversão.")