def check_binary_relation(relation, set_a, set_b):
    if type(relation) is set and all(map(lambda elem:
                                         type(elem) is tuple and len(elem) == len(next(iter(relation))), relation)):
        if len(next(iter(relation))) is 2:
            if set_a is None and set_b is None:
                print("no sets that relation is created over")
                set_1 = []
                set_2 = []
                for tuple_ in relation:
                    set_1.append(tuple_[0])
                    set_2.append(tuple_[1])
                set_a = set(set_1)
                set_b = set(set_2)
            elif type(set_a) is set and set_b is None:
                set_b = set_a
            elif type(set_a) is not set:
                raise TypeError("relation must be created over at least one set")

            for tuple_ in relation:
                if tuple_[0] not in set_a or tuple_[1] not in set_b:
                    raise TypeError("this relation cannot be made over this set or sets")

            return set_a, set_b
        else:
            raise TypeError("only binary relations have properties")
    else:
        raise TypeError("relation must be set and all elements must be same length")


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
                                         type(elem) is tuple and len(elem) == len(next(iter(relation))), relation)):
        return {tuple_[-1] for tuple_ in relation}
    else:
        raise TypeError("relation must be set and all elements must be same length")


def reflexive(relation, set_a=None, set_b=None):
    """ checks if relation is reflexive (for all x in X, xRx) """
    set_a, set_b = check_binary_relation(relation, set_a, set_b)
    for element_a in set_a:
        if (element_a, element_a) not in relation:
            return False
    return True


def irreflexive(relation, set_a=None, set_b=None):
    """ checks if relation is irreflexive (for no x in X, xRx) """
    set_a, set_b = check_binary_relation(relation, set_a, set_b)
    for element_a in set_a:
        if (element_a, element_a) in relation:
            return False
    return True


def coreflexive(relation, set_a=None, set_b=None):
    """ checks if relation is coreflexive (for all x and y in X, if xRy then x = y) """
    set_a, set_b = check_binary_relation(relation, set_a, set_b)
    for element_a in set_a:
        for element_b in set_b:
            if (element_a, element_b) in relation and element_a != element_b:
                return False
    return True


def quasireflexive(relation, set_a=None, set_b=None):
    """ checks if relation is quasi-reflexive (for all x and y in X, if xRy then xRx and yRy) """
    set_a, set_b = check_binary_relation(relation, set_a, set_b)
    for element_a in set_a:
        if (element_a, element_a) not in relation:
            return False
    for element_b in set_b:
        if (element_b, element_b) not in relation:
            return False
    return True


def symmetric(relation, set_a=None, set_b=None):
    """ checks if relation is symmetric (for all x and y in X, if xRy then yRx) """
    set_a, set_b = check_binary_relation(relation, set_a, set_b)
    for element_a in set_a:
        for element_b in set_b:
            if (element_a, element_b) in relation and (element_b, element_a) not in relation:
                return False
    return True


def antisymmetric(relation, set_a=None, set_b=None):
    """ checks if relation is antisymmetric (for all x and y in X, if xRy and yRx then x = y) """
    set_a, set_b = check_binary_relation(relation, set_a, set_b)
    for element_a in set_a:
        for element_b in set_b:
            if (element_a, element_b) in relation and (element_b, element_a) in relation and \
                    element_a != element_b:
                return False
    return True


def asymmetric(relation, set_a=None, set_b=None):
    """ checks if relation is asymmetric (for all x and y in X, if xRy then not yRx) """
    set_a, set_b = check_binary_relation(relation, set_a, set_b)
    for element_a in set_a:
        for element_b in set_b:
            if (element_a, element_b) in relation and (element_b, element_a) in relation:
                return False
    return True


def transitive(relation, set_a=None, set_b=None):
    """ checks if relation is transitive (for all x and y and z in X, if xRy and yRz then xRz) """
    set_a, set_b = check_binary_relation(relation, set_a, set_b)
    for tuple_a in relation:
        for tuple_b in relation:
            if tuple_a[1] == tuple_b[0] and (tuple_a[0], tuple_b[1]) not in relation:
                return False
    return True


def connex(relation, set_a=None, set_b=None):
    """ checks if relation is connex (for all x and y in X, xRy or yRx) """
    set_a, set_b = check_binary_relation(relation, set_a, set_b)
    for element_a in set_a:
        for element_b in set_b:
            if (element_a, element_b) not in relation and (element_b, element_a) not in relation:
                return False
    return True


