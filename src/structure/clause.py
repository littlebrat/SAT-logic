

class Clause:
    """
    It is assumed that the clause is in cnf form. So here we have disjuntion of literals.
    A clause is a dictionary with the positive literal as key and a bool as
    its proper boolean value.
    """

    def __init__(self, lst):
        self.cl = {}
        for x in lst:
            num  = int(x)
            if int(x) > 0:
                self.cl[abs(x)] = True
            else:
                self.cl[abs(x)] = False

    def isValid(self,literal,bool):
        # This method checks if the boolean attribution for the input literal
        # argument satisfies this clause object.
        if self.cl[literal] == bool:
            return True
        else:
            return False

    def __repr__(self):
        # Method to print the object in string format in the form: [x1: bool; ...; xn: bool].
        r = ''
        for literal in self.cl.keys():
            r += str(literal) + ': ' + str(self.cl[literal]) + '; '
        return r[:-2]

