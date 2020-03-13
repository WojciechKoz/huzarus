# huzarus
## Description

## Usage examples
### Venn diagrams

venn takes string or sequence of sets (up to 3)
It draws using matplotlib a visual representation of given sets
```
from venn import venn

venn('(A sum B) diff (C and D)')
```

![venn example photo no1](https://github.com/WojciechKoz/huzarus/blob/master/imgs/venn1.png)

```
from venn import venn

A = {1, 2, 3, 4, 5, 6, 'e', 'f', '*', '&',}
B = {'a', 'b', 'c', 'd', 'e', 'f', 1, 2, '*', '&'}
C = {'!', '@', '#', '$', '%', 'a', 'b', 3, '*', '&'}
venn(A, B, C)
```
![venn example photo no2](https://github.com/WojciechKoz/huzarus/blob/master/imgs/venn2.png)

### Truth table
truth_table takes string (form) and returns tuple of pandas.DataFrame (represents truth table for given form) and 
set of variables used in form. Form is a string representation of some logic formula e.g. "a and b => c"

```
>>> truth_table('a and b => c')[0] # index 0 - shows only truth table
       a      b      c  a and b  a and b implies c
0  False  False  False    False               True
1  False  False   True    False               True
2  False   True  False    False               True
3  False   True   True    False               True
4   True  False  False    False               True
5   True  False   True    False               True
6   True   True  False     True              False
7   True   True   True     True               True
```
As we know from school, implication is false only when first argument is true and second is false. 
We can easly check if our answer is correct however we can pass to that function even more complicated arguments.
