def dom(relation):
    if type(relation) is set and all(map(lambda elem:
                                         type(elem) is tuple and len(elem) == len(next(iter(relation))), relation)):
        return {tuple_[0] for tuple_ in relation}
    else:
        raise TypeError("relation must be set and all elements must be same length")


def ran(relation):
    if type(relation) is set and all(map(lambda elem:
                                         type(elem) is tuple and len(elem) == len(next(iter(relation)))
                                         and len(elem) > 1, relation)):
        return {tuple_[-1] for tuple_ in relation}
    else:
        raise TypeError("relation must be set and all elements must be same length")
