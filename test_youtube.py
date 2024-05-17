longeur_caractere = int(input("Entrez la longueur du mot de passe souhaiter : "))
liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def bruteforce(word, length):
    if length <= longeur_caractere:
        for letter in liste:
            if mdp == word + letter:
                print("Votre mot de passe est " + word + letter)
            else:
                print(word + letter)
                bruteforce(word + letter, length + 1)


print("Entrez votre mot de passe (il dois avoir une longeur de", longeur_caractere, "caracteres)")
mdp = input("\n mdp : ")
bruteforce('', 1)

for letter in liste:
    if mdp == word + letter:

        print("Votre mot de passe est " + word + letter)

    else:
        print(word + letter)
        bruteforce(word + letter, length + 1)



mdp = input("Entrez votre mot de passe : ")
bruteforce('', 1)