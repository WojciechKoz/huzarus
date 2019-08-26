from vienn import vienn
'''
A = {1, 2, 3, 4, 5, 6, 'e', 'f', '*', '&',}
B = {'a', 'b', 'c', 'd', 'e', 'f', 1, 2, '*', '&'}
C = {'!', '@', '#', '$', '%', 'a', 'b', 3, '*', '&'}
vienn(A, B, C)
input()
#  vienn(A, B)
'''
form = "not(A inter B) - C"
print(form)
vienn(form)
