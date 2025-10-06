
## 1. O que é um Artefato de Build?

O **Artefato de Build** (ou Artefato de Software) é o produto concreto, o resultado final ou intermediário de um processo de compilação ( **build** ) de um projeto. É o item distribuível que contém o código compilado e, em alguns casos, recursos e metadados necessários para que o software funcione ou seja usado como dependência.

Essencialmente, é a embalagem do seu código.

**Exemplos Comuns de Artefatos:**

* **Arquivos JAR** (Java Archive): Para bibliotecas ou aplicações Java.
* **Arquivos WAR** (Web Archive): Para aplicações web.
* **Arquivos EAR** (Enterprise Archive): Para aplicações corporativas mais complexas.
* **Pacotes NuGet, RPM, DEB, ou binários** (executáveis).

As ferramentas de build, como Maven (`mvn package`) e Gradle, são responsáveis por coletar, compilar, testar e empacotar todos os arquivos do seu projeto em um ou mais artefatos.

---

## 2. O que é um Snapshot (Instantâneo)?

Um **Snapshot** (Instantâneo) não é um tipo de artefato, mas sim uma **política de versionamento** aplicada a um artefato. Ele indica que o artefato é uma **versão de desenvolvimento** que ainda não é final e está sujeita a mudanças.

No Maven e Gradle, uma versão é considerada um Snapshot se ela for sufixada com **`-SNAPSHOT`** (exemplo: `1.0.0-SNAPSHOT`).

**Propriedades Chave de um Snapshot:**

* **Instabilidade/Desenvolvimento:** É o código mais recente em uma linha de desenvolvimento, antes que a versão final (Release) seja lançada.
* **Mutabilidade:** Um artefato **`1.0.0-SNAPSHOT`** pode ser gerado e publicado várias vezes no repositório (Nexus, Artifactory, etc.) ao longo do dia, e o conteúdo de cada build será diferente, mas o nome do artefato será sempre o mesmo.
* **Resolução de Dependência:** Quando um projeto consome uma dependência `-SNAPSHOT`, o Maven/Gradle verifica o repositório remoto periodicamente (geralmente diariamente por padrão, mas pode ser configurado) para garantir que está usando o **build mais recente** daquele Snapshot, pois ele presume que o código pode ter mudado.

---

## 3. Principais Diferenças

A diferença fundamental reside no **escopo** e na  **natureza da mudança** .

| Característica           | Artefato de Build                                                   | Snapshot                                                                                            |
| ------------------------- | ------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Definição**     | O**produto físico**(arquivo JAR/WAR) da compilação.        | A**política de versionamento**que o artefato possui.                                         |
| **Escopo**          | Termo**genérico**para qualquer saída de build.              | Termo**específico**para artefatos em desenvolvimento.                                        |
| **Mutabilidade**    | **Pode ser**um Release (imutável) ou um Snapshot (mutável). | **Sempre Mutável**(pode ser substituído por um novo build com o mesmo nome).                |
| **Identificação** | Pelo seu nome e versão completos.                                  | Pela presença do sufixo**`-SNAPSHOT`**na versão.                                                |
| **Propósito**      | Ser o componente distribuível/dependência.                        | Facilitar a colaboração e o consumo de código**em desenvolvimento**entre equipes/módulos. |

**Em Resumo:**

Todo **Snapshot** é um  **Artefato de Build** , mas nem todo **Artefato de Build** é um  **Snapshot** .

* Um artefato com a versão **`1.0.0-RELEASE`** ou apenas **`1.0.0`** é um **Artefato de Build** do tipo **Release** (final e imutável).
* Um artefato com a versão **`1.0.0-SNAPSHOT`** é um **Artefato de Build** do tipo **Snapshot** (em desenvolvimento e mutável).


---



Essa é a parte crucial! Saber a diferença entre um *Snapshot* e um *Artefato de Build* (especificamente, a distinção entre um Snapshot e um  **Release** ) é fundamental para a  **estabilidade** , a **reprodutibilidade** e a **eficiência** de qualquer pipeline de Integração Contínua/Entrega Contínua (CI/CD) e para o gerenciamento de dependências.

Aqui estão os principais motivos pelos quais essa distinção é importante:

## 1. Garantir a Reprodutibilidade (O Padrão Ouro)

Este é o ponto mais crítico.

* **Artefatos de *Release* (imutáveis)** : Quando um artefato é publicado como uma versão de *release* (ex: `1.0.0`), ele é considerado  **imutável** . O que isso significa? Se você baixar o `1.0.0` hoje e baixá-lo daqui a um ano, o conteúdo do arquivo (o JAR, WAR, etc.) será  **exatamente o mesmo** . Isso garante que o seu ambiente de produção seja idêntico ao ambiente de homologação, eliminando o problema de "funciona na minha máquina".
* **Artefatos *Snapshot* (mutáveis)** : Como o código `1.0.0-SNAPSHOT` pode ser publicado várias vezes ao dia, se você depender de um Snapshot, o build que você executa hoje pode ser diferente do build que você executa amanhã,  **mesmo que a versão declarada seja a mesma** . Isso torna o build  **não-reprodutível** , algo perigoso para a produção.

## 2. Controlar o Ciclo de Vida do Software

A distinção define em que fase do desenvolvimento um componente se encontra:

* **Snapshots (Fase de Desenvolvimento):** São usados internamente para comunicação rápida e eficiente entre módulos ou equipes que estão trabalhando **simultaneamente** no mesmo ciclo de desenvolvimento. Você não precisa esperar por um *release* formal para testar a funcionalidade mais recente de um módulo vizinho.
* **Releases (Fase de Estabilização e Produção):** São usados como dependências finais para compilação e, crucialmente, são os únicos artefatos que devem ser implantados em ambientes de  **Produção** .

## 3. Otimizar a Resolução de Dependências

Maven e Gradle tratam os dois tipos de forma diferente para otimizar o tempo de build:

* **Resolução de Snapshot:** As ferramentas de build são configuradas para **verificar periodicamente** o repositório remoto para ver se uma versão mais recente do mesmo Snapshot foi publicada. Isso custa tempo, mas é necessário na fase de desenvolvimento.
* **Resolução de Release:** Uma vez que um Release é baixado para o seu repositório local, a ferramenta de build **nunca mais tenta baixá-lo novamente** do repositório remoto, pois sabe que ele é imutável. Isso torna o processo de build muito mais rápido e previsível.

## 4. Gerenciamento de Repositórios

A maioria dos repositórios de artefatos (como Nexus ou Artifactory) armazena e gerencia Snapshots e Releases em áreas separadas, geralmente com políticas de limpeza diferentes:

* **Repositório de Snapshot:** O conteúdo antigo é frequentemente **limpo** (removido) automaticamente para economizar espaço, já que a imutabilidade não é garantida e apenas o build mais recente importa.
* **Repositório de Release:** Os artefatos são **preservados indefinidamente** para garantir a rastreabilidade e a capacidade de reconstruir versões antigas do sistema (reprodutibilidade histórica).

Em suma, a distinção entre um **Artefato Release** (imutável e final) e um **Artefato Snapshot** (mutável e em desenvolvimento) é o que permite que os desenvolvedores trabalhem rapidamente com a versão mais recente do código, **sem comprometer** a estabilidade e a integridade da aplicação final que vai para o cliente.
