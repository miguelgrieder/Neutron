class BoardImage:
	#Realiza a comunicacao entra board(back) e actorplayer(front) para a exibicao
	def __init__(self):
		super().__init__()
		self.message=""
		self.map=[]
		for y in range(5):
			column = []
			for x in range(5):
				if y ==0: #red
					num = 1
				if y ==4: #white
					num = 2
				column.append(num)
			self.map.append(column)
		self.map[2][2] = 3 #neutron

	 
	def getValue(self, line, column):
		return self.map[(line-1)][(column-1)]

	def setValue(self, line, column, value):
		self.map[(line-1)][(column-1)] = value

