package java.exercises.exercicioA;

public class Configuracao {
    /**
     * Campo final static (constante de classe).
     *
     * - static: O campo pertence à classe, não a objetos individuais.
     * - final: O valor é uma constante e não pode ser alterado após a inicialização.
     */
    public static final int MAX_TENTATIVAS = 5;

    // Outros campos de instância (não estáticos)
    private String nomeApp;

    public Configuracao(String nomeApp) {
        this.nomeApp = nomeApp;
    }

    public String getNomeApp() {
        return nomeApp;
    }
}