"""
Problème : Somme des sous-ensembles
Objectif : Déterminer si un ensemble donné d'entiers peut être partitionné en deux sous-ensembles tels que la somme des nombres dans chaque sous-ensemble soit la même.

Données : Une liste d'entiers positifs.

Exemple :

Soit la liste nums = [1, 5, 11, 5].

La liste peut être divisée en les sous-ensembles [1, 5, 5] et [11], où la somme des deux sous-ensembles est 11.
Défi : Écris une fonction récursive pour déterminer si une telle partition est possible pour une liste donnée. Si c'est possible, ta fonction devrait retourner True, sinon False.
"""
"""
// SOLUTION //

def canPartition(nums):
    total_sum = sum(nums)
    # Si la somme totale est impaire, une partition en deux sous-ensembles égaux n'est pas possible
    if total_sum % 2 != 0:
        return False
    return canPartitionHelper(nums, 0, total_sum // 2)

def canPartitionHelper(nums, index, sum_remaining):
    # Cas de base: Si la somme restante est 0, nous avons trouvé une partition valide
    if sum_remaining == 0:
        return True
    # Si nous dépassons la fin de la liste ou si la somme restante est négative, retourne False
    if index >= len(nums) or sum_remaining < 0:
        return False
    # Inclure l'élément actuel dans le sous-ensemble ou ne pas l'inclure
    return canPartitionHelper(nums, index + 1, sum_remaining - nums[index]) or canPartitionHelper(nums, index + 1, sum_remaining)

# Test de la fonction
print(canPartition([1, 5, 11, 5]))  # True
print(canPartition([1, 2, 3, 5]))   # False
"""

