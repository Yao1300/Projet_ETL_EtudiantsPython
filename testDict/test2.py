# test2.py

# ============================================================
# Dictionnaire contenant les étudiants
# ============================================================

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


# ============================================================
# 1. Afficher tous les étudiants
# ============================================================

print("\n===== LISTE DES ÉTUDIANTS =====")

for id_etudiant, infos in etudiants.items():
    print(
        "ID :", id_etudiant,
        "| Nom :", infos["nom"],
        "| Âge :", infos["age"],
        "| Ville :", infos["ville"],
        "| Note :", infos["note"]
    )


# ============================================================
# 2. Rechercher un étudiant par ID
# ============================================================

print("\n===== RECHERCHE PAR ID =====")

id_recherche = int(input("Entrez l'identifiant de l'étudiant : "))

if id_recherche in etudiants:

    etudiant = etudiants[id_recherche]

    print("\nInformations de l'étudiant")
    print("ID :", id_recherche)
    print("Nom :", etudiant["nom"])
    print("Âge :", etudiant["age"])
    print("Ville :", etudiant["ville"])
    print("Note :", etudiant["note"])

else:
    print("Étudiant introuvable.")


# ============================================================
# 3. Ajouter un étudiant
# ============================================================

print("\n===== AJOUT D'UN ÉTUDIANT =====")

nouvel_id = 4

etudiants[nouvel_id] = {
    "nom": "Jean",
    "age": 23,
    "ville": "Longueuil",
    "note": 78
}

print("Étudiant ajouté :", etudiants[nouvel_id])


# ============================================================
# 4. Modifier un étudiant
# ============================================================

print("\n===== MODIFICATION =====")

etudiants[2]["age"] = 23
etudiants[2]["ville"] = "Montreal"
etudiants[2]["note"] = 88

print("Informations modifiées pour Paul :")
print(etudiants[2])


# ============================================================
# 5. Supprimer un étudiant
# ============================================================

print("\n===== SUPPRESSION =====")

id_suppression = 3

if id_suppression in etudiants:
    del etudiants[id_suppression]
    print("Étudiant", id_suppression, "supprimé.")
else:
    print("Étudiant introuvable.")


# ============================================================
# 6. Rechercher un étudiant par nom
# ============================================================

print("\n===== RECHERCHE PAR NOM =====")

nom_recherche = input("Entrez le nom de l'étudiant : ")

trouve = False

for id_etudiant, infos in etudiants.items():

    if infos["nom"].lower() == nom_recherche.lower():

        print("\nÉtudiant trouvé")
        print("ID :", id_etudiant)
        print("Nom :", infos["nom"])
        print("Âge :", infos["age"])
        print("Ville :", infos["ville"])
        print("Note :", infos["note"])

        trouve = True

if not trouve:
    print("Étudiant introuvable.")


# ============================================================
# 7. Afficher les étudiants ayant une note >= 80
# ============================================================

print("\n===== ÉTUDIANTS AVEC NOTE >= 80 =====")

for id_etudiant, infos in etudiants.items():

    if infos["note"] >= 80:

        print(
            "ID :", id_etudiant,
            "| Nom :", infos["nom"],
            "| Note :", infos["note"]
        )


# ============================================================
# 8. Calculer la moyenne des notes
# ============================================================

print("\n===== MOYENNE DES NOTES =====")

total = 0

for infos in etudiants.values():
    total += infos["note"]

moyenne = total / len(etudiants)

print("Moyenne :", moyenne)


# ============================================================
# 9. Trouver le meilleur étudiant
# ============================================================

print("\n===== MEILLEUR ÉTUDIANT =====")

meilleur = None

for id_etudiant, infos in etudiants.items():

    if meilleur is None or infos["note"] > meilleur["note"]:

        meilleur = {
            "id": id_etudiant,
            "nom": infos["nom"],
            "note": infos["note"]
        }

print("Meilleur étudiant :", meilleur["nom"])
print("ID :", meilleur["id"])
print("Note :", meilleur["note"])


# ============================================================
# 10. Compter les étudiants d'une ville
# ============================================================

print("\n===== RECHERCHE PAR VILLE =====")

ville_recherche = input("Entrez la ville : ")

compteur = 0

for infos in etudiants.values():

    if infos["ville"].lower() == ville_recherche.lower():
        compteur += 1

print(
    "Nombre d'étudiants à",
    ville_recherche,
    ":",
    compteur
)


# ============================================================
# 11. Afficher les étudiants majeurs
# ============================================================

print("\n===== ÉTUDIANTS MAJEURS =====")

for id_etudiant, infos in etudiants.items():

    if infos["age"] >= 18:

        print(
            "ID :", id_etudiant,
            "| Nom :", infos["nom"],
            "| Âge :", infos["age"]
        )


# ============================================================
# 12. Afficher le dictionnaire final
# ============================================================

print("\n===== DICTIONNAIRE FINAL =====")

for id_etudiant, infos in etudiants.items():

    print(id_etudiant, ":", infos)