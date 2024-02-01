from itertools import permutations

words = ["genderless", "singular", "third person"]
combos = list(permutations(words))
for a, b, c in combos:
    print(f"{a} {b} {c} pronoun")
