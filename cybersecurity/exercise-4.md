
## O que é Cross-Site Request Forgery (CSRF)?

O CSRF explora a  **confiança que um site tem no navegador do usuário** , e não a confiança do usuário no site (como acontece no XSS).

### Definição e Funcionamento

**Definição:** O CSRF é um ataque que força um usuário final a executar ações não intencionais em um aplicativo web em que ele está autenticado. O ataque se baseia no fato de que o navegador da vítima incluirá automaticamente cookies de sessão, credenciais HTTP e outras informações de autenticação em qualquer solicitação enviada ao site de destino.

**O Ciclo de Ataque:**

1. **Vítima Autenticada:** O usuário (vítima) faz login no site legítimo (ex: um banco) e recebe um  **cookie de sessão** , que o mantém autenticado.
2. **Engenharia Social:** O atacante convence a vítima a visitar um site malicioso (ou clicar em um link/e-mail malicioso) em outra aba do navegador, enquanto a sessão com o banco ainda está ativa.
3. **Requisição Forjada:** O site malicioso contém um código (geralmente um formulário oculto ou uma *tag* `<img>` com uma URL) que envia uma **solicitação HTTP forjada** para o site do banco.
   * Exemplo de solicitação forjada: `POST https://banco.com/transferir?destino=conta_do_atacante&valor=1000`.
4. **Execução Indesejada:** O navegador da vítima, seguindo o comportamento padrão, **anexa automaticamente o cookie de sessão do banco** à solicitação forjada.
5. **Sucesso do Ataque:** O servidor do banco recebe a solicitação e, como ela contém um cookie de sessão válido, ele a trata como **legítima** e executa a ação, como transferir dinheiro ou mudar o e-mail do usuário. A vítima não tinha a intenção de realizar essa ação.

O ataque é eficaz porque o atacante  **não precisa roubar o cookie de sessão** ; ele apenas induz o navegador do usuário a enviá-lo.

---

## Mitigação Comum: Tokens Anti-CSRF (Tokens de Sincronização)

A técnica de mitigação mais eficaz e amplamente utilizada para CSRF é o uso de  **Tokens Anti-CSRF** , também conhecidos como  **Tokens de Sincronização (Synchronizer Token Pattern)** .

### Como Funciona:

1. **Geração do Token:** Quando o servidor web (backend) envia uma página HTML (que contém um formulário, por exemplo), ele gera um valor **único, secreto e imprevisível** chamado Token Anti-CSRF.
2. **Entrega ao Cliente:** O servidor:
   * Armazena uma cópia do token na **sessão** do usuário.
   * Envia o token para o cliente, geralmente como um **campo oculto** dentro do formulário HTML ou em um **cabeçalho customizado** (para requisições AJAX).
3. **Validação na Requisição:** Quando o cliente (o navegador da vítima) envia uma solicitação que altera o estado do sistema (POST, PUT, DELETE), ele deve **incluir o token** que foi recebido.
4. **Checagem pelo Servidor:** O servidor compara o token recebido na solicitação com o token armazenado na sessão do usuário.
   * **Se coincidirem:** A requisição é considerada legítima e é processada.
   * **Se não coincidirem (ou estiver faltando):** A requisição é rejeitada como uma potencial tentativa de CSRF.

### Por que Mitiga o Ataque?

Um atacante operando a partir de um site externo **não tem como adivinhar ou obter** o token secreto, pois ele não é exposto a scripts externos e é gerado aleatoriamente para cada sessão ou formulário. Sem o token correto, a solicitação forjada do atacante falha na validação do servidor.
