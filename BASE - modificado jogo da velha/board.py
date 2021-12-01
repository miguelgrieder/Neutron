import position
import player
import humanPlayer
import boardImage
import move
import random

#	Board matchStatus
# 1 - game not started (initial message)
# 2 - next player (match in progress)
# 3 - irregular move (match in progress)
# 4 - game with winner
# 5 - game tied

class Board:
	def __init__(self):
		super().__init__()
		self.player1=humanPlayer.HumanPlayer()
		self.player2=humanPlayer.HumanPlayer()
		self.player1.initialize("Jogador Vermelho", 1)
		self.player2.initialize("Jogador Branco", 2)
		self.matchStatus = 1
		self.positions=[]
		for y in range(5):
			column = []
			for x in range(5):
				column.append(position.Position())
			self.positions.append(column)

	def getStatus(self):
		return self.matchStatus

	def setStatus(self, value):
		self.matchStatus = value

	def reset(self):
		for x in range(5):
			for y in range(5):
				self.positions[x][y].empty()
		self.player1.reset()
		self.player2.reset()
		self.setStatus(1)

	def evaluateFull(self):
		full = True
		for x in range(5):
			for y in range(5):
				if (not self.positions[x][y].occupied()):
					full = False
		return full
	
	def getWinner(self):
		if (self.player1.getWinner()):
			return self.player1
		else:
			if (self.player2.getWinner()):
				return self.player2
			else:
				return None			
	
	def getPosition(self, aMove):
		x = aMove.getLine() - 1
		y = aMove.getColumn() - 1
		return self.positions[x][y]

	def getEnabledPlayer(self):
		if self.player1.getTurn():
			return self.player1
		else: 
			return self.player2

	def getDisabledPlayer(self):
		if self.player1.getTurn():
			return self.player2
		else: 
			return self.player1


	def getState(self):
		state = boardImage.BoardImage()
		# composing the message
		if (self.getStatus() == 1): 
			state.setMessage("Clique em qualquer posição para iniciar")
		elif (self.getStatus() == 2):
			state.setMessage((self.getEnabledPlayer()).getName() + " deve jogar")	
		elif (self.getStatus() == 3): 
			state.setMessage("jogada irregular - jogue novamente")
		elif (self.getStatus() == 4): 
			state.setMessage((self.getWinner()).getName() + " venceu a partida")
		elif (self.getStatus() == 5): 
			state.setMessage("A partida terminou empatada")
		# obtaining board filling	
		for x in range(5):
			for y in range(5):
				if (self.positions[x][y].occupied()):
					value = (self.positions[x][y].getOccupant()).getSymbol()
					state.setValue((x+1), (y+1), value)			
				else:
					value = 0
					state.setValue((x+1), (y+1), value)
		return state

	def proceedMove(self, aMove):
		selectedPosition = self.getPosition(aMove)
		if selectedPosition.occupied():
			self.setStatus(3)	#	irregular move
		else:
			enabledPlayer = self.getEnabledPlayer()
			disabledPlayer = self.getDisabledPlayer()
			selectedPosition.setOccupant(enabledPlayer)

			if enabledPlayer.getWinner():	#	winner
				self.setStatus(4)
			else:
				if self.evaluateFull():		#	tied
					self.setStatus(5)
				else:						#	next player
					self.setStatus(2)
					newState = self.getState()
					enabledPlayer.disable()
					newMove = disabledPlayer.enable(newState)
					if (newMove.getLine()!=0):
						self.proceedMove(newMove)

	def startMatch(self):
		self.reset()
		self.setStatus(2)
		initialState = boardImage.BoardImage()
		if random.randint(1,2)==1:
			self.player1.enable(initialState)
		else:
			aMove = self.player2.enable(initialState)
			self.proceedMove(aMove)

	def click(self, line, column):
		if (self.getStatus()==1):
			self.startMatch()
		else:
			if (self.getStatus()==2 or self.getStatus()==3):
				aMove = move.Move(line, column)
				self.proceedMove(aMove)
			else:
				if (self.getStatus()==4 or self.getStatus()==5):
					self.reset()
		
#-----------------------------------------------------------------------------------------------------------------------------------
					