-- Comando para criar a tabela de exemplo
-- O CREATE TABLE seguido do nome da tabela serve para criar a tabela, é como começamos toda criação do BD no SGBD
CREATE TABLE Funcionarios (
    ID_Funcionario INT PRIMARY KEY, -- INT indica que é um interio e PRIMARY KEY indica que é a chave primaria
    Nome VARCHAR(100) NOT NULL, -- VARCHAR indica até 100 caracteres e NOT NULL indica que não pode estar vazio
    Departamento VARCHAR(50) NOT NULL, 
    Salario DECIMAL(10, 2) NOT NULL --  DECIMAL(10, 2) que o tamanho do número é 10 e o decimal é 2 ex.: 12345678.90
);

-- Inserir dados de exemplo (com salários variados em cada departamento)
INSERT INTO Funcionarios (ID_Funcionario, Nome, Departamento, Salario) VALUES
-- INSERT INTO mais nome da tabala indica onde queremos insereir dados
-- logo (selecionamos os atributos ou VALUES que queremos popular desntro dos parênteses) VALUES indica que começaremos a inserir os dados a seguir 
(1, 'Alice',   'Vendas', 60000.00),
-- ID_Funcionario, Nome, Departamento, Salario
(2, 'Bruno',   'Vendas', 55000.00),
(3, 'Carla',   'Vendas', 72000.00), -- Mais alto em Vendas
(4, 'David',   'TI',     95000.00), -- Mais alto em TI
(5, 'Elisa',   'TI',     80000.00),
(6, 'Fábio',   'TI',     85000.00),
(7, 'Gustavo', 'RH',     48000.00),
(8, 'Helena',  'RH',     48000.00), -- Salário empatado
(9, 'Igor',    'RH',     50000.00);

-- SELECT é para começar um busca, basicamente é como selecionar frutas em uma bacia de frutas
-- os nomes logo a seguir são os atributos a nos quais os dados vão ser selecionados
-- FROM é a tabela onde os atributos estão
SELECT
    Nome,
    Departamento,
    Salario,
    -- Aplicação da função de janela
    -- ROW_NUMBER() OVER() é como se criasse uma sub-tabela como os atributos que lhe são pedido
    -- PARTITION BY atributo cria uma sub-tabela direfetene para cada atributo
    -- ORDER BY aqui pega cada salario do departamento selecionado e mostra de forma decrescente
    -- as no final nomeia o resultado como Rank_Salario_Departamento para usarmos depois de forma mais legível e para poder referenciar
    ROW_NUMBER() OVER (
        PARTITION BY Departamento  -- Agrupa e reinicia a contagem por Departamento
        ORDER BY Salario DESC      -- Ordena por Salário dentro de cada grupo
    ) as Rank_Salario_Departamento
FROM
    Funcionarios
ORDER BY
    -- ORDER BY ordena primeiro pelo departamento por ordem alfabética, isso vem por padrão e pode ser modificado
    -- logo ordena pelo segundo item que é o resultado do ROW_NUMBER()
    Departamento, Rank_Salario_Departamento;



    -- Departamento (1º critério),Rank_Salario_Departamento (2º critério)
    -- TI,1 (Salário mais alto em TI)
    -- TI,2
    -- TI,3
    -- Vendas,1 (Salário mais alto em Vendas)
    -- Vendas,2
    -- Vendas,3