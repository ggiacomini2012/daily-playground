-- Criação da tabela de clientes
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(70) NOT NULL,
    idade INTEGER NOT NULL CHECK (idade >= 0 AND idade < 150),
    cidade VARCHAR(70)
);

-- Inserção de dados
INSERT INTO clientes (id, nome, idade, cidade) VALUES
(1, 'Alice Silva', 30, 'São Paulo'),
(2, 'Bruno Costa', 24, 'Rio de Janeiro'),
(3, 'Carla Oliveira', 45, 'Belo Horizonte'),
(4, 'Daniel Pereira', 28, 'São Paulo'),
(5, 'Elisa Santos', 35, 'Curitiba');

SELECT *
FROM clientes
ORDER BY nome DESC;