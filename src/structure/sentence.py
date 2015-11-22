from structure.clause import Clause


class Sentence:
    """
    Sentence that represents a SAT problem with a set of clauses with restrictions.
    """

    def __init__(self):
        self.clauses = []
        self.variables = 0
        self.dim = 0

    @staticmethod
    def from_file(path, numclauses=1000000000):
        sentence = Sentence()
        i = 0
        # this method loads a file into a object of this class.
        with open(path) as file:
            for line in file:
                # for each line in the file verify if the structure of the line is correct.
                words = line.split()
                if len(words) != 0 and words[0] is 'c':
                    # comments line should be ignored
                    continue
                elif len(words) != 0 and words[0] == 'p' and words[1] == 'cnf' and len(words) == 4:
                    # Read format
                    # Number of clauses
                    sentence.dim = int(words[3])
                    # Number of variables
                    sentence.variables = int(words[2])
                elif len(words) != 0 and words[0] != '%' and 1 <= abs(int(words[0])) <= sentence.variables:
                    # Read clause line
                    if i < numclauses:
                        # Check if the number of wanted clauses is lower than the intended
                        # Add clause to list
                        aux = words[:-1]
                        cl = Clause(aux)
                        sentence.clauses.append(cl)
                        i += 1
                    else:
                        # If we already have the number of clauses we want, return sentence.
                        sentence.dim = numclauses
                        return sentence
        return sentence

    def get_validated_clauses(self, solution):
        # Check the number of satisfied clauses with model 'solution'.
        r = 0
        for c in self.clauses:
            if c.is_clause_satisfied(solution):
                r += 1
        return r

    def is_satisfied(self, solution):
        # Check if the sentence is satisfied.
        if self.get_validated_clauses(solution) == len(self.clauses):
            return True
        else:
            return False

    @staticmethod
    def simplify(other, literal, key):
        # Useful for DPLL, this removes literals from clauses already checked on the algorithm.
        # Returns the new modified sentence
        s = Sentence()
        s.variables = other.variables
        for c in other.clauses:
            q = c.has_literal(literal)
            if q and c.exists(literal, key):
                continue
            elif q:
                c.remove_literal(literal)
                s.clauses.append(c)
            else:
                s.clauses.append(c)
        return s



    def is_model_verified(self, solution):
        # Useful for DPLL, this checks if the model found verifies the sentence.
        if len(self.clauses) == 0:
            return True
        else:
            return False

    def is_model_wrong(self, solution):
        # Useful for DPLL, this checks if the model found doesn't verify sentece.
        for c in self.clauses:
            if c.empty():
                return True
        return False

    def false_clauses(self, solution):
        # Useful for walksat, this method returns the unsatisfied clauses from sentence with model solution.
        false_sentences = []
        for c in self.clauses:
            if not c.is_clause_satisfied(solution):
                false_sentences.append(c)
        return false_sentences

    def find_pure_symbol(self, symbols):
        # Finds pure symbol in clauses of sentence, returns its literal and correspondent value.
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
        # Finds unit clause in clauses of sentence, returns its literal and correspondent value.
        for c in self.clauses:
            literal, bl = c.get_unit_symbol()
            if literal is not None and literal in symbols:
                return literal, bl
        return None, None

    def variable_set(self):
        # Creates an array of literals in order of the total appearances of this symbol.
        # This will serve as an heuristic to speed up DPLL
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
        # This method makes a deep copy of this object.
        r = Sentence()
        r.variables = other.variables
        r.dim = other.dim
        for c in other.clauses:
            aux = Clause.copy(c)
            r.clauses.append(aux)
        return r

    def __repr__(self):
        r = ''
        for c in self.clauses:
            r += str(c) + '\n'
        return r
