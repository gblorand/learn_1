from collections import defaultdict


def sum_int(a: int, b: int) ->  int:
    return a + b


""" the method count_appearances gets a list of lists og int as input and outputs for each int in the output
the number of lines it appeared in the input. If an int appeared more than once in a list we count it as one appearance """
def count_appearances(list_of_lists: list[list[int]]) -> dict[int, int]:
    # we use a defaultdict to count the appearances of each int in the input that return 0
    # if the key is not in the dictionary
    appearances = defaultdict(int)
    for list in list_of_lists:
        for num in set(list):
           appearances[num] += 1
    return appearances