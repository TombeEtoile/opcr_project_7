"""
Problème : La Tour de Hanoï
Objectif : Déplacer une série de disques de différentes tailles d'une tige à une autre, en utilisant une troisième tige comme aide, tout en respectant certaines règles.

Données :

Trois tiges : une tige de départ, une tige de destination, et une tige auxiliaire.
Plusieurs disques de diamètres différents, tous empilés sur la tige de départ en ordre décroissant de taille (le plus grand disque en bas et le plus petit en haut).
Règles :

Tu peux déplacer un seul disque à la fois.
Un disque plus grand ne peut jamais être placé sur un disque plus petit.
But :

Déplacer tous les disques de la tige de départ à la tige de destination, en utilisant la tige auxiliaire comme support.
"""


def hanoi_rec(n, start, destination, auxiliary):

    if n == 1:
        print(f"Déplacer le 1 de {start} à {destination}")
        return

    if start & auxiliary == 0:
        print("Le problème est terminé")
        return

    hanoi(n-1, source, auxiliary, target)

    print(f"Déplacer le disque {n} de {source} à {target}")

    hanoi(n - 1, auxiliary, target, source)


hanoi_rec(3, A, B, C)

