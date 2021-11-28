"""
# Projet : Création d'un pendu
# words.py - Contient une liste de listes avec des mots entre 3 et 10 caractères
 ┏━━━━━┓
 ┃     O
 ┃    ─╁─
 ┃    ╱ \
━┻━━
"""
from words import liste_des_mots
import random

def afficherPendu():
    """None -> None
        Affiche le pendu"""
    print(" ┏━━━━━┓ \n"
          " ┃    ",cases[0]," \n"
          " ┃   ",cases[2]+cases[1]+cases[3],"\n"
          " ┃   ",cases[4],cases[5],"\n"
          "━┻━━")

def afficherMotS(lst_s):
    """lst -> None
        Affiche le mot en cours"""
    for k in lst_s:
        print(k, end="")
    print()

def placer_s():
    """ -> None
        Place la partie du corps sur le pendu"""
    for k in range(len(cases)):
        if cases[k] == " ":
            cases[k] = cases_s[k]
            break

def ajouterLettre(lst, lst_s, lettre):
    """lst x list x str -> Bool
        Ajoute les lettres correspondant. Renvoie False s'il n'y en a aucune"""
    trouve = False
    for k in range(len(lst)):
        if lst[k].lower() == lettre.lower() :
            lst_s[k] = lst[k]
            trouve = True
    return trouve

def afficherSeparateur():
    """None -> None
        Affiche une ligne de séparation"""
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

print("Bienvenue dans le jeu du pendu !\n"
      "Les règles du jeu :\n"
      "- Vous allez choisir un nombre de lettre entre 3 et 10\n"
      "- Vous devrez ensuite deviner un mot correspondant au nombre de lettre\n"
      "- Vous avez 6 essais !\n")
afficherSeparateur()
while True:
    cases = [" " for _ in range(6)]
    cases_s = ["O", "╁", "─", "─", "╱", "\ "]
    lettres_testees = []
    nb_lettres = 0
    while nb_lettres < 3 or nb_lettres > 10:
        nb_lettres = int(input("Combien de lettre souhaitez-vous ? (3->10) "))
        if nb_lettres < 3 or nb_lettres > 10:
            print("/!\ Vous devez choisir un nombre entre 3 et 10 !")
    afficherSeparateur()
    mot = random.choice(liste_des_mots[nb_lettres - 3])
    lst_mot = [x for x in mot]
    lst_mot_s = ["_" for _ in range(len(mot))]

    while True:
        if len(lettres_testees) > 0:
            print("Lettres testées :")
            afficherMotS(lettres_testees)
        afficherPendu()
        afficherMotS(lst_mot_s)
        while True :
            lettre = input("Entrez une lettre : ")
            if lettre in lettres_testees:
                print("/!\ Vous avez déjà joué cette lettre !")
            elif "a" > lettre.lower() and lettre.lower() < "z":
                print("/!\ Vous devez jouer une lettre !")
            else :
                break
        lettres_testees.append(lettre)
        if not(ajouterLettre(lst_mot, lst_mot_s, lettre)):
            placer_s()
        afficherSeparateur()
        if cases_s == cases:
            afficherPendu()
            afficherMotS(lst_mot_s)
            print("Perdu ! Vous avez utilisé tous vos essais !\n"
                  "Le mot était : ")
            afficherMotS(lst_mot)
            break
        if lst_mot == lst_mot_s:
            afficherPendu()
            afficherMotS(lst_mot_s)
            print("Bravo ! Vous avez trouvé le mot !")
            break

    Rejouer = "X"
    afficherSeparateur()
    while Rejouer not in ["O", "N"]:
        Rejouer = input("Souhaitez-vous rejouer ? [O/N] ").upper()

    if Rejouer == "N":
        break

afficherSeparateur()
print("Merci d'avoir joué !")
afficherSeparateur()
