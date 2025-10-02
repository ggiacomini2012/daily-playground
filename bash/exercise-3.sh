mkdir logs && touch logs/log_0{1..3}.txt

# Explicação: 
# Cria a pasta: O sistema tenta criar a pasta logs.

# Verifica o sucesso: Se a pasta foi criada com sucesso.

# Cria os arquivos: O sistema expande o {1..3} e, em seguida, 
# usa o comando touch para criar os três arquivos vazios: log_01.txt, 
# log_02.txt e log_03.txt dentro da nova pasta logs.