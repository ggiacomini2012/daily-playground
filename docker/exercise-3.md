# Adicionando o Serviço PostgreSQL

Você deve adicionar um novo serviço, tipicamente chamado `db` ou `postgres`, ao nível principal do seu arquivo `docker-compose.yml`, ao lado de seus serviços existentes.

**Exemplo de Configuração:**

**YAML**

```
version: '3.8'

services:
  # O seu serviço de aplicação (e.g., frontend, api)
  # [Serviço Existente...]
  app:
    image: minha-imagem-app:latest
    ports:
      - "8080:8080"
    depends_on:
      - db
    environment:
      # Exemplo de como a sua aplicação acessaria o banco
      DATABASE_URL: postgres://user:sua_senha_secreta@db:5432/mydatabase

  # NOVO SERVIÇO DE BANCO DE DADOS
  db:
    image: postgres:15-alpine # Use uma tag estável do PostgreSQL
    container_name: meu-postgres-db
    restart: always
    environment:
      # VARIÁVEL DE AMBIENTE OBRIGATÓRIA
      POSTGRES_PASSWORD: sua_senha_secreta # MUDAR! Use uma senha forte e segura.
      # Opcional: Define o usuário padrão (default é 'postgres')
      POSTGRES_USER: user 
      # Opcional: Define o nome do banco de dados (default é o nome do usuário)
      POSTGRES_DB: mydatabase
    volumes:
      # Opcional, mas recomendado: Persiste os dados fora do container
      - postgres_data:/var/lib/postgresql/data
    ports:
      # Opcional: Expõe a porta para acesso externo (e.g., pgAdmin)
      - "5432:5432"

volumes:
  # Define o volume para persistência de dados
  postgres_data:
```

### Detalhes da Configuração:

1. **`image: postgres:15-alpine`** : Define qual imagem Docker será usada. A imagem oficial do PostgreSQL é a mais comum.
2. **`environment`** : É aqui que você define a  **`POSTGRES_PASSWORD`** . Essa variável de ambiente é exigida pela imagem oficial do PostgreSQL para configurar o banco de dados na primeira execução.
3. **`volumes` (Altamente Recomendado)** : O mapeamento do volume (`postgres_data:/var/lib/postgresql/data`) é crucial para  **persistir os dados** . Sem ele, todos os dados do seu banco seriam perdidos sempre que o contêiner fosse destruído (o que pode acontecer em atualizações ou falhas).
4. **`depends_on: - db` (No serviço da aplicação)** : Isso garante que o Docker Compose inicie o serviço `db` antes de tentar iniciar o seu serviço de aplicação (`app`), pois a aplicação precisa do banco.

Lembre-se de substituir `sua_senha_secreta` por uma senha real e segura. Para ambientes de produção, use **variáveis de ambiente do sistema** ou um **Docker Secret** para evitar expor a senha diretamente no arquivo.
