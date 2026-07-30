-- Chiffre d'affaires total
SELECT 
    SUM(Montant) AS Chiffre_Affaires
FROM Ventes;


-- Analyse par client
SELECT
    c.Nom,
    COUNT(v.VenteID) AS Nombre_Commandes,
    SUM(v.Montant) AS Total_Achats

FROM Clients c

INNER JOIN Ventes v
ON c.ClientID = v.ClientID

GROUP BY c.Nom;


--Création d'une vue pour Power BI
CREATE VIEW Vue_Performance_Client AS

SELECT

    c.Nom,
    c.Ville,
    COUNT(v.VenteID) AS Nombre_Commandes,
    SUM(v.Montant) AS Chiffre_Affaires

FROM Clients c

LEFT JOIN Ventes v
ON c.ClientID = v.ClientID

GROUP BY 
    c.Nom,
    c.Ville;

--Procédure stockée SQL Server

CREATE PROCEDURE Calculer_Chiffre_Affaires

AS

BEGIN

SELECT 
    SUM(Montant) AS Total_Ventes

FROM Ventes;

END;

EXEC Calculer_Chiffre_Affaires;

--Fact_Vente
CREATE TABLE Fact_Vente
(
    VenteID INT PRIMARY KEY,
    ClientKey INT,
    ProduitKey INT,
    DateKey INT,
    Montant DECIMAL(10,2)
);


-- Dim_Client
CREATE TABLE Dim_Client
(
    ClientKey INT PRIMARY KEY,
    Nom VARCHAR(100),
    Ville VARCHAR(50)
);
