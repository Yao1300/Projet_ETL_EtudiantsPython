/* =========================================================
   PROJET ETL VENTES - SQL SERVER
   ========================================================= */


/* =========================================================
   1. CREATION DE LA BASE DE DONNEES
   ========================================================= */

IF DB_ID('ETL_BI') IS NULL
BEGIN
    CREATE DATABASE ETL_BI;
END;
GO


/* =========================================================
   2. UTILISATION DE LA BASE
   ========================================================= */

USE ETL_BI;
GO


/* =========================================================
   3. SUPPRESSION DE L'ANCIENNE TABLE
   ========================================================= */

IF OBJECT_ID('dbo.Ventes', 'U') IS NOT NULL
BEGIN
    DROP TABLE dbo.Ventes;
END;
GO


/* =========================================================
   4. CREATION DE LA TABLE VENTES
   ========================================================= */

CREATE TABLE dbo.Ventes
(
    VenteID INT IDENTITY(1,1) PRIMARY KEY,

    DateVente DATE NOT NULL,

    Client VARCHAR(100) NOT NULL,

    Ville VARCHAR(100) NOT NULL,

    Produit VARCHAR(100) NOT NULL,

    Categorie VARCHAR(100) NOT NULL,

    Quantite INT NOT NULL,

    Prix_Unitaire DECIMAL(10,2) NOT NULL,

    Chiffre_Affaires DECIMAL(12,2) NOT NULL
);
GO


/* =========================================================
   5. INSERTION DES DONNEES
   ========================================================= */

INSERT INTO Ventes (
    DateVente,
    Client,
    Ville,
    Produit,
    Categorie,
    Quantite,
    Prix_Unitaire,
    Chiffre_Affaires
)
VALUES
('2026-01-05', 'Client A', 'Montreal', 'Ordinateur', 'Informatique', 2, 850, 1700),
('2026-01-08', 'Client B', 'Laval', 'Souris', 'Accessoires', 5, 35, 175),
('2026-01-12', 'Client C', 'Montreal', 'Clavier', 'Accessoires', 3, 75, 225),
('2026-01-15', 'Client D', 'Longueuil', 'Ordinateur', 'Informatique', 1, 950, 950),
('2026-01-20', 'Client E', 'Montreal', 'Ecran', 'Informatique', 2, 320, 640),
('2026-02-03', 'Client A', 'Montreal', 'Clavier', 'Accessoires', 4, 70, 280),
('2026-02-10', 'Client F', 'Laval', 'Ordinateur', 'Informatique', 1, 900, 900),
('2026-02-18', 'Client C', 'Montreal', 'Souris', 'Accessoires', 6, 30, 180),
('2026-02-22', 'Client B', 'Laval', 'Ecran', 'Informatique', 2, 300, 600),
('2026-03-05', 'Client D', 'Longueuil', 'Ordinateur', 'Informatique', 2, 880, 1760);
GO


/* =========================================================
   6. VERIFICATION DES DONNEES
   ========================================================= */

SELECT *
FROM dbo.Ventes;
GO


/* =========================================================
   7. KPI PRINCIPAUX
   ========================================================= */

SELECT
    SUM(Chiffre_Affaires) AS Chiffre_Affaires_Total,

    COUNT(*) AS Nombre_Commandes,

    SUM(Quantite) AS Quantite_Totale,

    AVG(Chiffre_Affaires) AS Panier_Moyen

FROM dbo.Ventes;
GO


/* =========================================================
   8. CHIFFRE D'AFFAIRES PAR VILLE
   ========================================================= */

SELECT
    Ville,
    COUNT(*) AS Nombre_Commandes,
    SUM(Quantite) AS Quantite_Totale,
    SUM(Chiffre_Affaires) AS Chiffre_Affaires

FROM dbo.Ventes

GROUP BY Ville

ORDER BY Chiffre_Affaires DESC;
GO


/* =========================================================
   9. CHIFFRE D'AFFAIRES PAR CATEGORIE
   ========================================================= */

SELECT
    Categorie,
    COUNT(*) AS Nombre_Commandes,
    SUM(Quantite) AS Quantite_Totale,
    SUM(Chiffre_Affaires) AS Chiffre_Affaires

FROM dbo.Ventes

GROUP BY Categorie

ORDER BY Chiffre_Affaires DESC;
GO


/* =========================================================
   10. CHIFFRE D'AFFAIRES PAR PRODUIT
   ========================================================= */

SELECT
    Produit,
    SUM(Quantite) AS Quantite_Vendue,
    SUM(Chiffre_Affaires) AS Chiffre_Affaires

FROM dbo.Ventes

GROUP BY Produit

ORDER BY Chiffre_Affaires DESC;
GO


/* =========================================================
   11. CHIFFRE D'AFFAIRES PAR CLIENT
   ========================================================= */

SELECT
    Client,
    COUNT(*) AS Nombre_Commandes,
    SUM(Quantite) AS Quantite_Achetee,
    SUM(Chiffre_Affaires) AS Chiffre_Affaires

FROM dbo.Ventes

GROUP BY Client

ORDER BY Chiffre_Affaires DESC;
GO


/* =========================================================
   12. CHIFFRE D'AFFAIRES PAR MOIS
   ========================================================= */

SELECT
    YEAR(DateVente) AS Annee,
    MONTH(DateVente) AS Mois,
    SUM(Chiffre_Affaires) AS Chiffre_Affaires

FROM dbo.Ventes

GROUP BY
    YEAR(DateVente),
    MONTH(DateVente)

ORDER BY
    Annee,
    Mois;
GO