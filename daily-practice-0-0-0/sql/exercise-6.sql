SELECT
    ClienteID,
    COUNT(PedidoID) AS TotalDePedidos
FROM
    Pedidos
GROUP BY
    ClienteID;