from src.structure.sentence import Sentence
from src.structure.solution import Solution
from random import choice
from random import random


class Algorithms:
    """
        Algorithms that solve SAT problems
    """

    @staticmethod
    def gsat(sentence, max_restarts, max_climbs):
        sl = Solution(sentence.variables)
        for i in range(max_restarts):
            # For each symbol assign a random boolean.
            sl.restart()
            for j in range(max_climbs):
                # Checks if sentence is satisfied by the current values of literals in solution object.
                if sentence.is_satisfied(sl):
                    return sl
                else:
                    # Variable to track the best score for satisfied clauses.
                    max_score = sentence.get_validated_clauses(sl)
                    # Variable to store the literal attribution of the best score.
                    best = None
                    for literal in range(1, sentence.variables + 1):
                        sl.toggle(literal)
                        score = sentence.get_validated_clauses(sl)
                        if score > max_score:
                            max_score = score
                            best = literal
                        sl.toggle(literal)
                    if best is not None:
                        sl.toggle(best)
        return 'No solution was found.'

    @staticmethod
    def walksat(sentence, p, max_flips):
        # Instatiate the model for the problem
        sl = Solution(sentence.variables)
        # For each symbol assign a random boolean.
        sl.restart()
        for i in range(max_flips):
            # Checks if sentence is satisfied by the current values of literals in solution object.
            if sentence.is_satisfied(sl):
                return sl
            else:
                # Get the list of false clauses from the model and sentence.
                falses_clauses = sentence.false_clauses(sl)
                # Choose a random false clause from the sentence.
                false_cl = choice(falses_clauses)
                # with probability p flip the value of a randomly selected symbol from clause.
                if p > random():
                    random_literal = choice(false_cl.get_literals())
                    sl.toggle(random_literal)
                else:
                    # flip whichever symbol in clause that maximizes the number of satisfied clauses.
                    # Variable to track the best score for satisfied clauses.
                    max_score = sentence.get_validated_clauses(sl)
                    # Variable to store the literal attribution of the best score.
                    best = None
                    for literal in false_cl.get_literals():
                        sl.toggle(literal)
                        score = sentence.get_validated_clauses(sl)
                        if score > max_score:
                            max_score = score
                            best = literal
                        sl.toggle(literal)
                    if best is not None:
                        sl.toggle(best)
        return 'No solution was found.'


    @staticmethod
    def setup_dpll(sentence):
        model = Solution()
        symbols = sentence.variable_set()
        return (Algorithms.dpll(Sentence.sent_copy(sentence), symbols.copy(), model.deep_copy()) or Algorithms.dpll(Sentence.sent_copy(sentence), symbols.copy(), model.deep_copy()))

    @staticmethod
    def dpll(sentence, symbols, model):
        if sentence.is_model_verified(model):
            return True
        if sentence.is_model_wrong(model):
            return False
        s, bl = sentence.find_pure_symbol(symbols)
        if s:
            symbols.remove(s)
            model.set(s, bl)
            return Algorithms.dpll(sentence, symbols, model)
        s, bl = sentence.find_unit_clause(symbols)
        if s:
            symbols.remove(s)
            model.set(s, bl)
            return Algorithms.dpll(sentence, symbols, model)
        s = symbols.pop()
        model2 = model.deep_copy()
        model.set(s, True)
        model2.set(s, False)
        return (Algorithms.dpll(Sentence.sent_copy(sentence), symbols.copy(), model) or Algorithms.dpll(Sentence.sent_copy(sentence), symbols.copy(), model2))


sent = Sentence.from_file('../test_files/uf20/uf20-01.cnf')
# r = Algorithms.gsat(sent, 50, 30)
r = Algorithms.walksat(sent, 0.8, 500)

print(r)
