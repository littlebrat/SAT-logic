from random import getrandbits


class Solution:

    def __init__(self, num_vars):
        # The object is initialized as a dictionary of literals-booleans
        self.sl = {}
        for v in range(1, num_vars + 1):
            self.sl[v] = None

    def restart(self):
        # Do a random restart of the variables in solution.
        for var in self.sl.keys():
            self.sl[var] = not getrandbits(1)

    def literal(self, var):
        # Get the boolean value associated with literal 'var'.
        return self.sl[var]

    def toggle(self, var):
        # Swap the boolean value of the literal
        self.sl[var] = not self.sl.get(var)

    def set(self, var, bl):
        # Set the variable 'var' to the boolean value of 'bl'.
        self.sl[var] = bl

    def output(self):
        # YOUR CODE HERE FAGGOT!!!
        return

    def deep_copy(self):
        return self.sl.copy()

    def __repr__(self):
        # Method to print the object in string format in the form: [x1: bool; ...; xn: bool].
        r = ''
        for literal in self.sl.keys():
            r += str(literal) + ': ' + str(self.sl[literal]) + '; '
        return r[:-2]
