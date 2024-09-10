#!/usr/bin/env python3

def lire_fichier_simpliste(chemin_vers_fichier):
    with open(chemin_vers_fichier, ) as fichier:
        contenu = fichier.readlines()

    for ligne in contenu:
        print(ligne.strip())


def lire_fichier(chemin_vers_fichier):
    with open(chemin_vers_fichier, ) as fichier:
        premiere_ligne = fichier.readline()
        contenu = fichier.readlines()
    print("La première ligne est: ", premiere_ligne, "/")
    print("La première ligne est: ", premiere_ligne.strip(), "/")
    for ligne in contenu:
        print(ligne.strip())

if __name__ == '__main__':
    lire_fichier('text.txt')
