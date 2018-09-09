from itertools import groupby
from itertools import permutations
from collections import Counter


def group_by(data, group_col, value_col, agg_function):
    """ Group by
        Inputs:
          - data: list of tuples e.g.: [('A', 2, 3), ('A', 3, 4)]
          - group_col: int, column to group by e.g.: 0
          - value_col: int, column to aggregate e.g: 1
          - agg_function: agg function, so e.g. : sum
            it is applied to list of values in value_col
            for the group
            e.g. sum([1, 2, 3])
        Output:
          - out: dict group_name -> value {'A': 5}
    """
    data = sorted(data, key=lambda x: x[group_col])

    out = {}
    for key, values in groupby(data, lambda x: x[group_col]):
        out[key] = agg_function(v[value_col] for v in values)
    return out


def num_bad_permutations(n):
    """
    Number of permutations of length n
    where each element is not on its place
    Inputs:
      - n: int, length of permutation
    Output:
      - num_perm: int, number of such permutations
    """
    num_perm = 0

    for perm in list(permutations(range(n))):
        for i in range(n):
            if perm[i] == i:
                break
        else:
            num_perm += 1

    return num_perm


def count_ngrams(text, n):
    """
        Counter of symbol ngrams
        Inputs:
          - text: str, some text
          - n: int, length of symbol ngram
        Output:
          - ngrams: Counter, ngram-> number of times
                                     it was in text
        """
    ngrams = Counter()

    for word in text.split(' '):
        word = word.strip()
        for i in range(len(word) - n + 1):
            ngrams[word[i:i+n]] += 1

    return ngrams
