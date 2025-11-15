package java.exercises.exercicioA;

public class Main {
    public static void main(String[] args) {
        
        // --- Acesso ao Campo Constante (na main) ---
        
        // A constante é acessada diretamente pela CLASSE (Configuracao.MAX_TENTATIVAS).
        // Não é necessário criar um objeto de Configuracao para acessá-la.
        int limite = Configuracao.MAX_TENTATIVAS;
        
        System.out.println("O valor da constante MAX_TENTATIVAS é: " + limite);
        System.out.println("Acessado diretamente pela classe: " + Configuracao.MAX_TENTATIVAS);
        
        // Demonstração da Imutabilidade (gera erro de compilação se descomentada)
        // Configuracao.MAX_TENTATIVAS = 10; // ERRO: Não é possível atribuir um valor a uma variável final
        
        System.out.println("\n--- Exemplo com Instância ---");
        Configuracao minhaConfig = new Configuracao("App Financeiro");
        
        // A constante pode ser acessada através da instância, mas a notação via Classe
        // é a forma correta e recomendada em Java.
        System.out.println("Acessado via instância: " + minhaConfig.MAX_TENTATIVAS);
        System.out.println("Nome do App: " + minhaConfig.getNomeApp());
    }
}