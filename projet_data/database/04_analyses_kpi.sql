SELECT 
    SUM(Montant) AS Chiffre_Affaires
FROM Vente;

--Meilleurs clients
SELECT
    c.Nom,
    SUM(v.Montant) AS Total_Achat

FROM Client c

JOIN Vente v
ON c.ClientID = v.ClientID

GROUP BY c.Nom

ORDER BY Total_Achat DESC;

--Analyse mensuelle
SELECT
    YEAR(DateVente) AS Annee,
    MONTH(DateVente) AS Mois,
    SUM(Montant) AS Revenus

FROM Vente

GROUP BY
    YEAR(DateVente),
    MONTH(DateVente);