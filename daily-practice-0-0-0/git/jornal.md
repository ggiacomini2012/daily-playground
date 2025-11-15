# Exercício de Git: Fluxo Básico

**Objetivo:** Praticar o ciclo fundamental de desenvolvimento com Git, incluindo a criação de branches, staging, commit e merge.

**Contexto:** Você vai modificar o arquivo `js/exercise.js` que criamos anteriormente. A ideia é fazer essa alteração em uma branch separada e, depois, integrá-la à branch principal (`main` ou `master`).

---

### Passos:

**1. Verifique sua Branch Atual**
   - Garanta que você está na branch principal.
   ```bash
   git branch
   ```
   - O asterisco (`*`) deve apontar para `main` ou `master`. Se não estiver, mude para ela com `git checkout main`.

**2. Crie e Mude para uma Nova Branch**
   - Crie uma branch chamada `feature/saudacao-js`.
   ```bash
   git checkout -b feature/saudacao-js
   ```
   - Este comando cria a branch e já muda para ela.

**3. Modifique o Arquivo**
   - Abra o arquivo `js/exercise.js`.
   - Vá até a seção da solução (que está comentada) e descomente o código.
   - Troque `"Seu Nome"` pelo seu nome de verdade.

**4. Adicione a Mudança ao Staging**
   - Use `git status` para ver o arquivo modificado.
   - Adicione o arquivo `js/exercise.js` à área de "staging".
   ```bash
   git add js/exercise.js
   ```

**5. Faça o Commit**
   - Crie um commit com uma mensagem clara.
   ```bash
   git commit -m "feat(js): implementa solucao do exercicio de saudacao"
   ```

**6. Volte para a Branch Principal**
   - Mude de volta para a sua branch principal.
   ```bash
   git checkout main
   ```

**7. Faça o Merge da Sua Feature**
   - Integre as mudanças da branch `feature/saudacao-js` na branch `main`.
   ```bash
   git merge feature/saudacao-js
   ```
   - Você verá uma mensagem indicando que o merge foi feito com "fast-forward".

**8. (Opcional) Exclua a Branch da Feature**
   - Como o trabalho na branch foi concluído e integrado, você pode excluí-la.
   ```bash
   git branch -d feature/saudacao-js
   ```

---

Parabéns! Você completou um ciclo de desenvolvimento com Git.
