class Relation:
    def __init__(self, base, set_a=None, set_b=None):
        if type(base) is set or (not base and type(base) is dict):
            self.relation = base
            if not base and type(base) is dict:
                self.set_a = {}
                self.set_b = {}
            elif type(self.relation) is set and all(map(lambda elem: type(elem) is tuple and len(elem) == len(next(iter(
                    self.relation))), self.relation)):
                if set_a is None and set_b is None:
                    print("no sets that relation is created over")
                    set_1 = []
                    set_2 = []
                    for tuple_ in self.relation:
                        set_1.append(tuple_[0])
                        set_2.append(tuple_[1])
                    self.set_a = set(set_1)
                    self.set_b = set(set_2)
                elif type(set_a) is set and set_b is None:
                    self.set_b = set_a
                elif type(set_a) is not set:
                    raise TypeError("relation must be created over at least one set")
                else:
                    self.set_a = set_a
                    self.set_b = set_b
            else:
                raise TypeError("relation must be set and all elements must be same length")

            for tuple_ in self.relation:
                if tuple_[0] not in self.set_a or tuple_[1] not in self.set_b:
                    raise TypeError("this relation cannot be made over this set or sets")

            if len(self.relation) is 0:
                self.type = 0
            else:
                self.type = len(next(iter(self.relation)))
        else:
            raise TypeError("type of first argument must be 'set'")

    def __str__(self):
        if self.set_a == self.set_b:
            return "R=" + str(self.relation) + " created over set A=" + str(self.set_a)
        else:
            return "R=" + str(self.relation) + " created over: set A=" + str(self.set_a) + " set B=" + str(self.set_b)


def binary_homogeneous(relation):
    if type(relation) is Relation and relation.type is 2 and relation.set_a == relation.set_b:
        return
    else:
        raise TypeError("argument type must be 'Relation' and argument must be binary homogeneous relation")


def binary(relation):
    if type(relation) is Relation and relation.type is 2:
        return
    else:
        raise TypeError("argument type must be 'Relation' and argument must be binary relation")


def dom(relation):
    """ returns domain of relation """
    if type(relation) is Relation:
        return {tuple_[0] for tuple_ in relation.relation}
    else:
        raise TypeError("argument type must be 'Relation'")


def ran(relation):
    """ returns range of relation """
    if type(relation) is Relation:
        return {tuple_[-1] for tuple_ in relation.relation}
    else:
        raise TypeError("argument type must be 'Relation'")


def reflexive(relation):
    """ checks if relation is reflexive (for all x in X, xRx) """
    binary_homogeneous(relation)
    for element_a in relation.set_a:
        if (element_a, element_a) not in relation.relation:
            return False
    return True


def irreflexive(relation):
    """ checks if relation is irreflexive (for no x in X, xRx) """
    binary_homogeneous(relation)
    for element_a in relation.set_a:
        if (element_a, element_a) in relation.relation:
            return False
    return True


def coreflexive(relation):
    """ checks if relation is coreflexive (for all x and y in X, if xRy then x = y) """
    binary_homogeneous(relation.relation)
    for element_a in relation.set_a:
        for element_b in relation.set_b:
            if (element_a, element_b) in relation.relation and element_a != element_b:
                return False
    return True


def quasireflexive(relation):
    """ checks if relation is quasi-reflexive (for all x and y in X, if xRy then xRx and yRy) """
    binary_homogeneous(relation)
    for element_a in relation.set_a:
        if (element_a, element_a) not in relation.relation:
            return False
    for element_b in relation.set_b:
        if (element_b, element_b) not in relation.relation:
            return False
    return True


def symmetric(relation):
    """ checks if relation is symmetric (for all x and y in X, if xRy then yRx) """
    binary_homogeneous(relation)
    for element_a in relation.set_a:
        for element_b in relation.set_b:
            if (element_a, element_b) in relation and (element_b, element_a) not in relation.relation:
                return False
    return True


