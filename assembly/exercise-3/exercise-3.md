
## 1\. Sintaxe e Função do Comando `MOV` em x86

O comando `MOV` é usado para **copiar** dados de um local de origem (Source) para um local de destino (Destination).

A sintaxe que você está usando, **`MOV EAX, EBX`**, segue a convenção mais comum do Assembly x86 (a sintaxe **Intel**):

$$\text{MOV} \quad \text{destino}, \quad \text{fonte}$$

### Regra Principal

O `MOV` não "move" no sentido de cortar e colar; ele **copia**. O valor na fonte permanece inalterado, e o valor no destino é substituído pelo valor da fonte.

$$\text{Destino} \leftarrow \text{Fonte}$$

### O que acontece em `MOV EAX, EBX`

  * **Fonte (Source):** O registrador **`EBX`** (Extended Base Register).
  * **Destino (Destination):** O registrador **`EAX`** (Extended Accumulator Register).
  * **Ação:** O valor de **`EBX`** é **copiado** para **`EAX`**. O valor original em `EAX` é perdido, mas o valor em `EBX` permanece o mesmo.

Ambos `EAX` e `EBX` são registradores de propósito geral de **32 bits** (Doubleword) na arquitetura x86.

**Em outras palavras:** É o equivalente à operação em uma linguagem de alto nível como `EAX = EBX;`.

### Tipos de Movimento com `MOV`

O comando `MOV` permite a transferência de dados entre diferentes tipos de operandos:

| Tipo de Transferência | Sintaxe (Exemplo - Intel Syntax) | Descrição |
| :---: | :---: | :--- |
| **Registrador para Registrador** | `MOV EAX, EBX` | Copia o valor de um registrador para outro. |
| **Imediato para Registrador** | `MOV ECX, 10` | Copia um valor constante (imediato) para um registrador. |
| **Registrador para Memória** | `MOV [minha_var], EAX` | Copia o valor de um registrador para um endereço de memória. |
| **Memória para Registrador** | `MOV EAX, [minha_var]` | Copia o valor de um endereço de memória para um registrador. |
| **Imediato para Memória** | `MOV [minha_var], 5` | Copia um valor constante para um endereço de memória. |

**Importante:** A arquitetura x86 **não permite** o movimento direto de memória para memória, como `MOV [var1], [var2]`. Você deve usar um registrador intermediário.

-----

## 2\. Criando o Arquivo Assembly (`mov_exemplo.asm`)

O seguinte *script* de Assembly x86 para Linux (usando a sintaxe **NASM** e a convenção de chamada de sistema - *syscall*) demonstra o uso de `MOV` entre registradores e com um valor imediato, e então usa `MOV` para encerrar o programa.

Crie um arquivo chamado `mov_exemplo.asm`:

```assembly
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
    int 0x80
```

### O que o código faz

1.  `mov ebx, 10`: Inicializa o registrador `EBX` com o valor **$10$**.
2.  `mov eax, ebx`: **Copia** o valor de `EBX` ($10$) para `EAX`. Ambos `EAX` e `EBX` agora contêm $10$.
3.  `mov eax, 1`: Sobrescreve `EAX` com o valor **$1$**. Este valor é necessário para a *syscall* de encerramento (`exit`).
4.  `int 0x80`: Executa a *syscall*. O sistema operacional lê `EAX` ($1$) para saber qual função executar (encerrar o programa) e lê `EBX` ($10$) para saber qual código de saída retornar.

Para verificar se o código de saída foi realmente $10$ após a execução no terminal, você usaria o comando `echo $?`.