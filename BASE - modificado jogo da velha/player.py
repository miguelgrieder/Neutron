#import abc
#class Player(metaclass=abc.ABCMeta):
class Player():
	def __init__(self):
		self.symbol = None	#int
		self.turn = False	#boll
		self.winner = False	#boll
		self.name = ''	#string

	#@abstractmethod
	def enable(self, state):
		pass

	def initialize(self, aName, aSymbol):
		self.symbol = aSymbol	#int
		self.name = aName		#string
		self.turn = False		#bool
		self.winner = False		#bool

	def reset(self):
		self.turn = False		#bool
		self.winner = False		#bool

	def disable(self):
		self.turn = False
	 
	def getSymbol(self):
		return self.symbol
	 
	def getName(self):
		return self.name
	
	def getWinner(self):
		return self.winner
	 
	def setWinner(self):
		self.winner = True
	 
	def getTurn(self):
		return self.turn