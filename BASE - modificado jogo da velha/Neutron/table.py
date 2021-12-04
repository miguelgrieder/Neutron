from tkinter import *
import board

class Table:
	#Classe representa o "front-end" da aplicacao
	def __init__(self):
		self.mainWindow = Tk()
		self.BoardGenerator()
		self.labels()
		self.myBoard = board.Board()
		self.mainWindow.mainloop()
		self.updateUserInterface()
        
	def BoardGenerator(self):
		#Gera o tabuleiro, inicialmente sem nenhuma peça

		self.mainWindow.title("Neutron")
		self.mainWindow.iconbitmap("images/icon.ico")
		self.mainWindow.geometry("575x615")
		self.mainWindow.resizable(False, False)
		self.mainWindow["bg"]="black"

		self.mainFrame = Frame(self.mainWindow, padx=32, pady=25, bg="white")
		self.messageFrame = Frame(self.mainWindow, padx=4, pady=1, bg="white")

		self.empty = PhotoImage(file="images/empty.gif")		#pyimage0
		self.red = PhotoImage(file="images/red.gif")			#pyimage1
		self.white = PhotoImage(file="images/white.gif")		#pyimage2
		self.neutron = PhotoImage(file="images/neutron.png")	#pyimage3

		#Itnera sobre matrix, composto por column sendo uma linha de posicoes
		

		self.initialPositions()

	def initialPositions(self):
		#Colocar as peças no lugar inicial

		#Define o tabuleiro inteiro como empty
		self.matrix=[]
		for y in range(5):
		    column = []	#	column
		    for x in range(5):
		    	field = Label(self.mainFrame, bd=2, relief="solid", image=self.empty)
		    	field.grid(row=x , column=y)
		    	field.bind("<Button-1>", lambda event, line=y+1, column=x+1: self.click(event, line, column))	#	inverted
		    	column.append(field)
		    self.matrix.append(column)
			





	def labels(self):
		#Adiciona os textos informativos na interface
		self.labelMessage = Label(self.messageFrame, bg="black",fg="white", text='Clique no tabuleiro para iniciar')
		self.labelMessage.grid(row=0, column=0, columnspan=3)
		self.mainFrame.grid(row=0 , column=0)
		self.messageFrame.grid(row=1 , column=0) 

	def click(self, event, line, column):
		#envento ao clicar em uma posicao
		self.myBoard.click(line, column)
		self.updateUserInterface()		

	def updateUserInterface(self):
		#Atualiza o tabuleiro apos uma jogada

		newState = self.myBoard.getState()

		self.labelMessage['text']=self.myBoard.getMessage()
		for y in range(5):	#	inverted
			for x in range(5):	#	inverted
				label = self.matrix[x][y]
				value = newState.getValue(x+1, y+1) #getvalue
				if value==0:
					label['imag'] = self.empty
				elif value==1:
					label['imag'] = self.red
				elif value==2:
					label['imag'] = self.white
				elif value==3:
					label['imag'] = self.neutron


Table()