def antisymmetric(relation):
    """ checks if relation is antisymmetric (for all x and y in X, if xRy and yRx then x = y) """
    binary_homogeneous(relation)
    for element_a in relation.set_a:
        for element_b in relation.set_b:
            if (element_a, element_b) in relation and (element_b, element_a) in relation.relation and \
                    element_a != element_b:
                return False
    return True


def asymmetric(relation):
    """ checks if relation is asymmetric (for all x and y in X, if xRy then not yRx) """
    binary_homogeneous(relation)
    for element_a in relation.set_a:
        for element_b in relation.set_b:
            if (element_a, element_b) in relation and (element_b, element_a) in relation.relation:
                return False
    return True


def transitive(relation):
    """ checks if relation is transitive (for all x and y and z in X, if xRy and yRz then xRz) """
    binary_homogeneous(relation)
    for tuple_a in relation.relation:
        for tuple_b in relation.relation:
            if tuple_a[1] == tuple_b[0] and (tuple_a[0], tuple_b[1]) not in relation.relation:
                return False
    return True


def connex(relation):
    """ checks if relation is connex (for all x and y in X, xRy or yRx) """
    binary_homogeneous(relation)
    for element_a in relation.set_a:
        for element_b in relation.set_b:
            if (element_a, element_b) not in relation.relation and (element_b, element_a) not in relation.relation:
                return False
    return True


def trichotomous(relation):
    """ checks if relation is trichotomous (for all x and y in X, exactly one of xRy, yRx or x = y holds) """
    binary_homogeneous(relation)
    for element_a in relation.set_a:
        for element_b in relation.set_b:
            if ((element_a, element_b) not in relation.relation and (element_b, element_a) not in relation.relation) \
                    and element_a != element_b:
                return False
    return True


def right_euclidean(relation):
    """ checks if relation is right Euclidean (for all x, y and z in X, if xRy and xRz then yRz) """
    binary_homogeneous(relation)
    for tuple_a in relation.relation:
        for tuple_b in relation.relation:
            if tuple_a[0] == tuple_b[0] and (tuple_a[1], tuple_b[1]) not in relation.relation:
                return False
    return True


def left_euclidean(relation):
    """ checks if relation is left Euclidean (for all x, y and z in X, if yRx and zRx then yRz) """
    binary_homogeneous(relation)
    for tuple_a in relation.relation:
        for tuple_b in relation.relation:
            if tuple_a[1] == tuple_b[1] and (tuple_a[0], tuple_b[0]) not in relation.relation:
                return False
    return True


def serial(relation):
    """ checks if relation is serial (for all x in X, there exists y in X such that xRy) """
    binary_homogeneous(relation)
    set_a = list(relation.set_a)
    for tuple_a in relation.relation:
        set_a.remove(tuple_a[0])
    if len(set_a) is 0:
        return True
    else:
        return False


def set_like(relation):
    """ checks if relation is set-like (for all x in X, the class of all y such that yRx is a set) """
    binary_homogeneous(relation)
    set_b = list(relation.set_b)
    for tuple_ in relation.relation:
        set_b.remove(tuple_[1])
        if type(tuple_[0]) is not set:
            return False
    if len(set_b) is 0:
        return True
    else:
        return False


def tournament(relation):
    """ checks if relation is tournament (is irreflexive and antisymmetric) """
    return irreflexive(relation) and antisymmetric(relation)


def dependency(relation):
    """ checks if relation is an dependency relation (is reflexive and symmetric) """
    return reflexive(relation) and symmetric(relation)


def preorder(relation):
    """ checks if relation is preorder (is reflexive and transitive) """
    return reflexive(relation) and transitive(relation)


def strict_preorder(relation):
    """ checks if relation is strict preorder (is irreflexive and transitive) """
    return irreflexive(relation) and transitive(relation)


def total_preorder(relation):
    return preorder(relation)


