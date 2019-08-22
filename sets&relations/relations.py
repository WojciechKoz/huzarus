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
        raise TypeError("relation must be set and all elements must be same length")


def is_irreflexive(relation):
    """ checks if relations is irreflexive (for no x in X, xRx) """
    if type(relation) is set and all(map(lambda elem:
                                         type(elem) is tuple and len(elem) == len(next(iter(relation))), relation)):
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
        raise TypeError("relation must be set and all elements must be same length")


def is_coreflexive(relation):
    """ checks if relations is coreflexive (for all x and y in X, if xRy then x = y) """
    if type(relation) is set and all(map(lambda elem:
                                         type(elem) is tuple and len(elem) == len(next(iter(relation))), relation)):
        for tuple_ in relation:
            if tuple_[0] != tuple_[-1]:
                return False
        return True
    else:
        raise TypeError("relation must be set and all elements must be same length")


def is_quasireflexive(relation):
    """ checks if relations is quasi-reflexive (for all x and y in X, if xRy then xRx and yRy) """
    if type(relation) is set and all(map(lambda elem:
                                         type(elem) is tuple and len(elem) == len(next(iter(relation))), relation)):
        elements = [list() for x in range(len(next(iter(relation))))]
        i = 0
        for tuple_ in relation:  # creating lists of elements to check
            for element in tuple_:
                if element not in elements[i]:
                    elements[i].append(element)
                i += 1
            i = 0

        for i in range(len(elements)):  # removing doubled lists of elements
            if elements[i] in elements[:i]:
                elements.pop(i)

        for list_ in elements:  # property checking
            for tuple_ in relation:
                if tuple_[0] == tuple_[-1] and tuple_[0] in list_:
                    list_.remove(tuple_[0])
            if len(list_) is not 0:
                return False
        return True
    else:
        raise TypeError("relation must be set and all elements must be same length")