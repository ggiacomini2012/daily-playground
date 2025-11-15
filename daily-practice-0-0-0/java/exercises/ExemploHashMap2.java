package java.exercises;

import java.util.HashMap;
import java.util.Map;

public class ExemploHashMap2 {

    public static void main(String[] args) {
        // 1. Instanciação: Cria o HashMap
        // HashMap<Tipo da Chave, Tipo do Valor> nomeDoMapa = new HashMap<>();
        Map<String, Integer> idades = new HashMap<>();

        // 2. Adição de pares chave-valor
        // O método .put(chave, valor) é usado para adicionar elementos.
        idades.put("Alice", 25);
        idades.put("Bruno", 30);
        idades.put("Célia", 22);

        // 3. (Opcional) Visualizar o mapa para ver o resultado
        System.out.println("Mapa de Idades: " + idades);
        
        // 4. (Opcional) Como acessar um valor pela chave (ex: idade da Alice)
        Integer idadeAlice = idades.get("Alice");
        System.out.println("Idade da Alice: " + idadeAlice);
    }
}