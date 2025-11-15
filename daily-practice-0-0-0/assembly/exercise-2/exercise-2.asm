.global _start

_start:
    ; Mover o valor imediato 5 para o registrador R0 (Rd)
    MOV R0, #5
    
    ; Mover o valor imediato 8 para o registrador R1 (Rm)
    MOV R1, #8
    
    ; Mover o conteúdo de R0 para R2
    MOV R2, R0 
    
    ; Adicionar R1 (8) ao R2 (5), o resultado (13) vai para R2
    ADD R2, R2, R1
    
    ; Fim do programa (Chamada de sistema exit)
    ; Para a maioria dos sistemas ARM Linux:
    ; r7 = syscall number (1 para exit)
    ; r0 = exit code (0 para sucesso)
    MOV R7, #1
    MOV R0, #0
    SVC #0        
    ; Executa a chamada de sistema (Supervisor Call)