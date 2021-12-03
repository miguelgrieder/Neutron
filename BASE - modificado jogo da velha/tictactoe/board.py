import position
import player
import humanPlayer
import boardImage
import move
import random

#	Estados do jogo
# 1 - Jogo nao iniciado
# 2 - Proximo jogador
# 3 - Jogada iregular
# 4 - Jogo finalizado com vencedor
# 5 - Jogo finalizado empatado

class Board:
	#Realiza a gerencia real do tabuleiro "back-end"
	def __init__(self):
		#Define os jogadores
		super().__init__()
		self.player1=humanPlayer.HumanPlayer()
		self.player2=humanPlayer.HumanPlayer()
		self.player1.initialize("Jogador Vermelho", 1)
		self.player2.initialize("Jogador Branco", 2)
		self.matchStatus = 1
		#Define as posicoes no "backend"
		self.positions=[]
		for y in range(5):
			column = []
			for x in range(5):
				column.append(position.Position())
			self.positions.append(column)

	def getStatus(self):
		#Retorna o estado do jogo
		return self.matchStatus

	def setStatus(self, value):
		#Define o estado do jogo
		self.matchStatus = value

	def reset(self):
		#Reinicia o tabuleiro com todas posicoes vazias
		for x in range(5):
			for y in range(5):
				self.positions[x][y].empty()
		self.player1.reset()
		self.player2.reset()
		self.setStatus(1)

	def evaluateFull(self):
		#Testa se o tabuleiro esta cheio, apos checar se tenha vencidor( entao jogo empatado)
		full = True
		for x in range(5):
			for y in range(5):
				if (not self.positions[x][y].occupied()):
					full = False
		return full
	
	def getWinner(self):
		#Retorna o vencedor, caso seja
		if (self.player1.getWinner()):
			return self.player1
		else:
			if (self.player2.getWinner()):
				return self.player2
			else:
				return None			
	
	def getPosition(self, aMove):
		#Retorna o estado da posicao indicada 
		x = aMove.getLine() - 1
		y = aMove.getColumn() - 1
		return self.positions[x][y]

	def getEnabledPlayer(self):
		#Retorna o jogador da rodada
		if self.player1.getTurn():
			return self.player1
		else: 
			return self.player2

	def getDisabledPlayer(self):
		#Retorna o jogador da proxima rodada
		if self.player1.getTurn():
			return self.player2
		else: 
			return self.player1


	def getState(self):
		state = boardImage.BoardImage()
		# Retorna a mensagem do estado
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
		#Realiza a jogada, e testa qual condica
		selectedPosition = self.getPosition(aMove)
		if selectedPosition.occupied():
			self.setStatus(3)	#Local ocupado - irregular
		else:
			#Jogada regular, testar resultado
			enabledPlayer = self.getEnabledPlayer()
			disabledPlayer = self.getDisabledPlayer()
			selectedPosition.setOccupant(enabledPlayer)

			if enabledPlayer.getWinner():	#	Caso vença
				self.setStatus(4)
			else:
				if self.evaluateFull():		#	Caso empate
					self.setStatus(5)
				else:						#	Caso continue o jogo
					self.setStatus(2)
					newState = self.getState()
					enabledPlayer.disable()
					newMove = disabledPlayer.enable(newState)
					if (newMove.getLine()!=0):
						self.proceedMove(newMove)

	def startMatch(self):
		# Comeca uma nova partida
		self.reset()
		self.setStatus(2)
		initialState = boardImage.BoardImage()
		if random.randint(1,2)==1:
			self.player1.enable(initialState)
		else:
			aMove = self.player2.enable(initialState)
			self.proceedMove(aMove)

	def click(self, line, column):
		# Realiza os processos ao jogador clicar em uma posicao
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
					