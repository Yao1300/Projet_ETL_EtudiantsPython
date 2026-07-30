-- Ajout d'une colonne calculée
ALTER TABLE Vente
ADD Taxe DECIMAL(10,2);


-- Calcul de la taxe
UPDATE Vente
SET Taxe = Montant * 0.15;


-- Création d'une vue analytique
CREATE VIEW Vue_Ventes_Client AS

SELECT
    c.Nom,
    c.Ville,
    COUNT(v.VenteID) AS Nombre_Ventes,
    SUM(v.Montant) AS Total_Achat

FROM Client c

INNER JOIN Vente v
ON c.ClientID = v.ClientID

GROUP BY
    c.Nom,
    c.Ville;