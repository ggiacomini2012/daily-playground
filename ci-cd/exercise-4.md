
## O Workflow Básico Explicado

Este arquivo deve ser salvo em: `.github/workflows/main.yml`

```yaml
name: Integração Contínua (CI) Simples

# 1. QUANDO EXECUTAR? (O Gatilho)
# Esta seção diz ao GitHub quando "ligar" este workflow.
on:
  # 'push' significa que o workflow rodará sempre que enviarmos (push) código.
  push:
    # 'branches' limita a ação apenas quando o push for para a branch 'main'.
    branches:
      - main
  
  # 'workflow_dispatch' permite que você clique em um botão no GitHub para rodar manualmente.
  workflow_dispatch:

# 2. O QUE EXECUTAR? (Os Jobs)
# Um 'job' é um conjunto de passos que roda em uma máquina virtual isolada.
jobs:
  build:
    # 'name' é o nome amigável que aparece no painel do GitHub Actions.
    name: Compilar e Verificar
    
    # 'runs-on' define o tipo de máquina virtual que será usada para o job.
    # 'ubuntu-latest' é uma máquina Linux comum e gratuita.
    runs-on: ubuntu-latest

    # 'steps' é a lista de tarefas, executadas uma após a outra, dentro do job 'build'.
    steps:
      # TAREFA 1: Baixar o Código
      - name: Baixar o código do repositório
        # 'uses' roda uma ação pré-configurada pelo GitHub.
        # 'actions/checkout@v4' baixa seu código para a máquina virtual.
        uses: actions/checkout@v4
        
      # TAREFA 2: Simular o Build
      - name: Ação: Simular a compilação
        # 'run' executa comandos de linha (como se você estivesse digitando no terminal).
        # Neste caso, apenas imprime uma mensagem.
        run: echo 'Building... (Simulando a compilação do seu projeto)'
```

## Resumo Didático

Pense neste arquivo como um contrato com o GitHub:

1.  **Gatilho (`on: push`):** "GitHub, eu quero que você execute esta lista de tarefas **automaticamente** toda vez que eu atualizar a *branch* principal (`main`)."
2.  **Job (`jobs: build`):** "A lista de tarefas se chama **'build'**. Para executá-la, por favor, configure uma máquina Linux (`runs-on: ubuntu-latest`)."
3.  **Passos (`steps`):**
      * **Passo 1 (`actions/checkout@v4`):** "Primeiro, baixe todo o meu código para esta máquina."
      * **Passo 2 (`run: echo`):** "Segundo, finja que está compilando, apenas mostrando a mensagem 'Building...'."

