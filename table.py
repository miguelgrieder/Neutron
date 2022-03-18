from tkinter import *
import board

class Table:
    #Classe representa o "front-end" da aplicacao
    def __init__(self):
        self._mainWindow = Tk()
        self.BoardGenerator()
        self.labels()
        self._myBoard = board.Board()
        self._mainWindow.mainloop()
        self.updateUserInterface()
        
    def BoardGenerator(self):
        #Gera o tabuleiro, inicialmente sem nenhuma peça

        self._mainWindow.title("Neutron")
        self._mainWindow.iconbitmap("images/icon.ico")
        self._mainWindow.geometry("575x650")
        self._mainWindow.resizable(False, False)
        self._mainWindow["bg"]="black"

        self._mainFrame = Frame(self._mainWindow, padx=32, pady=25, bg="black")
        self._messageFrame = Frame(self._mainWindow, padx=4, pady=1, bg="black")
        self._statusFrame = Frame(self._mainWindow, padx=4, pady=1, bg="black")

        self._empty = PhotoImage(file="images/empty.gif")        #pyimage0
        self._proton = PhotoImage(file="images/proton.gif")            #pyimage1
        self._eletron = PhotoImage(file="images/eletron.gif")        #pyimage2
        self._neutron = PhotoImage(file="images/neutron.png")    #pyimage3

        recomecar = Button(self._mainWindow, text="Recomeçar", command=self.restart)
        recomecar.place(x=30, y=600, width=100, height=20)
        #Itnera sobre matrix, composto por column sendo uma linha de posicoes
        

        self.initialFields()

    def initialFields(self):
        #Colocar as peças no lugar inicial

        #Define o tabuleiro inteiro como empty
        self._matrix=[]
        for y in range(5):
            column = []    #    column
            for x in range(5):
                field = Label(self._mainFrame, bd=2, relief="solid", image=self._empty)
                field.grid(row=x , column=y)
                field.bind("<Button-1>", lambda event, line=y+1, column=x+1: self.click(event, line, column))    #    inverted
                column.append(field)
            self._matrix.append(column)

    def restart(self):
        self._myBoard.startMatch()
        self.updateUserInterface()

    def labels(self):
        #Adiciona os textos informativos na interface
        self._labelMessage = Label(self._messageFrame, bg="black",fg="white", text='')
        self._labelStatus = Label(self._statusFrame, bg="black",fg="white", text='Clique no tabuleiro para iniciar')
        self._labelMessage.grid(row=0, column=0, columnspan=3)
        self._labelStatus.grid(row=0, column=0, columnspan=3)
        self._mainFrame.grid(row=0 , column=0)
        self._messageFrame.grid(row=3 , column=0) 
        self._statusFrame.grid(row=1 , column=0)

    def click(self, event, line, column):
        #envento ao clicar em uma posicao
        self._myBoard.click(line, column)
        self.updateUserInterface()        

    def updateUserInterface(self):
        #Atualiza o tabuleiro apos uma jogada
        self._labelMessage['text']=self._myBoard.getMessage()
        self._labelStatus['text']=self._myBoard.getStatusMessage()
        for y in range(5):    #    inverted
            for x in range(5):    #    inverted
                label = self._matrix[x][y]
                value = self._myBoard.getValue(x,y) #getvalue
                
                if value==0:
                    label['imag'] = self._empty
                elif value==1:
                    label['imag'] = self._proton
                elif value==2:
                    label['imag'] = self._eletron
                elif value==3:
                    label['imag'] = self._neutron


Table()