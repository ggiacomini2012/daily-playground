
## O que é Cross-Site Scripting (XSS)?

**Cross-Site Scripting (XSS)** é um tipo de ataque de **injeção de código** em que um invasor insere **scripts maliciosos** (geralmente JavaScript) em um website confiável e legítimo. O ataque não visa o servidor, mas sim os **navegadores** dos usuários que visitam a página comprometida.

### Como Funciona?

O ataque ocorre porque a aplicação web **não valida ou não trata corretamente** as informações fornecidas por um usuário antes de exibi-las para outros.

1.  **Injeção:** O atacante encontra um campo de entrada vulnerável (como um campo de comentário, busca ou perfil de usuário) e, em vez de um texto normal, insere um script (ex: `<script>alert('Ataque XSS!')</script>`).
2.  **Armazenamento/Reflexão:**
    * **XSS Armazenado (Stored XSS):** O script é salvo permanentemente no banco de dados do site (por exemplo, em um comentário de blog).
    * **XSS Refletido (Reflected XSS):** O script é incluído na URL e "refletido" de volta ao navegador da vítima na resposta HTTP (por exemplo, em uma página de resultados de busca).
3.  **Execução:** Quando uma vítima navega para a página comprometida, o script malicioso é carregado pelo servidor e, sem que o navegador saiba que é malicioso, ele o **executa** no contexto de segurança do site confiável.

### O Perigo do XSS

Ao ser executado no navegador da vítima, o script malicioso pode:

* **Roubar Cookies:** Capturar **cookies de sessão** do usuário (que mantêm o usuário logado) e enviá-los para o servidor do atacante, permitindo o **sequestro de sessão (session hijacking)**.
* **Capturar Credenciais:** Usar o JavaScript para registrar teclas digitadas (keylogging) ou criar formulários falsos (phishing).
* **Modificar a Página:** Alterar visualmente o conteúdo da página (defacement) ou redirecionar o usuário para um site malicioso.

---

## Técnica de Mitigação: Sanitização e Codificação de Saída (Output Encoding)

A técnica de mitigação mais eficaz contra XSS é a **Codificação de Saída (Output Encoding)**, que geralmente é combinada com a **Sanitização de Input**.

### Sanitização de Input (Filter Input)

A **sanitização de input** é o processo de **remover ou filtrar** ativamente caracteres perigosos, como `<` e `>`, na **entrada** do usuário.

* **Exemplo:** Se um usuário digitar `<script>`, o código de sanitização pode simplesmente removê-lo.

### Codificação de Saída (Output Encoding) — A Defesa Primária

A **codificação de saída** é a principal defesa contra XSS. Em vez de tentar remover o código malicioso, ela garante que o dado de entrada **nunca seja interpretado** como código ativo pelo navegador.

* **Como funciona:** Antes de exibir qualquer dado fornecido pelo usuário (seja de um banco de dados ou de uma URL) na página HTML, a aplicação converte caracteres especiais em suas **entidades HTML** equivalentes.

| Caractere Perigoso | Entidade HTML |
| :----------------: | :------------ |
| `<` (menor que)    | `&lt;`        |
| `>` (maior que)    | `&gt;`        |
| `"` (aspas duplas) | `&quot;`      |
| `'` (aspas simples) | `&#x27;`      |

* **Resultado:** Se um atacante injetar `<script>alert(1)</script>`, a página exibe o texto como: `&lt;script&gt;alert(1)&lt;/script&gt;`.
    * O navegador vê isso apenas como **texto simples** (`<script>alert(1)</script>`) e o exibe, em vez de **executá-lo** como um script.