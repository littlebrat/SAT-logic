from src.structure.sentence import Sentence
from src.structure.solution import Solution
from src.structure.clause import Clause
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
                    if best != None:
                        sl.toggle(best)
        return 'No solution was found.'

sent = Sentence.from_file('../test_files/pokemon/charmander.txt')
# r = Algorithms.gsat(sent, 50, 20)
r = Algorithms.walksat(sent, 0.5, 20)
print(r)

