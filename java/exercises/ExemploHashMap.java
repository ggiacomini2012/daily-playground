package java.exercises;

import java.util.HashMap;
import java.util.Map;

public class ExemploHashMap {
    public static void main(String[] args) {
        // 1. Declare uma variável do tipo 'Map' que mapeia 'Integer' para 'String'
        //    e a inicialize com uma instância de 'HashMap'.
        Map<Integer, String> mapaDeNomes = new HashMap<>();

        // 2. Adicione um par chave-valor a ela.
        mapaDeNomes.put(1, "João Silva");

        // (Opcional) Imprime o mapa para verificar o resultado.
        System.out.println(mapaDeNomes);
    }
}