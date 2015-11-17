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

    def false_clauses(self, solution):
        false_sentences = []
        for c in self.clauses:
            if not c.is_clause_satisfied(solution):
                false_sentences.append(c)
        return false_sentences

    def find_pure_symbol(self, symbols):
        for s in symbols:
            found_pos, found_neg = False, False
            for c in self.clauses:
                if not found_pos and c.exists(s, True):
                    found_pos = True
                if not found_neg and c.exists(s, False):
                    found_neg = True
            if found_pos != found_neg:
                return s, found_pos
        return None, None

    def find_unit_clause(self, symbols):
        for c in self.clauses:
            literal, bl = c.get_unit_symbol()
            if literal is not None and literal in symbols:
                return literal, bl
        return None, None

    def variable_set(self):
        v_order = {}
        for v in range(1, self.variables + 1):
            v_order[v] = 0
        for c in self.clauses:
            for vr in range(1, self.variables + 1):
                if c.has_literal(vr):
                    v_order[vr] += 1
        x = sorted(list(v_order.keys()), key=v_order.__getitem__)
        return x

    @staticmethod
    def sent_copy(other):
        r = Sentence()
        r.variables = other.variables
        for c in other.clauses:
            aux = Clause.copy(c)
            r.clauses.append(aux)
        return r

    def __repr__(self):
        r = ''
        for c in self.clauses:
            r += str(c) + '\n'
        return r

# sent = Sentence.from_file('../test_files/pikachu.txt')
# print(sent)
