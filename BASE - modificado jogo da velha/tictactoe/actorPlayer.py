from tkinter import *
import board

class ActorPlayer:
	def __init__(self):
		self.mainWindow = Tk()
		self.BoardGenerator()
		self.labels()
		self.myBoard = board.Board()
		self.mainWindow.mainloop()

	def BoardGenerator(self):
		#Gera o tabuleiro, inicialmente sem nenhuma peça

		self.mainWindow.title("Neutron")
		self.mainWindow.iconbitmap("images/icon.ico")
		self.mainWindow.geometry("575x615")
		self.mainWindow.resizable(False, False)
		self.mainWindow["bg"]="black"

		self.mainFrame = Frame(self.mainWindow, padx=32, pady=25, bg="black")
		self.messageFrame = Frame(self.mainWindow, padx=4, pady=1, bg="black")

		self.empty = PhotoImage(file="images/empty.gif")		#pyimage0
		self.white = PhotoImage(file="images/white.gif")		#pyimage2
		self.red = PhotoImage(file="images/red.gif")			#pyimage1
		self.neutron = PhotoImage(file="images/neutron.png")	#pyimage3

		#Itnera sobre boardView, composto por viewTier sendo uma linha de posicoes
		self.boardView=[]
		for y in range(5):
		    viewTier = []	#	column
		    for x in range(5):
		    	aLabel = Label(self.mainFrame, bd=2, relief="solid", image=self.empty)
		    	aLabel.grid(row=x , column=y)
		    	aLabel.bind("<Button-1>", lambda event, line=y+1, column=x+1: self.click(event, line, column))	#	inverted
		    	viewTier.append(aLabel)
		    self.boardView.append(viewTier)

		self.initialPositions(viewTier)
		

	def labels(self):
		#Adiciona os textos informativos na interface
		self.labelMessage = Label(self.messageFrame, bg="black",fg="white", text='Clique no tabuleiro para iniciar')
		self.labelMessage.grid(row=0, column=0, columnspan=3)
		self.mainFrame.grid(row=0 , column=0)
		self.messageFrame.grid(row=1 , column=0) 


	def initialPositions(self, viewTier):
		#Colocar as peças no lugar inicial

		#neutron
		neut = Label(self.mainFrame, bd=3, relief="solid", image=self.neutron)
		neut.grid(row=2 , column=2)
		neut.bind("<Button-1>", lambda event, line=2, column=2: self.click(event, line, column))
		viewTier.append(neut)
		self.boardView[2][2] = neut
		self.boardView.append(viewTier)

		#red 
		for y in range(5):
		    viewTier = []	#	column
		    aLabel = Label(self.mainFrame, bd=1, relief="solid", image=self.red)
		    aLabel.grid(row=0 , column=y)
		    aLabel.bind("<Button-1>", lambda event, line=y+1, column=0+1: self.click(event, line, column))	#	inverted
		    viewTier.append(aLabel)
		    self.boardView.append(viewTier)

		#white
		for y in range(5):
		    viewTier = []	#	column
		    aLabel = Label(self.mainFrame, bd=2, relief="solid", image=self.white)
		    aLabel.grid(row=4 , column=y)
		    aLabel.bind("<Button-1>", lambda event, line=y+1, column=4+1: self.click(event, line, column))	#	inverted
		    viewTier.append(aLabel)
		    self.boardView.append(viewTier)


	def click(self, event, line, column):
		#envento ao clicar em uma posicao
		self.myBoard.click(line, column)
		self.updateUserInterface()

	def updateUserInterface(self):
		#Atualiza o tabuleiro apos uma jogada
		newState = self.myBoard.getState()
		self.labelMessage['text']=newState.getMessage()
		for y in range(5):	#	inverted
			for x in range(5):	#	inverted
				label = self.boardView[x][y]
				value = newState.getValue(x+1, y+1)
				if value==0:
					label['imag'] = self.empty
				elif value==1:
					label['imag'] = self.red
				elif value==2:
					label['imag'] = self.white
				elif value==3:
					label['imag'] = self.neutron