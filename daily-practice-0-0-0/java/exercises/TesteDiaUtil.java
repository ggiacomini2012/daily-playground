package java.exercises;

// 3. Classe principal para testar o uso da enum (o arquivo se chamaria TesteDiaUtil.java)
public class TesteDiaUtil {
    
    // Método principal onde a execução do programa começa
    public static void main(String[] args) {
        
        // 4. DECLARANDO e INICIALIZANDO uma variável do tipo DiaUtil.
        // Você só pode atribuir um dos valores definidos na enum (SEGUNDA, TERCA, etc.).
        DiaUtil hoje = DiaUtil.QUARTA;
        
        // 5. Imprimindo o valor. O Java converte automaticamente para String.
        System.out.println("Hoje é: " + hoje); 
        // Saída: Hoje é: QUARTA
        
        // 6. Comparação: Usamos '==' (igualdade) para comparar valores de enum,
        // o que é seguro e rápido, pois são constantes únicas.
        if (hoje == DiaUtil.QUARTA) {
            System.out.println("Meio da semana! Força!");
        }
        
        // --- Exemplo de como acessar todos os membros ---
        
        System.out.println("\nTodos os dias úteis:");
        
        // 7. O método 'values()' (que toda enum em Java tem) retorna um array
        // com todos os membros da enumeração na ordem em que foram declarados.
        // Usamos um loop 'for-each' para iterar por eles.
        for (DiaUtil dia : DiaUtil.values()) {
            
            // 8. Imprime cada membro.
            System.out.println(dia);
        }
        /* * Saída final do loop:
         * SEGUNDA
         * TERCA
         * QUARTA
         * QUINTA
         * SEXTA
         */
    }
}