def trichotomous(relation, set_a=None, set_b=None):
    """ checks if relation is trichotomous (for all x and y in X, exactly one of xRy, yRx or x = y holds) """
    set_a, set_b = check_binary_relation(relation, set_a, set_b)
    for element_a in set_a:
        for element_b in set_b:
            if ((element_a, element_b) not in relation and (element_b, element_a) not in relation) and \
                    element_a != element_b:
                return False
    return True


def right_euclidean(relation, set_a=None, set_b=None):
    """ checks if relation is right Euclidean (for all x, y and z in X, if xRy and xRz then yRz) """
    check_binary_relation(relation, set_a, set_b)
    for tuple_a in relation:
        for tuple_b in relation:
            if tuple_a[0] == tuple_b[0] and (tuple_a[1], tuple_b[1]) not in relation:
                return False
    return True


def left_euclidean(relation, set_a=None, set_b=None):
    """ checks if relation is left Euclidean (for all x, y and z in X, if yRx and zRx then yRz) """
    check_binary_relation(relation, set_a, set_b)
    for tuple_a in relation:
        for tuple_b in relation:
            if tuple_a[1] == tuple_b[1] and (tuple_a[0], tuple_b[0]) not in relation:
                return False
    return True


def serial(relation, set_a=None, set_b=None):
    """ checks if relation is serial (for all x in X, there exists y in X such that xRy) """
    set_a, set_b = check_binary_relation(relation, set_a, set_b)
    set_a = list(set_a)
    for tuple_a in relation:
        set_a.remove(tuple_a[0])
    if len(set_a) is 0:
        return True
    else:
        return False


def set_like(relation, set_a=None, set_b=None):
    """ checks if relation is set-like (for all x in X, the class of all y such that yRx is a set) """
    set_a, set_b = check_binary_relation(relation, set_a, set_b)
    set_b = list(set_b)
    for tuple_ in relation:
        set_b.remove(tuple_[1])
        if type(tuple_[0]) is not set:
            return False
    if len(set_b) is 0:
        return True
    else:
        return False


def tournament(relation, set_a, set_b):
    """ checks if relation is tournament (is irreflexive and antisymmetric) """
    return irreflexive(relation, set_a, set_b) and antisymmetric(relation, set_a, set_b)


def dependency(relation, set_a, set_b):
    """ checks if relation is an dependency relation (is reflexive and symmetric) """
    return reflexive(relation, set_a, set_b) and symmetric(relation, set_a, set_b)


def preorder(relation, set_a, set_b):
    """ checks if relation is preorder (is reflexive and transitive) """
    return reflexive(relation, set_a, set_b) and transitive(relation, set_a, set_b)


def strict_preorder(relation, set_a, set_b):
    """ checks if relation is strict preorder (is irreflexive and transitive) """
    return irreflexive(relation, set_a, set_b) and transitive(relation, set_a, set_b)


def total_preorder(relation, set_a, set_b):
    return preorder(relation, set_a, set_b)


def partial_order(relation, set_a, set_b):
    """ checks if relation is partial order (is reflexive and antisymmetric and transitive) """
    return reflexive(relation, set_a, set_b) and antisymmetric(relation, set_a, set_b) and transitive(relation,
                                                                                                      set_a, set_b)


def strict_partial_order(relation, set_a, set_b):
    """ checks if relation is strict partial order (is reflexive and antisymmetric and transitive) """
    return reflexive(relation, set_a, set_b) and antisymmetric(relation, set_a, set_b) and transitive(relation,
                                                                                                      set_a, set_b)


def strict_weak_order(relation, set_a, set_b):
    """ checks if relation is strict weak order (is irreflexive and antisymmetric and transitive) """
    return irreflexive(relation, set_a, set_b) and antisymmetric(relation, set_a, set_b) and transitive(relation, set_a,
                                                                                                        set_b)


def total_order(relation, set_a, set_b):
    return partial_order(relation, set_a, set_b)


def partial_equivalence(relation, set_a, set_b):
    """ checks if relation is partial equivalence relation (is symmetric and transitive) """
    return symmetric(relation, set_a, set_b) and transitive(relation, set_a, set_b)


def equivalence(relation, set_a, set_b):
    """ checks if relation is equivalence relation (is reflexive and symmetric and transitive) """
    return reflexive(relation, set_a, set_b) and symmetric(relation, set_a, set_b) and transitive(relation, set_a, set_b)