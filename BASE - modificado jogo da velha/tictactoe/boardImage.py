class BoardImage:
	#Realiza a comunicacao entra board(back) e actorplayer(front) para a exibicao
	def __init__(self):
		super().__init__()
		self.message=""
		self.map=[]
		for y in range(5):
			column = []
			for x in range(5):
				column.append(0)
			self.map.append(column)

	def getMessage(self):
		return self.message
	 
	def getValue(self, line, column):
		return self.map[(line-1)][(column-1)]
	 
	def setMessage(self, text):
		self.message = text
	 
	def setValue(self, line, column, value):
		self.map[(line-1)][(column-1)] = value
	 
	def emptyPosition(self, line, column):
		return (self.map[line-1][column-1] == 0)
	 
	def occupiedPosition(self, line, column):
		return (self.map[line-1][column-1] != 0)
	 
	def getEmptyCenter(self):
		return (self.emptyPosition(2, 2))

	def getEmpty(self):
		empty = True
		for x in range(5):
			for y in range(5):
				if self.occupiedPosition(x+1, y+1):
					empty = False
		return empty

	def occupiedPositionsOnTheLine(self, line):
		cont = 0
		for x in range(5):
			if self.occupiedPosition(line, x+1):
				cont=cont+1
		return cont
	 
	def occupiedPositionsOnTheColumn(self, column):
		cont = 0
		for x in range(5):
			if self.occupiedPosition(x+1, column):
				cont=cont+1
		return cont
