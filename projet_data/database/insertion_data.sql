USE GestionVentes;

INSERT INTO Client
(ClientID, Nom, Ville, DateCreation)

VALUES
(1, 'Jean Dupont', 'Montreal', '2025-01-10'),
(2, 'Marie Martin', 'Quebec', '2025-02-15');


INSERT INTO Vente
(VenteID, ClientID, DateVente, Montant)

VALUES
(100,1,'2025-03-01',250.50),
(101,2,'2025-03-05',430.00);

SELECT * FROM Client;

SELECT * FROM Vente;