class Veiculo:
    """
    Classe base para todos os veículos.
    """
    def __init__(self, marca, modelo, velocidade_max):
        self.marca = marca
        self.modelo = modelo
        self.velocidade_max = velocidade_max

    def detalhes(self):
        """
        Retorna os detalhes básicos do veículo.
        """
        return f"Marca: {self.marca}, Modelo: {self.modelo}, V. Máxima: {self.velocidade_max} km/h"

class Carro(Veiculo):
    """
    Classe Carro, herda de Veiculo e adiciona o número de portas.
    """
    def __init__(self, marca, modelo, velocidade_max, num_portas):
        # Chamada ao construtor da classe base
        super().__init__(marca, modelo, velocidade_max)
        self.num_portas = num_portas

    def detalhes(self):
        """
        Sobrescreve: Adiciona o número de portas aos detalhes da classe base.
        """
        detalhes_base = super().detalhes() # Reutiliza o método da classe pai
        return f"{detalhes_base}, Portas: {self.num_portas}"

    def acelerar(self):
        """
        Método exclusivo de Carro.
        """
        return f"O {self.modelo} está acelerando de forma potente!"

class Bicicleta(Veiculo):
    """
    Classe Bicicleta, herda de Veiculo e adiciona a informação de marchas.
    """
    def __init__(self, marca, modelo, velocidade_max, tem_marchas):
        super().__init__(marca, modelo, velocidade_max)
        self.tem_marchas = tem_marchas

    def detalhes(self):
        """
        Sobrescreve: Adiciona a informação de marchas aos detalhes.
        """
        marchas_info = "Tem marchas" if self.tem_marchas else "Não tem marchas"
        detalhes_base = super().detalhes()
        return f"{detalhes_base}, Configuração: {marchas_info}"

    def tocar_campainha(self):
        """
        Método exclusivo de Bicicleta.
        """
        return "Trim Trim! (A bicicleta está a tocar a campainha)"

class Moto(Veiculo):
    """
    Classe Moto, herda de Veiculo e adiciona a informação de cilindradas.
    """
    def __init__(self, marca, modelo, velocidade_max, cilindradas):
        super().__init__(marca, modelo, velocidade_max)
        self.cilindradas = cilindradas

    def detalhes(self):
        """
        Sobrescreve: Adiciona as cilindradas aos detalhes.
        """
        detalhes_base = super().detalhes()
        return f"{detalhes_base}, Cilindradas: {self.cilindradas}cc"
    
    def empinar(self):
        """
        Método exclusivo de Moto.
        """
        return "A moto está empinando!"
    


# --- Teste das Instâncias ---

# 1. Carro
meu_carro = Carro("Fiat", "Uno", 160, 4)
print("\n--- Objeto Carro ---")
print(meu_carro.detalhes())
print(meu_carro.acelerar())

# 2. Bicicleta
minha_bike = Bicicleta("Caloi", "Elite", 40, True)
print("\n--- Objeto Bicicleta ---")
print(minha_bike.detalhes())
print(minha_bike.tocar_campainha())

# # 3. Moto
# minha_moto = Moto("Yamaha", )