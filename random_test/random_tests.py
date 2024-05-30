def carre(x):
    return x * x
# print(carre(4))

carre_lambda = lambda x: x * x
# print(carre_lambda(3))


def addition(n):
    return n + n


numbers = [1, 2, 3, 4, 5]
all_add = map(addition, numbers)

all_add = map(lambda n: n + n, numbers)

# print(list(all_add))

random_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]

test = random_liste[3::2]
# print(test)

liste = [1, 2, 3, 4, 5]
liste_1 = []
liste_2 = []

for element in liste:
    liste_1.append(element)
    liste_2.append(liste_1[:])

print(liste_2)

