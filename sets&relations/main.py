from vienn import vienn
from relations import is_reflexive

print(is_reflexive({("a", "a")}))
print(is_reflexive({("a", "b"), ("b", "c"), ("a", "c")}, {"a", "b"}, {"b", "c", "d"}))
print(is_reflexive({("a", "b"), ("b", "c"), ("a", "c")}, {"a", "b", "c"}))
print(is_reflexive({("a", "b"), ("b", "c"), ("a", "c")}, {"a", "b"}, {"b", "c", "t"}))

"""
A = {1, 2, 3, 4, 5, 6, 'e', 'f', '*', '&',}
B = {'a', 'b', 'c', 'd', 'e', 'f', 1, 2, '*', '&'}
C = {'!', '@', '#', '$', '%', 'a', 'b', 3, '*', '&'}
vienn(A, B, C)
#  vienn(A, B)
"""