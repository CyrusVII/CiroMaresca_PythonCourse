--Si vogliono recuperare dal database "world" la lingua e la nazione di ogni città
SELECT c.Name, co.Name AS Paese, cl.Language
FROM city c
JOIN country co ON c.CountryCode = co.Code
JOIN countrylanguage cl ON co.Code = cl.CountryCode;

--Si vuole recuperare il numero di città per nazione dal database "world "mostrando anche il nome della nazione e ordinarli in base al numero di città.
SELECT co.Name AS Nazione, COUNT(c.Name) AS Numero_città
FROM country co
LEFT JOIN city c ON co.Code = c.CountryCode
GROUP BY co.Name
ORDER BY Numero_città DESC;

--la lista di repubbliche con aspettativa di vita maggiore dei 70 anni, inoltre si vuole visualizzare anche la lingua parlata
SELECT co.Name AS Nazione, co.LifeExpectancy AS Aspettativa_di_vita, cl.Language AS Lingua
FROM country co
JOIN countrylanguage cl ON co.Code = cl.CountryCode
WHERE co.LifeExpectancy > 70 AND cl.IsOfficial = 'T'
ORDER BY co.Name;
