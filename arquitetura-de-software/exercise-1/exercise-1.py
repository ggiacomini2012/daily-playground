from abc import ABC, abstractmethod

# Interface (Produto Abstrato)
class Conexao(ABC):
    """Define a interface comum para todos os objetos de conexão."""
    @abstractmethod
    def conectar(self):
        pass

# Produto Concreto A
class MySQLConexao(Conexao):
    """Implementa a conexão para um banco de dados MySQL."""
    def conectar(self):
        return "Conexão estabelecida com MySQL Database."

# Produto Concreto B
class PostgreSQLConexao(Conexao):
    """Implementa a conexão para um banco de dados PostgreSQL."""
    def conectar(self):
        return "Conexão estabelecida com PostgreSQL Database."

# A Fábrica (Creator)
class ConnectionFactory:
    """
    A fábrica que decide qual objeto de conexão criar (Factory Method).
    Esta classe encapsula a lógica de configuração do SGBD.
    """
    
    # Simula a leitura de uma variável de ambiente ou arquivo de configuração
    DB_TYPE = "PostgreSQL"  # Altere para "MySQL" para ver o resultado mudar

    @staticmethod
    def get_conexao() -> Conexao:
        """
        O Factory Method. Cria e retorna a instância da conexão correta.
        """
        if ConnectionFactory.DB_TYPE == "MySQL":
            print(f"DEBUG: Criando conexão do tipo {ConnectionFactory.DB_TYPE}...")
            return MySQLConexao()
        
        elif ConnectionFactory.DB_TYPE == "PostgreSQL":
            print(f"DEBUG: Criando conexão do tipo {ConnectionFactory.DB_TYPE}...")
            return PostgreSQLConexao()
        
        else:
            raise ValueError("Tipo de Banco de Dados não suportado na configuração.")

# --- USO PELO CLIENTE ---

# 1. O código cliente usa a fábrica para obter a conexão
print("--- Aplicação solicita a conexão ---")
conexao_app = ConnectionFactory.get_conexao()

# 2. O cliente usa a interface comum, sem saber a classe concreta
resultado = conexao_app.conectar()

print("\nResultado da Conexão:")
print(resultado)