from src.structure.clause import Clause


class Sentence:
    """
    Sentence that represents a SAT problem with a set of clauses with restrictions.
    """

    def __init__(self):
        self.clauses = []
        self.variables = 0

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
                    sentence.variables = int(words[2])
                else:
                    aux = words[:-1]
                    cl = Clause(aux)
                    sentence.clauses.append(cl)
        return sentence

    def get_validated_clauses(self, solution):
        r = 0
        for c in self.clauses:
            if c.is_clause_satisfied(solution):
                r += 1
        return r

    def is_satisfied(self, solution):
        if self.get_validated_clauses(solution) == len(self.clauses):
            return True
        else:
            return False

    def __repr__(self):
        r = ''
        for c in self.clauses:
            r += str(c) + '\n'
        return r

# sent = Sentence.from_file('../test_files/pikachu.txt')
# print(sent)
