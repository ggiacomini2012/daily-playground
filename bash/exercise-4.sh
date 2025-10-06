#!/bin/bash

# Este script usa o comando 'find' para localizar todos os arquivos com a extensão '.log'
# no diretório atual (representado por '.') e em todos os subdiretórios.

# Explicação detalhada do comando:
# find:     Inicia a busca por arquivos.
# .:        Especifica que a busca deve começar no diretório atual.
# -name:    O critério de busca é baseado no nome do arquivo.
# "*.log":  O padrão de busca. O '*' é um wildcard (curinga) que corresponde
#           a zero ou mais caracteres, garantindo que qualquer nome
#           seguido por '.log' seja encontrado.

find . -name "*.log"