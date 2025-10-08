
#!/bin/bash

# Define o arquivo de log de entrada onde a busca será realizada.
ARQUIVO_ENTRADA="app.log"

# Define o arquivo de saída onde as linhas encontradas serão salvas.
ARQUIVO_SAIDA="error.log"

# Verifica se o arquivo de entrada existe antes de prosseguir.
if [ ! -f "$ARQUIVO_ENTRADA" ]; then
    echo "Erro: O arquivo de log de entrada ($ARQUIVO_ENTRADA) não foi encontrado."
    exit 1
fi

# ------------------------------------------------------------------
# Comando principal:
#
# 1. 'grep -i "error"': Procura pela palavra 'error'.
#    - A opção '-i' garante que a busca não diferencie maiúsculas de minúsculas
#      (encontra 'error', 'Error', 'ERROR', etc.).
# 2. '$ARQUIVO_ENTRADA': O arquivo onde a busca será feita ('app.log').
# 3. '>': O operador de redirecionamento. Ele sobrescreve o arquivo de saída.
# 4. '$ARQUIVO_SAIDA': O nome do arquivo para onde a saída será direcionada ('error.log').
# ------------------------------------------------------------------
grep -i "error" "$ARQUIVO_ENTRADA" > "$ARQUIVO_SAIDA"

# Confirmação para o usuário.
echo "Busca concluída. Todas as ocorrências de 'error' (ignorando maiúsculas/minúsculas) de '$ARQUIVO_ENTRADA' foram salvas em '$ARQUIVO_SAIDA'."