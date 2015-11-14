

class Clause:

    def __init__(self, lst):
        self.cl = {}
        for x in lst:
            if int(x) > 0:
                self.cl[x] = True
            else:
                self.cl[x] = False

    