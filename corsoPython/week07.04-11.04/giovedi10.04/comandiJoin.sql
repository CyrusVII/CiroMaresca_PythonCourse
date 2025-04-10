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

--Si vuole recuperare dal database WORLD le lingue parlate per nazione con la rispettiva percentuale di utilizzo
SELECT co.Name AS Nazione, cl.Language AS Lingua, cl.Percentage AS Percentuale
FROM country co
JOIN countrylanguage cl ON co.Code = cl.CountryCode
ORDER BY co.Name, cl.Percentage DESC;

--si vuole recuperare dal database WORLD le nazioni e la lingua più parlata con percentuale;
SELECT co.Name AS Nazione, cl.Language AS Lingua, cl.Percentage AS Percentuale
FROM country co
JOIN countrylanguage cl ON co.Code = cl.CountryCode
WHERE (co.Code, cl.Percentage) IN (
SELECT CountryCode, MAX(Percentage)
FROM countrylanguage
GROUP BY CountryCode
)
ORDER BY co.Name;

--Visualizzato il nome del paese, la lingua ufficiale parlata e il nome della capitale, includendo solo i paesi con una popolazione superiore a 50 milioni.
SELECT co.Name AS Paese, cl.Language AS Lingua_Ufficiale, co.Capital AS Capitale
FROM country co
JOIN countrylanguage cl ON co.Code = cl.CountryCode
WHERE co.Population > 50000000 AND cl.IsOfficial = 'T'
ORDER BY co.Name;

--creiamo una view dalla base dell esercizio precedente
CREATE VIEW PaesiConLinguaUfficiale AS
SELECT co.Name AS Paese, cl.Language AS Lingua_Ufficiale, ci.Name AS Capitale, co.Population AS Popolazione
FROM country co
JOIN city ci ON co.Capital = ci.ID
JOIN countrylanguage cl ON co.Code = cl.CountryCode
WHERE co.Population > 50000000 AND cl.IsOfficial = 'T'
ORDER BY co.Name;

--Create una vista chiamata PopulationByContinent che mostri il nome del continente e la popolazione totale per ciascun continente.
CREATE VIEW PopulationByContinent AS
SELECT co.Continent, SUM(co.Population) AS PopolazioneTotale
FROM country co
GROUP BY co.Continent
ORDER BY co.Continent;





