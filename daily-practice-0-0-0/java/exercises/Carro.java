package java.exercises;

public class Carro {

    // Método que simula a ação de acelerar e imprime "Vrum!"
    public void acelerar() {
        System.out.println("Vrum!");
    }

    // Método principal (main) para testar a classe
    public static void main(String[] args) {
        // 1. Cria um novo objeto Carro
        Carro meuCarro = new Carro();

        // 2. Chama o método acelerar()
        System.out.println("Preparando para acelerar...");
        meuCarro.acelerar(); // Isso imprimirá "Vrum!"
    }
}