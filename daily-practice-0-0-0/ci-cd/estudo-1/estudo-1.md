Aqui está a definição de **Pipeline Stage** no contexto de CI/CD (GitLab/GitHub Actions), formatada em Markdown, conforme solicitado:

---

# Definição de Pipeline Stage (Estágio de Pipeline)

Em plataformas de Integração e Entrega Contínuas (CI/CD) como **GitLab CI/CD** e **GitHub Actions**, um **Pipeline Stage** (Estágio de Pipeline) é um componente estrutural que organiza o fluxo de trabalho.

A função pode ser definida em três passos principais:

---

## 1. O que é? (Agrupamento Lógico)

Um Estágio é uma **fase lógica de alto nível** dentro do *pipeline*. Seu propósito é **agrupar trabalhos (jobs)** que compartilham uma finalidade comum, como preparar o ambiente, validar o código ou implantar o software.

---

## 2. Qual é a Ordem? (Controle de Fluxo Sequencial)

Os estágios são executados **sequencialmente** e em uma **ordem predefinida** (geralmente `build`, `test`, `deploy`). O *pipeline* adota uma regra estrita:

* O Estágio **só pode avançar** para o próximo na sequência se **todos os jobs** no estágio atual forem concluídos com sucesso.
* Qualquer falha em um único job dentro de um estágio faz com que o estágio falhe e, por padrão, interrompe o *pipeline* inteiro.

---

## 3. Qual a Relação com os Jobs? (Execução Paralela)

Embora os estágios sejam sequenciais, os trabalhos (jobs) pertencentes ao **mesmo estágio** são executados **em paralelo**.

* O Estágio só é considerado finalizado quando o último job dentro dele termina com êxito. Essa execução paralela otimiza o tempo total do *pipeline*.

| Estágio | Exemplo de Uso | Tipo de Execução |
| :---: | :---: | :---: |
| **Build** | `job_compilar_backend`, `job_compilar_frontend` | **Paralela** |
| **Test** | `job_unitarios`, `job_integracao`, `job_seguranca` | **Paralela** |
| **Deploy** | `job_deploy_staging`, `job_deploy_producao` | **Paralela/Sequencial (conforme configuração)** |
