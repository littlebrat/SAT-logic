from src.structure.clause import Clause


class KnowledgeBase:
    """
    KB that represents a SAT problem with a set of clauses with restrictions.
    """

    def __init__(self):
        self.variables = []
        self.clauses = []

    @staticmethod
    def from_file(self, path):
        kb = KnowledgeBase()
        # this method loads a file into a object of this class.
        with open(path) as file:
            for line in file:
                # for each line in the file verify if the structure of the line is correct.
                words = line.split()
                if words[0] is 'c':
                    # comments line should be ignored
                    continue
                if words[0] is 'p' and words[1] is 'cnf' and len(words) == 4:
                    # read format
                    self.variables = range(1, int(words[2])+1)
                    clauses = int(words[3])
                else:
                    aux = words[:-1]
                    cl = Clause(aux)
                    self.clauses.append(cl)
        return kb

    def get_valid_clauses(self, attribution):
        r = 0

        return r


