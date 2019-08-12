
def convert(items):
    for index, item in enumerate(items):
        if item in ("^"): # you can add more 'and' substitute
            items[index] = "and"
        if item in ("imp", "->", "=>", ">"):
            items[index] = "implies"
        if item in ("<->", "<=>", "<>", "iff"):
            items[index] = "equals"
        if item in ("\/"): 
            items[index] = "or"
        if item in ("!", "~", "¬"):
            items[index] = "not"
    return items
