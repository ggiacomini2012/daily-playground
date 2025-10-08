SELECT
    nome,
    email
FROM
    clientes
WHERE
    data_cadastro >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH) -- Filtra registros do último mês
ORDER BY
    data_cadastro DESC;