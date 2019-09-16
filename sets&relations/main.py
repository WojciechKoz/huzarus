from vienn import vienn
from relations import *
from relation_graph import render_relation

R = Relation({("a", "b"), ("b", "c")})
render_relation(R)

"""
A = {1, 2, 3, 4, 5, 6, 'e', 'f', '*', '&',}
B = {'a', 'b', 'c', 'd', 'e', 'f', 1, 2, '*', '&'}
C = {'!', '@', '#', '$', '%', 'a', 'b', 3, '*', '&'}
vienn(A, B, C)
#  vienn(A, B)
"""
