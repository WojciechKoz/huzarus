from vienn import vienn
from relations import is_quasireflexive

print(is_quasireflexive({("a", "a")}))
print(is_quasireflexive({("a", "b", "a"), ("b", "t", "b"), ("a", "a", "a")}))

"""
A = {1, 2, 3, 4, 5, 6, 'e', 'f', '*', '&',}
B = {'a', 'b', 'c', 'd', 'e', 'f', 1, 2, '*', '&'}
C = {'!', '@', '#', '$', '%', 'a', 'b', 3, '*', '&'}
vienn(A, B, C)
#  vienn(A, B)
"""