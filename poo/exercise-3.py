class Veiculo:
    """Classe base para todos os veículos."""
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def ligar(self):
        """Método base para ligar um veículo."""
        return f"O {self.marca} {self.modelo} está ligado."

class Carro(Veiculo):
    """Subclasse que representa um Carro, que é um tipo de Veículo."""
    # O método __init__ é herdado automaticamente se não for definido aqui.

    def ligar(self):
        """
        Sobrescreve o método ligar() da classe Veiculo.
        Um carro 'ligado' está implicitamente 'em movimento' neste contexto.
        """
        return f"O {self.marca} {self.modelo} está em movimento."

# -----------------------------------------------------
# Demonstração
# -----------------------------------------------------

# 1. Instância da Classe Base (Veiculo)
moto = Veiculo("Honda", "CG 160")
print(f"Moto: {moto.ligar()}")

# 2. Instância da Subclasse (Carro)
sedan = Carro("Toyota", "Corolla")
print(f"Carro: {sedan.ligar()}")

# 3. Outra instância da Classe Base (para comparação)
caminhao = Veiculo("Volvo", "FH16")
print(f"Caminhão: {caminhao.ligar()}")