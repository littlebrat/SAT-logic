from src.structure.sentence import Sentence
from src.structure.clause import Clause
from random import getrandbits
import operator

class Algorithms:
	"""
	Algorithms that solve SAT problems
	"""

	def __init__(self):
		self.data = None

	@staticmethod
	def gsat(sentence, max_restarts, max_climbs):
		for i in max_restarts:
			e=0 #e is a variable that is used to run through A to change each symbol's value
			#for each symbol assign a random boolean
			for k in variables: #variables is the number of different symbols in the sentence
				A[k] = not getrandbits(1) #A is the set of literals
			aux = A
			for j in max_climbs:
				s = conjunction(A) #function that does the conjunction of clauses and returns true or false for the sentence (s)
				#check if the current set of literals satisfies the sentence
				if s is True:
					return A
					break
				else:
					for e is variables:
						A[e] = not A[e] #change the value of a symbol
						evaluationscore[e] = evaluation(A) #evaluation function to determine the operator that yields the best evaluation
						A = aux #revert the previous symbol change
					max_index, max_value = max(enumerate(evaluationscore), key=operator.itemgetter(1)) #find the best evaluation score and it's index
					aux[max_index] = not aux[max_index]
					A = aux #change the value of the symbol, which provides the best evaluation score, permanently
					e=0
		return Exception('Failure on GSAT')
					
	#@staticmethod
	#def walksat(clauses,p,max_flips):
		
