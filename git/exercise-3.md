
# O que é `git rebase -i HEAD~3`?

O comando `git rebase -i HEAD~3` faz duas coisas essenciais:

1. **`HEAD~3`** : Define o intervalo de *commits* a ser reescrito. Ele seleciona os **três últimos *commits*** do *branch* atual (excluindo o *commit* anterior a esses três).
2. **`-i` (Interativo)** : Abre um editor de texto (como Nano ou Vim) que permite a você **modificar** a ordem e a ação de cada *commit* dentro desse intervalo.

Ao executar o comando, o Git apresenta um arquivo parecido com este:

**Markdown**

```
pick 48b2c1d Commit A: Funcionalidade inicial
pick f34a98e Commit B: Correção de bug no layout
pick 1c2d3e4 Commit C: Adição de nova feature

# Rebase 45f3a0b..1c2d3e4 em 45f3a0b (3 commits)
#
# Comandos:
# p, pick <hash> = usar commit
# r, reword <hash> = usar commit, mas editar a mensagem
# e, edit <hash> = usar commit, mas parar para emendar
# s, squash <hash> = usar commit, mas fundi-lo com o commit anterior
# f, fixup <hash> = como "squash", mas descartar a mensagem de log do commit
# ... (outros comandos)
```

---

## Definindo Qual *Commit* Será 'Squashed'

O objetivo do 'squash' é **fundir** o código de um *commit* secundário no *commit* imediatamente **anterior** a ele na lista.

### Cenário: Fundir o *Commit B* (Correção) no *Commit A* (Funcionalidade)

Se o seu objetivo é pegar o trabalho de "Commit B" e **combiná-lo** com o "Commit A", você deve mudar o comando na linha do *Commit B* de `pick` para **`squash`** (ou  **`s`** ).

**Arquivo Editado:**

**Markdown**

```
pick 48b2c1d Commit A: Funcionalidade inicial
squash f34a98e Commit B: Correção de bug no layout <--- Mude esta linha
pick 1c2d3e4 Commit C: Adição de nova feature

# ... (comandos de ajuda)
```

**O que acontece a seguir:**

1. O Git aplica o  **Commit A** .
2. Ao chegar no  **Commit B** , o Git  **não cria um novo *commit*** ; em vez disso, ele aplica as alterações do Commit B sobre o Commit A.
3. O Git abre um **segundo editor** para que você possa **combinar as mensagens** de *log* do Commit A e do Commit B em uma única e limpa mensagem.

**Resultado:** O histórico final terá apenas dois *commits* (o novo A/B fundido e o Commit C), em vez dos três originais. Você terá um histórico mais limpo, onde a correção (`Commit B`) não aparece como um passo separado.
