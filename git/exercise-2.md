
## Como usar `git add` e `git commit --amend` para Corrigir a Mensagem do Último Commit

O comando `git commit --amend` é usado para **modificar o commit mais recente**. Ele substitui o último commit por um novo, mas mantendo a mesma data de autor e geralmente a mesma data de commit (a menos que você especifique o contrário).

### Cenário: Corrigir Apenas a Mensagem

1.  **Ação:** Digitar o comando:
    ```bash
    git commit --amend
    ```
2.  **Resultado:** O Git abrirá seu editor de texto configurado (como Vim, Nano, etc.) com a mensagem do commit anterior. Você edita a mensagem e salva/fecha o arquivo.
3.  **Efeito:** O Git substitui o commit anterior por um novo com a mensagem corrigida.

### Cenário: Incluir Alterações e Corrigir a Mensagem

Este é o cenário onde o `git add` entra em jogo, e é o que você está descrevendo.

Imagine que você fez um commit, mas logo em seguida percebeu que **esqueceu de incluir uma pequena correção** ou que **o arquivo que você modificou precisa ser incluído** no *mesmo* commit (para que a mensagem do commit faça sentido, ou para manter o histórico limpo).

#### 1\. Faça as Modificações e Adicione-as

Primeiro, você faz as alterações necessárias no seu arquivo modificado (ou em qualquer novo arquivo). Depois, você o adiciona à **área de *staging***.

```bash
# 1. Modifique o arquivo
# 2. Adicione o arquivo à staging area (índice)
git add nome_do_arquivo_modificado
```

#### 2\. Emende o Commit

Quando você usa `git commit --amend` **com arquivos na área de *staging***, o Git faz duas coisas:

1.  Ele inclui **todas as alterações** que estão atualmente na sua área de *staging* (incluindo o arquivo que você acabou de dar `git add`).
2.  Ele abre o editor de texto para que você possa **editar a mensagem do commit**.

<!-- end list -->

```bash
# 3. Use --amend para incluir as alterações e corrigir a mensagem
git commit --amend
```

### O Resultado Final

  * O Git **combina** as alterações do seu último commit *mais* as novas alterações na área de *staging*.
  * Ele usa a **nova mensagem** que você escreveu.
  * O **último commit original é descartado** e um **novo commit é criado**, com um novo *hash* (ID de commit).

**Em resumo:**

O **`git add`** serve para **incluir as alterações do arquivo** no *commit emendado*, e o **`git commit --amend`** serve para **combinar essas novas alterações com as antigas** e, ao mesmo tempo, permitir que você **atualize a mensagem** do commit.