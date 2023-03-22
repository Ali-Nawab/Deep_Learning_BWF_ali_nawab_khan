# Union of two sets

set1 = {1, 2, 3}
set2 = {2, 3, 4}
union_set = set1.union(set2)
# Or, alternatively:
# union_set = set1 | set2
print(union_set)  # Output: {1, 2, 3, 4}


# Intersection of two sets

set1 = {1, 2, 3}
set2 = {2, 3, 4}
intersection_set = set1.intersection(set2)
# Or, alternatively:
# intersection_set = set1 & set2
print(intersection_set)  # Output: {2, 3}


# Symmetric difference of two sets

set1 = {1, 2, 3}
set2 = {2, 3, 4}
symmetric_difference_set = set1.symmetric_difference(set2)
# Or, alternatively:
# symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set)  # Output: {1, 4}

