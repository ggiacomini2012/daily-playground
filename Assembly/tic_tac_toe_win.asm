; Jogo da Velha (Tic-Tac-Toe) para Windows 64-bit
; Autor: Gemini
; Para montar e linkar usando o terminal do Visual Studio:
; nasm -f win64 tic_tac_toe_win.asm -o tic_tac_toe_win.obj
; link tic_tac_toe_win.obj kernel32.lib user32.lib /subsystem:console /entry:main

; Importa as funções da API do Windows que vamos usar
extern GetStdHandle, WriteConsoleA, ReadConsoleA, ExitProcess

section .data
    ; Constantes para a função GetStdHandle
    STD_OUTPUT_HANDLE equ -11
    STD_INPUT_HANDLE  equ -10

    ; Variáveis para armazenar os "handles" do console
    stdout_handle dq 0
    stdin_handle  dq 0

    ; Variáveis para contagem de bytes escritos/lidos
    bytes_written dq 0
    bytes_read    dq 0

    ; Tabuleiro do jogo e mensagens (semelhante à versão Linux)
    board         db '1', '2', '3', '4', '5', '6', '7', '8', '9'
    msg_welcome   db "Bem-vindo ao Jogo da Velha em Assembly (Windows)!", 0Dh, 0Ah
    len_welcome   equ $ - msg_welcome
    msg_player_x  db "Jogador X, sua vez. Escolha uma posicao (1-9): ", 0Dh, 0Ah
    len_player_x  equ $ - msg_player_x
    msg_player_o  db "Jogador O, sua vez. Escolha uma posicao (1-9): ", 0Dh, 0Ah
    len_player_o  equ $ - msg_player_o
    msg_win_x     db "Jogador X venceu!", 0Dh, 0Ah
    len_win_x     equ $ - msg_win_x
    msg_win_o     db "Jogador O venceu!", 0Dh, 0Ah
    len_win_o     equ $ - msg_win_o
    msg_draw      db "O jogo terminou em empate!", 0Dh, 0Ah
    len_draw      equ $ - msg_draw
    msg_invalid   db "Posicao invalida ou ja ocupada. Tente novamente.", 0Dh, 0Ah
    len_invalid   equ $ - msg_invalid
    
    board_template db 0Dh, 0Ah, ' ', 0, ' | ', 0, ' | ', 0, 0Dh, 0Ah
                     db '---+---+---', 0Dh, 0Ah
                     db ' ', 0, ' | ', 0, ' | ', 0, 0Dh, 0Ah
                     db '---+---+---', 0Dh, 0Ah
                     db ' ', 0, ' | ', 0, ' | ', 0, 0Dh, 0Ah, 0Dh, 0Ah
    len_template   equ $ - board_template

    current_player db 'X'
    turns          db 0

section .bss
    user_input resb 4  ; Buffer para entrada (char + CR + LF + null)

section .text
global main

; Função para imprimir texto no console
print:
    ; A convenção de chamada do Windows x64 usa RCX, RDX, R8, R9 para os primeiros 4 argumentos
    ; WriteConsoleA(handle, buffer, length, &bytes_written, NULL)
    mov rcx, [stdout_handle] ; arg1: Handle para o stdout
    ; RDX já deve conter o endereço da mensagem (arg2)
    ; R8 já deve conter o tamanho da mensagem (arg3)
    mov r9, bytes_written    ; arg4: Endereço para armazenar o número de bytes escritos
    push qword 0             ; arg5: NULL (reservado)
    call WriteConsoleA
    ret

main:
    ; Obtém os handles para a saída e entrada padrão do console
    mov rcx, STD_OUTPUT_HANDLE
    call GetStdHandle
    mov [stdout_handle], rax
    
    mov rcx, STD_INPUT_HANDLE
    call GetStdHandle
    mov [stdin_handle], rax

    ; Exibe mensagem de boas-vindas
    mov rdx, msg_welcome
    mov r8, len_welcome
    call print

