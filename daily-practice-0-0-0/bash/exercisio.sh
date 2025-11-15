#!/bin/bash

# Exercício de Sintaxe Bash

# 1. Crie uma variável chamada `NOME` e atribua seu nome a ela.
# Dica: NOME="Seu Nome"
NOME="Gui"

# 2. Imprima a variável `NOME` na tela.
# Dica: Use o comando `echo` com a variável.
echo "Meu nome é $NOME"


# 3. Crie uma variável chamada `DATA_ATUAL` que armazena a data atual.
# Dica: Use o comando `date` com substituição de comando. Ex: VARIAVEL=$(comando)
DATA_ATUAL=$(date +"%d/%m/%Y")
# isso funciona porque o comando date retorna a data atual no formato especificado
# +"%d/%m/%Y" formata a data para dia/mês/ano


# 4. Imprima a data atual na tela, com uma mensagem amigável.
# Ex: "Hoje é: [data]"
echo "Hoje é: $DATA_ATUAL"

# 5. Crie um loop `for` que imprima os números de 1 a 5.
# Dica: for i in {1..5}; do ... done
#6. Dentro do loop, imprima o dobro de cada número.
# Dica: Use a expressão $((i * 2)) para calcular o dobro.
for index in {1..5}; do
    echo "$index) O dobro é $((index * 2))"
done




# --- Escreva seu código abaixo ---
