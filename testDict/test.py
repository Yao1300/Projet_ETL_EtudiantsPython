# Dictionnaire contenant les étudiants
etudiants = {
    1: {
        "nom": "Yao",
        "age": 25,
        "ville": "Montreal",
        "note": 85
    },
    2: {
        "nom": "Paul",
        "age": 22,
        "ville": "Quebec",
        "note": 72
    },
    3: {
        "nom": "Marie",
        "age": 24,
        "ville": "Laval",
        "note": 91
    }
}

# Afficher tous les étudiants
print("Liste des étudiants :")

for id_etudiant, infos in etudiants.items():
    print(
        id_etudiant,
        infos["nom"],
        infos["age"],
        infos["ville"],
        infos["note"]
    )

# Rechercher un étudiant
id_recherche = int(input("\nEntrez l'identifiant de l'étudiant : "))

if id_recherche in etudiants:
    etudiant = etudiants[id_recherche]

    print("\nInformations de l'étudiant")
    print("Nom :", etudiant["nom"])
    print("Âge :", etudiant["age"])
    print("Ville :", etudiant["ville"])
    print("Note :", etudiant["note"])

else:
    print("Étudiant introuvable.")