from src.structure.sentence import Sentence
from src.structure.solution import Solution


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

sent = Sentence.from_file('../test_files/charmander.txt')
r = Algorithms.gsat(sent, 50, 20)
print(r)