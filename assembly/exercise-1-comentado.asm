section .data
    ; Dados não inicializados ou constantes podem ir aqui.
    ; (Não há dados para este exemplo simples)

section .text
    ; Ponto de entrada do programa: global _start
    global _start

_start:
    ; 1. Operação Sequencial
    ; O EIP aponta para esta instrução (EIP -> INI_CALC)
INI_CALC:
    mov eax, 10       ; Move o valor 10 para o registrador EAX
                      ; O EIP é incrementado para apontar para a próxima instrução
    add eax, 5        ; Adiciona 5 ao EAX (EAX agora é 15)
                      ; O EIP é incrementado para apontar para a próxima instrução

    ; 2. Instrução de Desvio Condicional (Salto)
    ; O EIP aponta para 'jmp PULAR'
    jmp FIM           ; Salta incondicionalmente para o rótulo FIM
                      ; O EIP é diretamente sobrescrito para apontar para FIM

    ; 3. Código Ignorado
    ; O EIP NUNCA apontará para esta instrução devido ao 'jmp FIM'
IGNORADO:
    sub eax, 2        ; Subtrai 2 de EAX (Se fosse executado, EAX seria 13)

    ; 4. Finalização do Programa (Destino do Salto)
FIM:
    ; O EIP agora aponta para esta seção, continuando a execução
    
    ; Código para encerrar o programa (Chamada de sistema 'exit' do Linux)
    mov ebx, 0        ; Código de saída (0 = Sucesso)
    mov eax, 1        ; Número da chamada de sistema 'exit'
    int 0x80          ; Executa a chamada de sistema (o programa termina)