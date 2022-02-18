#PIERRE FEUILLE CISEAUX
import os
import random
continuer = True
score_ordi = 0
score_joueur = 0
nom_joueur = str(input("Quel est votre nom ? "))
print("\nBienvenue dans le jeu Pierre, Feuille, Ciseaux en python", nom_joueur,"!\n")

Pierre = 0
Feuille = 0
Ciseaux = 0
liste_ordi = ["P", "C", "F"]


while continuer:
    #Semi-Intelligence artificelle (c'est faux):
    if Pierre > Feuille and Pierre > Ciseaux:
        liste_ordi += "F"
    elif Feuille > Pierre and Feuille > Ciseaux:
        liste_ordi += "C"
    elif Ciseaux > Pierre and Ciseaux > Feuille:
        liste_ordi += "P"
    if Pierre == 10 or Feuille == 10 or Ciseaux == 10:
        liste_ordi = ["P", "C", "F"]


    #Partie pour l'ordi
    choix_ordi = random.choice(liste_ordi)

    #Partie pour le joueur et vérification des résultats
    print("A vous de jouer", nom_joueur," !!!")
    choix_joueur = str(input("Choisissez entre P pour Pierre, F pour Feuille, C pour Ciseaux (attention à la majuscule): "))
    if choix_joueur == "P":
        Pierre += 1
    elif choix_joueur == "F":
        Feuille += 1
    elif choix_joueur == "C":
        Ciseaux += 1
    if choix_ordi == choix_joueur:
        print("\n Match nul !\n")
    elif choix_ordi == "P" and choix_joueur == "C":
        score_ordi += 1
        print("\n L'ordi est gagnant, la pierre casse les ciseaux \n")
    elif choix_joueur == "P" and choix_ordi == "C":
        score_joueur += 1
        print("\n Vous êtes gagnant, la pierre casse les ciseaux \n")
    elif choix_ordi == "F" and choix_joueur == "P":
        score_ordi += 1
        print("\n L'ordi est gagnant, la feuille enroule la pierre \n")
    elif choix_joueur == "F" and choix_ordi == "P":
        score_joueur += 1
        print("\n Vous êtes gagnant, la feuille enroule la pierre \n")
    elif choix_ordi == "C" and choix_joueur == "F":
        score_ordi += 1
        print("\n L'ordi est gagnant, les ciseaux coupent la feuille \n")
    elif choix_joueur == "C" and choix_ordi == "F":
        score_joueur += 1
        print("\n Vous êtes gagnant, les ciseaux coupent la feuille \n")
    print(" Score ordi =", score_ordi)
    print(" Score", nom_joueur,"=", score_joueur,"\n")
    print(liste_ordi)
    continuer = int(input("Voulez vous continuer ?? Tapez 1 pour oui ou 2 pour non: "))
    os.system("cls")
    if continuer == 2:
        exit()

#Crédits: XS1lv3r

