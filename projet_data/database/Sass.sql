--Table de faits

CREATE TABLE Fact_Vente
(
    VenteKey INT PRIMARY KEY,
    ClientKey INT,
    DateKey INT,
    Montant DECIMAL(10,2)
);

--Dimensions

CREATE TABLE Dim_Client
(
    ClientKey INT PRIMARY KEY,
    Nom VARCHAR(100),
    Ville VARCHAR(50)
);