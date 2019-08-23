def dom(relation):
    """ returns domain of relation """
    if type(relation) is set and all(map(lambda elem:
                                         type(elem) is tuple and len(elem) == len(next(iter(relation))), relation)):
        return {tuple_[0] for tuple_ in relation}
    else:
        raise TypeError("relation must be set and all elements must be same length")


def ran(relation):
    """ returns range of relation """
    if type(relation) is set and all(map(lambda elem:
                                         type(elem) is tuple and len(elem) == len(next(iter(relation)))
                                         and len(elem) > 1, relation)):
        return {tuple_[-1] for tuple_ in relation}
    else:
        raise TypeError("relation must be set and all elements must be same length")


def is_reflexive(relation):
    """ checks if relations is reflexive (for all x in X, xRx) """
    if type(relation) is set and all(map(lambda elem:
                                         type(elem) is tuple and len(elem) == len(next(iter(relation))), relation)):
        if len(next(iter(relation))) is 2:
            elements = []
            for tuple_ in relation:
                for element_ in tuple_:
                    if element_ not in elements:
                        elements.append(element_)

            for tuple_ in relation:
                if tuple_[0] == tuple_[-1] and tuple_[0] in elements:
                    elements.remove(tuple_[0])
            if len(elements) is 0:
                return True
            else:
                return False
        else:
            raise TypeError("only binary relations have properties")
    else:
        raise TypeError("relation must be set and all elements must be same length")


def is_irreflexive(relation):
    """ checks if relations is irreflexive (for no x in X, xRx) """
    if type(relation) is set and all(map(lambda elem:
                                         type(elem) is tuple and len(elem) == len(next(iter(relation))), relation)):
        if len(next(iter(relation))) is 2:
            elements = []
            for tuple_ in relation:
                for element_ in tuple_:
                    if element_ not in elements:
                        elements.append(element_)

            for tuple_ in relation:
                if tuple_[0] == tuple_[-1] and tuple_[0] in elements:
                    return False
            return True
        else:
            raise TypeError("only binary relations have properties")
    else:
        raise TypeError("relation must be set and all elements must be same length")


def is_coreflexive(relation):
    """ checks if relations is coreflexive (for all x and y in X, if xRy then x = y) """
    if type(relation) is set and all(map(lambda elem:
                                         type(elem) is tuple and len(elem) == len(next(iter(relation))), relation)):
        if len(next(iter(relation))) is 2:
            for tuple_ in relation:
                if tuple_[0] != tuple_[-1]:
                    return False
            return True
        else:
            raise TypeError("only binary relations have properties")
    else:
        raise TypeError("relation must be set and all elements must be same length")


def is_quasireflexive(relation):
    """ checks if relations is quasi-reflexive (for all x and y in X, if xRy then xRx and yRy) """
    if type(relation) is set and all(map(lambda elem:
                                         type(elem) is tuple and len(elem) == len(next(iter(relation))), relation)):
        if len(next(iter(relation))) is 2:
            elements_a = []
            elements_b = []
            for tuple_ in relation:
                if tuple_[0] not in elements_a:
                    elements_a.append(tuple_[0])
                if tuple_[1] not in elements_b:
                    elements_b.append(tuple_[1])

            for tuple_ in relation:
                if tuple_[0] == tuple_[1]:
                    if tuple_[0] in elements_a:
                        elements_a.remove(tuple_[0])
                    if tuple_[1] in elements_b:
                        elements_b.remove(tuple_[1])
            return len(elements_a) is 0 and len(elements_b) is 0
        else:
            raise TypeError("only binary relations have properties")
    else:
        raise TypeError("relation must be set and all elements must be same length")