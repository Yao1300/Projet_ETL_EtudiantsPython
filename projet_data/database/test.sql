-- Afficher la version de SQL Server
SELECT @@VERSION;
GO

-- Afficher la date et l'heure actuelles
SELECT GETDATE() AS DateActuelle;
GO

-- Créer une base de données
CREATE DATABASE TestSQL;
GO

-- Utiliser la base de données
USE TestSQL;
GO

-- Créer une table
CREATE TABLE Etudiants (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Nom VARCHAR(50),
    Prenom VARCHAR(50),
    Age INT
);
GO

-- Insérer des données
INSERT INTO Etudiants (Nom, Prenom, Age)
VALUES
('Dupont', 'Jean', 22),
('Martin', 'Marie', 24),
('Akakpo', 'Yao', 30);
GO

-- Afficher les données
SELECT * FROM Etudiants;
GO