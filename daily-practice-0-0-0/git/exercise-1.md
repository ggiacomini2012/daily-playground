Para demonstrar o uso do comando `git stash push -m 'mensagem'` e listar o resultado, vou simular as três etapas que você faria no terminal:

-----

## 1\. Simulação: Criação de Mudanças

Antes de guardar (stashing), precisamos ter algumas alterações não *commitadas* no seu ambiente de trabalho.

*(Imagine que você executou comandos como `echo "nova linha" >> arquivo.txt`)*

## 2\. Execução: Guardando as Mudanças com Mensagem

Você usaria o comando `git stash push` com o argumento `-m` para adicionar uma descrição útil ao *stash*.

**Comando Executado:**

```bash
git stash push -m 'Feature: Implementação inicial do módulo de login'
```

**Resultado Simulado:**

```
Saved working tree and index state On feature/login: Feature: Implementação inicial do módulo de login
```

## 3\. Verificação: Listando os Stashes

O comando `git stash list` confirma que suas mudanças foram guardadas e exibe a mensagem que você forneceu.

**Comando Executado:**

```bash
git stash list
```

**Resultado Simulado (Listagem):**

```
stash@{0}: On feature/login: Feature: Implementação inicial do módulo de login
```

### O que significa o resultado:

  * **`stash@{0}`**: É o identificador da sua mudança. O número `0` indica que é o item mais recente na sua lista de *stashes*.
  * **`On feature/login`**: Indica a *branch* em que você estava quando guardou a mudança.
  * **`Feature: Implementação inicial do módulo de login`**: É a **mensagem** que você definiu com o argumento `-m`, o que torna muito mais fácil lembrar o que esse *stash* contém mais tarde.

Não, o `git stash` **não é o mesmo** que fazer `git add .` seguido de um `git commit`.

A principal diferença é o **objetivo** e a **permanência** das mudanças:

---

## Git Stash vs. Git Commit

| Característica | `git stash push` | `git add .` + `git commit` |
| :--- | :--- | :--- |
| **Objetivo** | **Guardar temporariamente** o estado de trabalho sujo para alternar de contexto. | **Gravar permanentemente** um conjunto de mudanças no histórico do projeto. |
| **Permanência** | **Temporário.** As mudanças ficam em uma "pilha" separada, fora do histórico da *branch*. | **Permanente.** As mudanças fazem parte da *branch* atual e são enviadas para o repositório remoto. |
| **Estado Limpo** | Sim. Após o `stash`, seu diretório de trabalho fica **limpo** e idêntico ao último *commit*. | Não. O `commit` **adiciona** as mudanças à *branch*, mas o estado de trabalho subsequente (se você continuar codificando) pode ficar sujo novamente. |
| **Visibilidade** | Visível apenas localmente através de `git stash list`. | Visível a qualquer pessoa que use `git log` ou acesse o repositório remoto. |

### Exemplo Prático

* Se você fizer um **`commit`**, as alterações se tornam parte da sua *branch*. Se você mudar para outra *branch*, as alterações do *commit* **não a seguirão**.
* Se você fizer um **`stash`**, suas alterações são removidas da *branch* atual. Você pode mudar para qualquer outra *branch*, trabalhar nela e, depois, voltar para a *branch* original e aplicar o `stash` (usando `git stash pop` ou `git stash apply`).