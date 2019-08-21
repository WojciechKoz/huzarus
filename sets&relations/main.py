from vienn import vienn
from relations import ran

print(ran({("a", "b"), ("a", "c")}))
"""
A = {1, 2, 3, 4, 5, 6, 'e', 'f', '*', '&',}
B = {'a', 'b', 'c', 'd', 'e', 'f', 1, 2, '*', '&'}
C = {'!', '@', '#', '$', '%', 'a', 'b', 3, '*', '&'}
vienn(A, B, C)
#  vienn(A, B)
"""
