from structure.sentence import Sentence
from structure.solution import Solution
from random import choice
from random import random

from time import time


class Algorithms:
    """
        Algorithms that solve SAT problems
    """
    def __init__(self):
        self.model = None

    def get_model(self):
        # Gets the model found for this problem.
        return self.model

    @staticmethod
    def gsat(sentence, max_restarts, max_climbs):
        sl = Solution(sentence.variables)
        for i in range(max_restarts):
            # For each symbol assign a random boolean.
            sl.restart()
            for j in range(max_climbs):
                # Checks if sentence is satisfied by the current values of literals in solution object.
                if sentence.is_satisfied(sl):
                    return True, sl
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
        return False, None

    @staticmethod
    def walksat(sentence, p, max_flips):
        # Instatiate the model for the problem
        sl = Solution(sentence.variables)
        # For each symbol assign a random boolean.
        sl.restart()
        for i in range(max_flips):
            # Checks if sentence is satisfied by the current values of literals in solution object.
            if sentence.is_satisfied(sl):
                return True, sl
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
        return False, None

    @staticmethod
    def setup_dpll(sentence):
        # Method to initialize the dpll algorithm.
        alg = Algorithms()
        model = Solution(sentence.variables)
        symbols = sentence.variable_set()
        return Algorithms.dpll(sentence, symbols, model, alg), alg.get_model()

    @staticmethod
    def dpll(sentence, symbols, model, alg):
        if sentence.is_model_verified(model):
            alg.model = model
            return True
        if sentence.is_model_wrong(model):
            return False
        s, bl = sentence.find_pure_symbol(symbols)
        if s:
            new_sentence = Sentence.simplify(sentence, s, bl)
            symbols.remove(s)
            model.set(s, bl)
            return Algorithms.dpll(new_sentence, symbols, model, alg)
        s, bl = sentence.find_unit_clause(symbols)
        if s:
            new_sentence = Sentence.simplify(sentence, s, bl)
            symbols.remove(s)
            model.set(s, bl)
            return Algorithms.dpll(new_sentence, symbols, model, alg)
        s = symbols.pop()
        model2 = Solution.deep_copy(model)
        model.set(s, True)
        model2.set(s, False)
        new_sentence2 = Sentence.sent_copy(sentence)
        return (Algorithms.dpll(Sentence.simplify(sentence, s, True), symbols.copy(), model, alg) or Algorithms.dpll(Sentence.simplify(new_sentence2, s, False), symbols.copy(), model2, alg))

    @staticmethod
    def to_file(filename, sentence, solution, result):
        # Method that outputs the solution in cnf file.
        c = 'c ' + filename + '\n'
        s = 's cnf ' + str(result) + ' ' + str(sentence.variables) + ' ' + str(sentence.dim) + '\n'
        r = ''
        for l in range(1, sentence.variables + 1):
            if solution.literal(l) is not None:
                r += 'v ' + str(solution.int_literal(l)) + '\n'
            elif solution.literal(l) is None and result is True:
                r += 'v ' + str(-l) + '\n'
        with open(filename + '_sol.cnf', "w") as text_file:
            res = c + s + r
            text_file.write(res)
