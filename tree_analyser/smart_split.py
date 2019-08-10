
chop = lambda text, c: [text[:text.find(c)], c, text[text.find(c)+1:]]


def partial_split(form, char):
    if form.find(char) == -1 or len(form) == 1:
        return form
    splitted = filter(lambda elem: elem, chop(form, char))
    return list(map(lambda elem: partial_split(elem, char), splitted))


def flatten(array):
    for item in array:
        if type(item) in (list, tuple):
            yield from flatten(item)
        else:
            yield item 


def smart_split(form, splitted_by=("(", ")", " "), ignore=(" ",)):
    form = [form]
    for char in splitted_by:
        form= [partial_split(text, char) for text in form]
        form = list(flatten(form))
    return list(filter(lambda elem: elem not in ignore, form))

