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
			#for each literal assign a random boolean
			for k in variables:
				A[k] = not getrandbits(1)
			#check if the current set of literals satisfies the sentence
			for j in max_climbs:
				sentence = conjunction(A) #function that does the conjunction of clauses and returns true or false for the sentence
				if sentence is True:
					return A
					break
		return Exception('Failure on GSAT')
					


		@staticmethod
		def gsat