def partial_order(relation):
    """ checks if relation is partial order (is reflexive and antisymmetric and transitive) """
    return reflexive(relation) and antisymmetric(relation) and transitive(relation)


def strict_partial_order(relation):
    """ checks if relation is strict partial order (is reflexive and antisymmetric and transitive) """
    return reflexive(relation) and antisymmetric(relation) and transitive(relation)


def strict_weak_order(relation):
    """ checks if relation is strict weak order (is irreflexive and antisymmetric and transitive) """
    return irreflexive(relation) and antisymmetric(relation) and transitive(relation)


def total_order(relation):
    return partial_order(relation)


def partial_equivalence(relation):
    """ checks if relation is partial equivalence relation (is symmetric and transitive) """
    return symmetric(relation) and transitive(relation)


def equivalence(relation):
    """ checks if relation is equivalence relation (is reflexive and symmetric and transitive) """
    return reflexive(relation) and symmetric(relation) and transitive(relation)


def union(relation_r, relation_s):
    """ return union of two relations """
    binary(relation_r)
    binary(relation_s)
    new_relation = list(relation_r.relation)
    for tuple_s in relation_s.relation:
        if tuple_s not in new_relation:
            new_relation.append(tuple_s)
    return Relation(set(new_relation), set(list(relation_r.set_a) + list(relation_s.set_a)),
                    set(list(relation_r.set_b) + list(relation_s.set_b)))


def intersection(relation_r, relation_s):
    """ return intersection of two relations """
    binary(relation_r)
    binary(relation_s)
    new_relation = []
    for tuple_a in relation_r.relation:
        if tuple_a in relation_s.relation:
            new_relation.append(tuple_a)
    return Relation(set(new_relation), set(list(relation_r.set_a) + list(relation_s.set_a)),
                    set(list(relation_r.set_b) + list(relation_s.set_b)))


def composition(relation_r, relation_s):
    """ returns composition of two relations"""
    binary(relation_r)
    binary(relation_s)
    new_relation = []
    for tuple_r in relation_r.relation:
        for tuple_s in relation_s.relation:
            if tuple_r[1] == tuple_s[0]:
                new_relation.append((tuple_r[0], tuple_s[1]))
    return Relation(set(new_relation), relation_r.set_a, relation_s.set_b)


def complement(relation):
    """ returns complementary relation to argument"""
    binary(relation)
    new_relation = []
    for a in relation.set_a:
        for b in relation.set_b:
            new_relation.append((a, b))

    for tuple_ in new_relation:
        if tuple_ in relation.relation:
            new_relation.remove(tuple_)
    return Relation(set(new_relation), relation.set_a, relation.set_b)


def converse(relation):
    """ returns converse relation to argument"""
    binary(relation)
    new_relation = []
    for tuple_ in relation.relation:
        new_relation.append((tuple_[1], tuple_[0]))
    return Relation(set(new_relation), relation.set_b, relation.set_a)


def reflexive_closure(relation):
    """ returns reflexive closure to argument """
    binary_homogeneous(relation)
    new_relation = list(relation.relation)
    for a in relation.set_a:
        if (a, a) not in new_relation:
            new_relation.append((a, a))
    return Relation(new_relation, relation.set_a)


def symmetric_closure(relation):
    """ returns symmetric closure to argument """
    binary_homogeneous(relation)
    return union(relation, converse(relation))


def transitive_closure(relation):
    """ returns transitive closure to argument """
    binary_homogeneous(relation)
    if transitive(relation):
        return relation
    else:
        old_relation = None
        while old_relation != relation:
            old_relation = relation
            relation = union(relation, composition(relation, relation))
        return relation


def transitive_reduction(relation):
    """ returns transitive reduction to argument """
    binary_homogeneous(relation)
    base_relation = Relation(relation.relation, relation.set_a)
    old_relation = None
    relation = composition(relation.relation, relation.relation)
    while old_relation != relation:
        old_relation = relation
        relation = union(relation, composition(relation, relation))
    return intersection(base_relation, complement(relation))
