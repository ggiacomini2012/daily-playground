; ----------------------------------------------------------------------
; Nome: mov_exemplo.asm
; Descrição: Exemplo simples da instrução MOV em Assembly x86 (32 bits)
; Assemble: nasm -f elf mov_exemplo.asm -o mov_exemplo.o
; Link: ld -m elf_i386 mov_exemplo.o -o mov_exemplo
; Executar: ./mov_exemplo
; ----------------------------------------------------------------------

section .text
    global _start

_start:
    ; 1. MOV Imediato para Registrador
    ; Define o valor inicial de EBX como 10 (decimal).
    ; EBX = 10
    mov ebx, 10     ; Note: o '10' é um valor imediato.

    ; 2. MOV Registrador para Registrador
    ; Copia o valor de EBX para EAX.
    ; EAX = EBX (agora EAX também é 10)
    mov eax, ebx

    ; 3. MOV para a chamada de sistema (Syscall)
    ; O kernel Linux (32 bits) espera o número da função no registrador EAX.
    ; O número 1 é para a função 'exit' (sair do programa).
    ; EAX = 1
    mov eax, 1      ; Altera EAX de 10 para 1 (Syscall 'exit')

    ; 4. MOV para o código de saída (exit code)
    ; O kernel Linux espera o código de retorno no registrador EBX.
    ; Neste caso, vamos usar o valor original 10 (que ainda está em EBX)
    ; como o código de retorno do programa.
    ; EBX = 10 (valor inalterado desde o passo 1)
    ; O resultado desta linha é que o programa terminará com o código de saída 10.
    ; mov ebx, 10  ; (Opcional, pois EBX já é 10, mas seria a forma de definir um novo código)

    ; Interrompe o sistema para executar a chamada de sistema (Syscall)
    int 0x