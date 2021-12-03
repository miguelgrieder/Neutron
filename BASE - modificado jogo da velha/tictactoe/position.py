class Position:
	#Representa uma posicao do tabuleiro
	def __init__(self):
		self.occupant = None
	 
	def occupied(self):
		return (self.occupant != None)
	 
	def setOccupant(self, aPlayer):
		self.occupant = aPlayer
	 
	def getOccupant(self):
		return self.occupant
	 
	def empty(self):
		self.occupant = None
	 
	def samePlayer(self, p1, p2):
		if (self.occupied() and p1.occupied() and p2.occupied()):
			return (  (self.occupant is p1.getOccupant()) and (self.occupant is p2.getOccupant()) )
		else:
			return False