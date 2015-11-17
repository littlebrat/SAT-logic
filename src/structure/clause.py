

class Clause:
    """
    It is assumed that the clause is in cnf form. So here we have disjuntion of literals.
    A clause is a dictionary with the positive literal as key and a bool as
    its proper boolean value.
    """

    def __init__(self, lst):
        self.cl = {}
        for x in lst:
            num = int(x)
            if num > 0:
                self.cl[abs(num)] = True
            else:
                self.cl[abs(num)] = False

    def is_clause_satisfied(self, solution):
        for l in self.cl.keys():
            if self.cl[l] == solution.literal(l):
                return True
        return False

    def get_unit_symbol(self):
        if len(self.cl.keys()) == 1:
            k = list(self.cl.keys())[0]
            return k, self.cl[k]
        else:
            return None, None

    def simplify(self, literal):
        # If literal appear on this clause, remove it from clause.
        if literal in self.cl.keys():
            del self.cl[literal]

    def get_literals(self):
        return list(self.cl.keys())

    def exists(self, literal, bl):
        if literal in self.cl.keys() and self.cl[literal] == bl:
            return True
        else:
            return False

    def has_literal(self, v):
        if v in self.cl.keys():
            return True
        else:
            return False

    @staticmethod
    def copy(other):
        # Method for deep-copying the clause 'other'.
        ls = []
        for literal in other.keys():
            if other.cl[literal]:
                ls.append(str(literal))
            else:
                ls.append(str(-literal))
        cp = Clause(ls)
        return cp

    def __repr__(self):
        # Method to print the object in string format in the form: [x1: bool; ...; xn: bool].
        r = ''
        for literal in self.cl.keys():
            r += str(literal) + ': ' + str(self.cl[literal]) + '; '
        return r[:-2]
