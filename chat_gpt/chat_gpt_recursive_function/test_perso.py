"""
# Factorise un nombre sans récursivité
def fact(number):

    if not isinstance(number, int):
        print("Le paramètre doit être un entier")

    if number < 0:
        print("le paramètre doit être supérieur ou égal à 0")

    result = 1
    while number > 1:
        result *= number
        number -= 1
    return result


print(fact(7))


# Factorise un nombre avec la manière récursive
def fact_rec(value):

    if not isinstance(value, int):
        print("Le paramètre doit être un entier")

    if value < 0:
        print("le paramètre doit être supérieur ou égal à 0")

    if value == 0:
        return 1

    else:
        return value * fact_rec(value - 1)


print(fact_rec(7))


# inverse les lettres d'un mot avec la récursivité
def inverse_rec(word):

    if len(word) in [0, 1]:
        return word

    else:
        return word[-1] + inverse_rec(word[:-1])


print(inverse_rec("augustin"))


def inverse_rec_2(word):

    if len(word) in [0, 1]:
        return word
    else:
        return word[-1] + inverse_rec_2(word[:-1])


print(inverse_rec_2('Augustin'))


def fact_rec_2(number):

    if number == 0:
        return 1

    else:
        return number * fact_rec_2(number - 1)


print(fact_rec_2(4))



# SUITE DE FIBONACCI
def fibonacci_rec(n):

    if n == 0:
        return 0

    elif n == 1:
        return 1

    elif n >= 20:
        print("STOOOOOOOOP")
        return None

    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)


for x in range(30):
    result = fibonacci_rec(n=x)
    if result is not None:
        print(result)

"""


def compteur(n):
    if n > 0:
        compteur(n - 1)
    else:
        print(n)


compteur(4)
