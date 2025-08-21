; Jogo da Velha (Tic-Tac-Toe) em Assembly x86-64 para Linux
; Autor: Gemini
; Para montar e linkar:
; nasm -f elf64 tic_tac_toe.asm -o tic_tac_toe.o
; ld tic_tac_toe.o -o tic_tac_toe

section .data
    ; Tabuleiro do jogo, inicializado com os números das posições
    board       db  '1', '2', '3', '4', '5', '6', '7', '8', '9'
    board_size  equ $ - board

    ; Mensagens para o usuário
    msg_welcome db  "Bem-vindo ao Jogo da Velha em Assembly!", 0ah
    len_welcome equ $ - msg_welcome
    
    msg_player_x db  "Jogador X, sua vez. Escolha uma posição (1-9): ", 0ah
    len_player_x equ $ - msg_player_x
    
    msg_player_o db  "Jogador O, sua vez. Escolha uma posição (1-9): ", 0ah
    len_player_o equ $ - msg_player_o

    msg_win_x    db  "Jogador X venceu!", 0ah
    len_win_x    equ $ - msg_win_x

    msg_win_o    db  "Jogador O venceu!", 0ah
    len_win_o    equ $ - msg_win_o

    msg_draw     db  "O jogo terminou em empate!", 0ah
    len_draw     equ $ - msg_draw
    
    msg_invalid  db  "Posição inválida ou já ocupada. Tente novamente.", 0ah
    len_invalid  equ $ - msg_invalid

    ; Template para desenhar o tabuleiro
    board_template db 0ah, ' ', 0, ' | ', 0, ' | ', 0, 0ah
                     db '---+---+---', 0ah
                     db ' ', 0, ' | ', 0, ' | ', 0, 0ah
                     db '---+---+---', 0ah
                     db ' ', 0, ' | ', 0, ' | ', 0, 0ah, 0ah
    len_template equ $ - board_template
    
    ; Variáveis do jogo
    current_player  db  'X'
    turns           db  0

section .bss
    ; Buffer para a entrada do usuário
    user_input resb 2

section .text
    global _start

_start:
    ; Exibir mensagem de boas-vindas
    mov rax, 1          ; syscall write
    mov rdi, 1          ; stdout
    mov rsi, msg_welcome
    mov rdx, len_welcome
    syscall

game_loop:
    ; Desenhar o tabuleiro
    call print_board

    ; Verificar se o número de turnos chegou a 9 (empate)
    cmp byte [turns], 9
    je game_draw

    ; Solicitar a jogada do jogador atual
    call get_player_move

    ; Validar e processar a jogada
    call process_move
    
    ; Verificar se o jogador atual venceu
    call check_win
    
    ; Trocar de jogador
    call switch_player
    
    ; Incrementar o contador de turnos
    inc byte [turns]
    
    ; Repetir o loop
    jmp game_loop

print_board:
    ; Prepara o template do tabuleiro com os valores atuais
    mov byte [board_template + 2],  [board]
    mov byte [board_template + 6],  [board + 1]
    mov byte [board_template + 10], [board + 2]
    mov byte [board_template + 25], [board + 3]
    mov byte [board_template + 29], [board + 4]
    mov byte [board_template + 33], [board + 5]
    mov byte [board_template + 48], [board + 6]
    mov byte [board_template + 52], [board + 7]
    mov byte [board_template + 56], [board + 8]
    
    ; Imprime o tabuleiro formatado
    mov rax, 1
    mov rdi, 1
    mov rsi, board_template
    mov rdx, len_template
    syscall
    ret

get_player_move:
    ; Exibe a mensagem do jogador correto
    mov rax, 1
    mov rdi, 1
    cmp byte [current_player], 'X'
    je player_x_prompt
    
player_o_prompt:
    mov rsi, msg_player_o
    mov rdx, len_player_o
    syscall
    jmp read_input
    
player_x_prompt:
    mov rsi, msg_player_x
    mov rdx, len_player_x
    syscall
    
read_input:
    ; Lê a entrada do usuário (um caractere + newline)
    mov rax, 0          ; syscall read
    mov rdi, 0          ; stdin
    mov rsi, user_input
    mov rdx, 2
    syscall
    ret

process_move:
    ; Converte o caractere de entrada (ASCII) para um índice de 0 a 8
    mov al, [user_input]
    sub al, '1'         ; Converte '1'-'9' para 0-8
    
    ; Verifica se a entrada está no intervalo válido (0-8)
    cmp al, 8
    ja invalid_move
    
    ; Verifica se a posição já está ocupada por 'X' ou 'O'
    mov rbx, 0
    mov bl, al
    mov cl, [board + rbx]
    cmp cl, 'X'
    je invalid_move
    cmp cl, 'O'
    je invalid_move
    
    ; Se a jogada é válida, atualiza o tabuleiro
    mov cl, [current_player]
    mov [board + rbx], cl
    ret

invalid_move:
    ; Exibe mensagem de jogada inválida
    mov rax, 1
    mov rdi, 1
    mov rsi, msg_invalid
    mov rdx, len_invalid
    syscall
    jmp game_loop       ; Pede a jogada novamente

check_win:
    ; Verifica todas as 8 condições de vitória
    mov al, [current_player]

    ; Linhas
    cmp [board], al
    jne .check_row2
    cmp [board+1], al
    jne .check_row2
    cmp [board+2], al
    je game_win
.check_row2:
    cmp [board+3], al
    jne .check_row3
    cmp [board+4], al
    jne .check_row3
    cmp [board+5], al
    je game_win
.check_row3:
    cmp [board+6], al
    jne .check_col1
    cmp [board+7], al
    jne .check_col1
    cmp [board+8], al
    je game_win

    ; Colunas
.check_col1:
    cmp [board], al
    jne .check_col2
    cmp [board+3], al
    jne .check_col2
    cmp [board+6], al
    je game_win
.check_col2:
    cmp [board+1], al
    jne .check_col3
    cmp [board+4], al
    jne .check_col3
    cmp [board+7], al
    je game_win
.check_col3:
    cmp [board+2], al
    jne .check_diag1
    cmp [board+5], al
    jne .check_diag1
    cmp [board+8], al
    je game_win

    ; Diagonais
.check_diag1:
    cmp [board], al
    jne .check_diag2
    cmp [board+4], al
    jne .check_diag2
    cmp [board+8], al
    je game_win
.check_diag2:
    cmp [board+2], al
    jne .no_win
    cmp [board+4], al
    jne .no_win
    cmp [board+6], al
    je game_win
    
.no_win:
    ret

switch_player:
    ; Alterna entre 'X' e 'O'
    cmp byte [current_player], 'X'
    je .to_o
    mov byte [current_player], 'X'
    ret
.to_o:
    mov byte [current_player], 'O'
    ret

game_win:
    ; Imprime o tabuleiro final
    call print_board
    
    ; Exibe a mensagem de vitória correta
    mov rax, 1
    mov rdi, 1
    cmp byte [current_player], 'X'
    je .win_x_msg
.win_o_msg:
    mov rsi, msg_win_o
    mov rdx, len_win_o
    syscall
    jmp exit
.win_x_msg:
    mov rsi, msg_win_x
    mov rdx, len_win_x
    syscall
    jmp exit
    
game_draw:
    ; Imprime o tabuleiro final
    call print_board
    
    ; Exibe a mensagem de empate
    mov rax, 1
    mov rdi, 1
    mov rsi, msg_draw
    mov rdx, len_draw
    syscall
    jmp exit
    
exit:
    ; Termina o programa
    mov rax, 60
    xor rdi, rdi
    syscall