-- Création de la base de données
CREATE DATABASE GestionVentes;

USE GestionVentes;


-- Table des clients
CREATE TABLE Client
(
    ClientID INT PRIMARY KEY,
    Nom VARCHAR(100),
    Ville VARCHAR(50),
    DateCreation DATE
);


-- Table des ventes
CREATE TABLE Vente
(
    VenteID INT PRIMARY KEY,
    ClientID INT,
    DateVente DATE,
    Montant DECIMAL(10,2),

    CONSTRAINT FK_Client_Vente
    FOREIGN KEY(ClientID)
    REFERENCES Client(ClientID)
);