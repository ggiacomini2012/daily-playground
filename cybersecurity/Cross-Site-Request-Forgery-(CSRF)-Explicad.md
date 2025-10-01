
## 🛡️ Cross-Site Request Forgery (CSRF) Explicado

**Cross-Site Request Forgery (CSRF)**, também conhecido como "sequestro de sessão" ou **XSRF**, é um tipo de ataque que explora a **confiança que uma aplicação web tem no navegador de um usuário autenticado**.

O objetivo do atacante é forçar o navegador da vítima a **enviar uma requisição HTTP indesejada** para um site no qual ela já está logada.

-----

### Como o Ataque CSRF Funciona?

O ataque CSRF não rouba dados diretamente (como uma senha), mas sim força o usuário a **executar uma ação**. Ele depende de três condições:

1.  **Usuário Autenticado:** O usuário deve estar logado no site alvo (ex: seu banco, rede social) em uma aba do navegador.
2.  **Ação Relevante:** O atacante precisa encontrar uma ação que possa ser executada por uma simples requisição HTTP (ex: mudar a senha, transferir dinheiro, postar algo).
3.  **Cookies Automáticos:** Os navegadores, por padrão, incluem automaticamente os **cookies de sessão** (que comprovam que o usuário está logado) em qualquer requisição enviada para o domínio original, mesmo que a requisição seja iniciada a partir de um site malicioso.

#### Cenário de Exemplo:

1.  O usuário, **João**, está logado no seu banco (`banco.com`). O navegador guarda seu cookie de sessão.
2.  O atacante envia a João um link ou e-mail que o leva a um site malicioso (`site-malicioso.com`).
3.  O `site-malicioso.com` contém um código oculto, como uma tag `<img>` ou um formulário submetido via JavaScript, que aponta para o endereço de transferência do banco de João:
    ```html
    <img src="https://banco.com/transferir?dest=Invasor&valor=1000" style="display:none;" />
    ```
4.  Quando o navegador de João carrega o `site-malicioso.com`, ele tenta carregar a imagem. Ao tentar fazer a requisição para `banco.com`, ele **automaticamente anexa o cookie de sessão de João**.
5.  O servidor do `banco.com` vê uma requisição válida (com o cookie de sessão) vinda de João e **executa a transferência de R$ 1.000,00** para a conta do Invasor, sem que João tenha conhecimento ou intenção.

-----

### 🔑 Principais Formas de Mitigação (Prevenção)

Para evitar que a aplicação confie cegamente nas requisições, os desenvolvedores utilizam mecanismos que exigem uma "prova" de que a requisição foi intencional:

1.  **Tokens Anti-CSRF (A principal defesa):** Um token secreto e imprevisível é gerado pelo servidor e incluído em cada formulário ou requisição que modifica dados. O servidor verifica se o token na requisição corresponde ao token na sessão do usuário. Se o invasor tentar forjar uma requisição, ele **não terá o token correto**, e a requisição será rejeitada.
2.  **Cabeçalho `SameSite` para Cookies:** Configurar os cookies com o atributo **`SameSite=Strict`** (ou `Lax`) impede que o navegador envie o cookie de sessão com requisições *cross-site*. Isso quebra a condição essencial do ataque.
3.  **Verificação do Cabeçalho `Referer` ou `Origin`:** O servidor pode verificar se o domínio de origem (`Origin`) da requisição é o mesmo domínio esperado.
4.  **Re-autenticação:** Para ações críticas (como mudança de senha), exigir que o usuário insira novamente sua senha.