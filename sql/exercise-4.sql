SELECT
    Departamento,
    COUNT(id_funcionario) AS TotalFuncionarios
FROM
    Funcionarios
-- Agrupa os resultados pela coluna Departamento
GROUP BY
    Departamento
-- Filtra os GRUPOS (departamentos) que têm uma contagem de funcionários maior que 10
HAVING
    COUNT(id_funcionario) > 10;