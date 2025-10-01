section .text
    global _start

_start:
INI_CALC:
    mov eax, 10
    add eax, 5
    
    jmp FIM
    
IGNORADO:
    sub eax, 2
    
FIM:
    mov ebx, 0
    mov eax, 1
    int 0x80