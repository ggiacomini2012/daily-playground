
# SpeedTracker Dev

> Um miniaplicativo de produtividade para guiar suas sessões de micro-tarefas com foco e disciplina.

-----

## 🚀 Por que o SpeedTracker?

O SpeedTracker Dev nasceu da necessidade de criar um "aquecimento" produtivo para o dia de um desenvolvedor. Ele transforma uma rotina de micro-tarefas (JavaScript, Python, Git, Segurança, etc.) em uma sessão de prática guiada, cronometrada e sem distrações.

Este aplicativo pega um simples roteiro de tarefas em formato `.json` e o converte em uma ferramenta interativa que impulsiona o foco, mede o tempo e constrói o hábito do aprendizado contínuo.

## ✨ Destaques

  * **Interface Minimalista:** Construído com CustomTkinter para uma experiência limpa, moderna e focada.
  * **Roteiros em JSON:** Carregue e alterne facilmente entre diferentes listas de tarefas (`.json`).
  * **Cronômetro Regressivo:** Um timer visual claro para manter você no ritmo.
  * **Fluxo Contínuo:** Ao final de uma tarefa, o app faz uma pequena pausa e inicia a próxima automaticamente.
  * **Alerta de Foco:** Nos últimos 5 segundos, a janela salta para a frente de todos os outros apps, garantindo que você não perca o final da tarefa.
  * **Pausa e Retomada:** Pause o cronômetro a qualquer momento.
  * **Log de Progresso:** Cada tarefa concluída é registrada em `activity_log.csv` com data e hora, permitindo que você acompanhe sua evolução.
  * **Modo Portátil:** Execute o app diretamente por um arquivo `.bat` sem precisar ativar ambientes virtuais manualmente (ideal para uso rápido).

-----

## 🛠️ Tecnologias

  * **Python 3.10+**
  * **CustomTkinter:** Para a criação da interface gráfica.
  * **pywinstyles:** Para aplicar efeitos visuais nativos do Windows (como "Mica").

-----

## 🏁 Começando

Para rodar o SpeedTracker na sua máquina, o processo é simples e rápido.

### Pré-requisitos

  * [Python 3.10](https://www.python.org/downloads/) ou superior
  * [Git](https://git-scm.com/downloads/)

### Instalação em 3 Passos

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/ggiacomini2012/daily-playground.git
    cd daily-playground/speed-track-dev
    ```

2.  **Crie e ative um ambiente virtual (Recomendado):**

    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS / Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

### Executando o App

  * **Modo Padrão (com ambiente virtual ativado):**
    ```bash
    python speed_tracker_app.py
    ```
  * **Modo Portátil (Windows, sem precisar ativar o venv):**
    Dê um duplo clique no arquivo `run.bat`. Ele encontrará o ambiente virtual e executará o script para você.

-----

## 📖 Como Usar

### 1\. Crie seu Roteiro

O coração do SpeedTracker é o arquivo `roteiro.json`. Edite-o para criar sua própria rotina de tarefas. Ou Peça para uma IA para criar, mostrando o seguinte json como exemplo e adicionando novos tópicos(ações).

```json
{
  "roteiro_speed_tracking": [
    {
      "id": 1,
      "acao": "Python",
      "tempo_minutos": 2,
      "tarefa_especifica_hoje": "Refatore uma função para torná-la mais legível."
    },
    {
      "id": 2,
      "acao": "Git",
      "tempo_minutos": 1,
      "tarefa_especifica_hoje": "Use 'git log --oneline --graph' para visualizar o histórico."
    }
  ]
}
```

### 2\. Controles do App

  * **Carregar Roteiro:** Use o botão no canto superior direito para carregar um novo arquivo `.json`.
  * **Iniciar/Pausar/Retomar:** Controle o cronômetro durante a execução.
  * **Arrastar:** Clique e arraste a barra de título para mover a janela.
  * **Fechar:** Clique no "✕" para sair.

-----

## 📦 Criando o Executável (Standalone)

Para distribuir o SpeedTracker como um programa `.exe` que não precisa de Python instalado, você pode usar o PyInstaller.

1.  **Instale o PyInstaller:**
    Certifique-se de que seu ambiente virtual (`venv`) está ativado e instale o PyInstaller:

    ```bash
    pip install pyinstaller
    ```

2.  **Gere o Executável:**
    No terminal, a partir da pasta raiz do projeto, execute o seguinte comando. Ele irá criar um único arquivo `.exe`, sem a janela de console preta e com um ícone personalizado.

    ```bash
    ./installer.sh
    ```

-----

## 🗺️ Roadmap

O futuro do SpeedTracker inclui:

  - [ ] **Relatórios Visuais:** Criar uma tela de estatísticas para visualizar os dados do `activity_log.csv`.
  - [ ] **Temas e Alertas Sonoros:** Permitir a personalização da aparência e dos sons.
  - [ ] **Internacionalização (i18n):** Suporte para múltiplos idiomas na interface.
  - [ ] **Edição de Tarefas na UI:** Permitir criar e editar tarefas diretamente pelo app.

-----

## 🤝 Como Contribuir

Contribuições são muito bem-vindas\! Se você tem ideias para novas funcionalidades, melhorias ou correções de bugs, siga os passos:

1.  Faça um **Fork** do projeto.
2.  Crie uma nova **Branch** (`git checkout -b feature/sua-feature-incrivel`).
3.  Faça o **Commit** das suas mudanças (`git commit -m 'Adiciona sua-feature-incrivel'`).
4.  Faça o **Push** para a Branch (`git push origin feature/sua-feature-incrivel`).
5.  Abra um **Pull Request**.

-----

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

-----

Criado com ❤️ por **Guilherme Giacomini Teixeira**