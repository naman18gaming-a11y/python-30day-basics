#All Permutations of a String in Lexicographic Order without Recursion
def get_permutations(s):
    if len(s) == 1:
        return [s]
    permutations = []
    for i, char in enumerate(s):
        for perm in get_permutations(s[:i] + s[i+1:]):
            permutations.append(char + perm)
    return sorted(permutations)