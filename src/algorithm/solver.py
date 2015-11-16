from src.structure.sentence import Sentence
from src.structure.solution import Solution
import random

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
                    if best != None:
                        sl.toggle(best)
        return 'No solution was found.'

    def walksat(sentence, p, max_flips):
        sl = Solution(sentence.variables) #sl is the set of symbols in the sentence
        sl.restart() #sl is now the model which means that there was a random assignment of true/false to the symbols in clauses
        for i in range(max_flips):
            # Checks if sentence is satisfied by the current values of literals in solution object.
            if sentence.is_satisfied(sl):
                return sl
            else:
                # Choose a random false clause from the sentence.
                clause = Randomfalseclause()  # it still does not exist. i want this in symbols not in booleans.
                # with probability p flip the value of a randomly selected symbol from clause.
                if p>random.random():
                    index = random.choice(clause)
                    sl.toggle[abs(index)-1]
                # flip whichever symbol in clause that maximizes the number of satisfied clauses.
                else:
                    # Variable to track the best score for satisfied clauses.
                    if
                    max_score = sentence.get_validated_clauses(sl)
                    # Variable to store the literal attribution of the best score.
                    best = None
                    for literal in range(len(clause)):
                        sl.toggle(abs(clause[literal])-1)
                        score = sentence.get_validated_clauses(sl)
                        if score > max_score:
                            max_score = score
                            best = abs(clause[literal])-1
                        sl.toggle(abs(clause[literal])-1)
                    if best != None:
                        sl.toggle(best)
        return 'No solution was found.'

sent = Sentence.from_file('../test_files/charmander.txt')
r = Algorithms.gsat(sent, 50, 20)
print(r)

