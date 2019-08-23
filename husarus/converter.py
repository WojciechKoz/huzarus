def convert(items):
    for index, item in enumerate(items):
        if item == "^":  # you can add more 'and' substitute
            items[index] = "and"
        if item in ("imp", "->", "=>", ">"):
            items[index] = "implies"
        if item in ("<->", "<=>", "<>", "iff"):
            items[index] = "equals"
        if item in ("/", "v", "\/"):
            items[index] = "or"
        if item in ("!", "~", "¬"):
            items[index] = "not"
    return items


def convert_sets_to_bool(items):
    for index, item in enumerate(items):
        if item in ('inter', '^', 'intersection'):
            items[index] = 'and'
        if item in ('sum', 'SUM', 'U'):
            items[index] = 'or'
        if item in ('diff', '\\', '-', 'difference'):
            items[index] = 'and'
            items.insert(index+1, 'not')
    return items
