--Scrivete una query SQL che restituisca solo i record dalla tabella "products" con un prezzo superiore a 50.
Select *
FROM products
WHERE buyPrice>50;

--Scrivete una query SQL che restituisca tutti i record dalla tabella "orders"ordinati per data in ordine decrescente.
SELECT *
FROM orders
ORDER BY orderNumber DESC;

--Scrivete una query SQL che aggiorni il prezzo di tutti i prodotti nella tabella"products" aumentandolo del 10%.
UPDATE products
SET buyPrice = buyPrice * 1.10

--Conta quanti dati ci sono nella tabella products colonna buyPrice
SELECT COUNT(buyPrice) 
FROM products;

--Scrivete una query SQL che inserisca un nuovo utente nella tabella customers
INSERT INTO customers (customerName, contactLastName,contactFirstName,phone,addressLine1,city,state,postalCode,country,salesRepEmployeeNumber,creditLimit)
VALUES ('Sam Doe', 'Doe', 'John', '123-456-7890', '123 Main St', 'New York', 'NY', '10001', 'USA', 1370, 50000.00);

--Scrivete una query SQL che elimini tutti gli ordini nella tabella "orders" con uno stato di "Cancelled".
DELETE FROM orderdetails
WHERE orderNumber in (SELECT orderNumber FROM orders WHERE LOWER(status) = 'cancelled');
DELETE FROM orders
WHERE LOWER(status) = 'cancelled'

--Scrivete una query SQL che restituisca tutti gli utenti dalla tabella "customers" il cui nome inizia con la S e vivono in California.
Select * FROM customers
where customerName LIKE 'S%' and state = 'CA'

