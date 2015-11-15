from src.structure.sentence import Sentence
from src.structure.clause import Clause
from random import getrandbits

class Algorithms:
	"""
	Algorithms that solve SAT problems
	"""

	def __init__(self):
		self.data = None

	@staticmethod
	def gsat(sentence, max_restarts, max_climbs):
		for i in max_restarts:
			#for each symbol assign a random boolean
			for k in variables: #variables is the number of different symbols in the sentence
				A[k] = not getrandbits(1) #A is the set of literals
			aux = A
			for j in max_climbs:
				literal=0 #literal is a variable that is used to run through A to change each symbol's value
				s = conjunction(A) #function that does the conjunction of clauses and returns true or false for the sentence (s)
				#check if the current set of literals satisfies the sentence
				if s is True:
					return A
					break
				else:
					max_score = 0 #max_score, which contains the best evaluation score, is initialized
					index = -1
					for literal in variables:
						A[literal] = not A[literal] #change the value of a symbol
						evaluationscore[literal] = evaluation(A) #evaluation function to determine the operator that yields the best evaluation
						if evaluationscore[literal]>max_score #check the current best evaluation score and it's index
							max_score = evaluationscore[literal]
							index = literal
						A = aux #revert the previous symbol change
					if index != -1 #if an evaluation score was found (at least one clause is true) then a symbol is permanently changed
						aux[index] = not aux[index]
						A = aux #change the value of the symbol, which provides the best evaluation score, permanently
		return Exception('Failure on GSAT')
					
	#@staticmethod
	#def walksat(clauses,p,max_flips):
		