game_loop:
    call print_board
    cmp byte [turns], 9
    je game_draw
    call get_player_move
    call process_move
    call check_win
    call switch_player
    inc byte [turns]
    jmp game_loop

print_board:
    mov byte [board_template + 3],  [board]
    mov byte [board_template + 7],  [board + 1]
    mov byte [board_template + 11], [board + 2]
    mov byte [board_template + 28], [board + 3]
    mov byte [board_template + 32], [board + 4]
    mov byte [board_template + 36], [board + 5]
    mov byte [board_template + 53], [board + 6]
    mov byte [board_template + 57], [board + 7]
    mov byte [board_template + 61], [board + 8]
    
    mov rdx, board_template
    mov r8, len_template
    call print
    ret

get_player_move:
    cmp byte [current_player], 'X'
    je player_x_prompt
    
player_o_prompt:
    mov rdx, msg_player_o
    mov r8, len_player_o
    call print
    jmp read_input
    
player_x_prompt:
    mov rdx, msg_player_x
    mov r8, len_player_x
    call print
    
read_input:
    ; ReadConsoleA(handle, buffer, buffer_size, &bytes_read, NULL)
    mov rcx, [stdin_handle]
    mov rdx, user_input
    mov r8, 2
    mov r9, bytes_read
    push qword 0
    call ReadConsoleA
    ret

process_move:
    mov al, [user_input]
    sub al, '1'
    cmp al, 8
    ja invalid_move
    
    movzx rbx, al
    mov cl, [board + rbx]
    cmp cl, 'X'
    je invalid_move
    cmp cl, 'O'
    je invalid_move
    
    mov cl, [current_player]
    mov [board + rbx], cl
    ret

invalid_move:
    mov rdx, msg_invalid
    mov r8, len_invalid
    call print
    jmp game_loop

; A lógica de check_win e switch_player é idêntica à versão Linux
check_win:
    mov al, [current_player]

    ; Linhas
    cmp byte [board], al
    jne .r2
    cmp byte [board+1], al
    jne .r2
    cmp byte [board+2], al
    je game_win
.r2:cmp byte [board+3], al
    jne .r3
    cmp byte [board+4], al
    jne .r3
    cmp byte [board+5], al
    je game_win
.r3:cmp byte [board+6], al
    jne .c1
    cmp byte [board+7], al
    jne .c1
    cmp byte [board+8], al
    je game_win
    
    ; Colunas
.c1:cmp byte [board], al
    jne .c2
    cmp byte [board+3], al
    jne .c2
    cmp byte [board+6], al
    je game_win
.c2:cmp byte [board+1], al
    jne .c3
    cmp byte [board+4], al
    jne .c3
    cmp byte [board+7], al
    je game_win
.c3:cmp byte [board+2], al
    jne .d1
    cmp byte [board+5], al
    jne .d1
    cmp byte [board+8], al
    je game_win

    ; Diagonais
.d1:cmp byte [board], al
    jne .d2
    cmp byte [board+4], al
    jne .d2
    cmp byte [board+8], al
    je game_win
.d2:cmp byte [board+2], al
    jne .no_win
    cmp byte [board+4], al
    jne .no_win
    cmp byte [board+6], al
    je game_win

.no_win: 
    ret

switch_player:
    cmp byte [current_player], 'X'
    je .to_o
    mov byte [current_player], 'X'
    ret
.to_o: mov byte [current_player], 'O'
    ret

game_win:
    call print_board
    cmp byte [current_player], 'X'
    je .win_x_msg
.win_o_msg:
    mov rdx, msg_win_o
    mov r8, len_win_o
    call print
    jmp exit
.win_x_msg:
    mov rdx, msg_win_x
    mov r8, len_win_x
    call print
    jmp exit
    
game_draw:
    call print_board
    mov rdx, msg_draw
    mov r8, len_draw
    call print
    jmp exit
    
exit:
    ; ExitProcess(exit_code)
    mov rcx, 0  ; Código de saída 0 (sucesso)
    call ExitProcess