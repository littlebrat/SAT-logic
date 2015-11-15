from src.structure.clause import Clause


class KnowledgeBase:
    """
    KB that represents a SAT problem with a set of clauses with restrictions.
    """

class Sentence:

    def __init__(self):
        self.variables = []
        self.clauses = []

    @staticmethod
    def from_file(path):
        sentence = Sentence()
        # this method loads a file into a object of this class.
        with open(path) as file:
            for line in file:
                # for each line in the file verify if the structure of the line is correct.
                words = line.split()
                if words[0] is 'c':
                    # comments line should be ignored
                    continue
                if words[0] == 'p' and words[1] == 'cnf' and len(words) == 4:
                    # read format
                    sentence.variables = range(1, int(words[2])+1)
                    clauses = int(words[3])
                else:
                    aux = words[:-1]
                    cl = Clause(aux)
                    sentence.clauses.append(cl)
        return sentence

    def variables(self):
        return self.variables

    def get_valid_clauses(self, attribution, best):
        r = 0

        return r

    def __repr__(self):
        r = ''
        for c in self.clauses:
            r += str(c) + '\n'
        return r

sent = Sentence.from_file('../test_files/pikachu.txt')
print(sent)
