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
        self.mainWindow.geometry("575x650")
        self.mainWindow.resizable(False, False)
        self.mainWindow["bg"]="black"

        self.mainFrame = Frame(self.mainWindow, padx=32, pady=25, bg="black")
        self.messageFrame = Frame(self.mainWindow, padx=4, pady=1, bg="black")
        self.statusFrame = Frame(self.mainWindow, padx=4, pady=1, bg="black")

        self.empty = PhotoImage(file="images/empty.gif")        #pyimage0
        self.proton = PhotoImage(file="images/proton.gif")            #pyimage1
        self.eletron = PhotoImage(file="images/eletron.gif")        #pyimage2
        self.neutron = PhotoImage(file="images/neutron.png")    #pyimage3

        #Itnera sobre matrix, composto por column sendo uma linha de posicoes
        

        self.initialFields()

    def initialFields(self):
        #Colocar as peças no lugar inicial

        #Define o tabuleiro inteiro como empty
        self.matrix=[]
        for y in range(5):
            column = []    #    column
            for x in range(5):
                field = Label(self.mainFrame, bd=2, relief="solid", image=self.empty)
                field.grid(row=x , column=y)
                field.bind("<Button-1>", lambda event, line=y+1, column=x+1: self.click(event, line, column))    #    inverted
                column.append(field)
            self.matrix.append(column)
            
    def labels(self):
        #Adiciona os textos informativos na interface
        self.labelMessage = Label(self.messageFrame, bg="black",fg="white", text='')
        self.labelStatus = Label(self.statusFrame, bg="black",fg="white", text='Clique no tabuleiro para iniciar')
        self.labelMessage.grid(row=0, column=0, columnspan=3)
        self.labelStatus.grid(row=0, column=0, columnspan=3)
        self.mainFrame.grid(row=0 , column=0)
        self.messageFrame.grid(row=3 , column=0) 
        self.statusFrame.grid(row=1 , column=0)

    def click(self, event, line, column):
        #envento ao clicar em uma posicao
        self.myBoard.click(line, column)
        self.updateUserInterface()        

    def updateUserInterface(self):
        #Atualiza o tabuleiro apos uma jogada
        self.labelMessage['text']=self.myBoard.getMessage()
        self.labelStatus['text']=self.myBoard.getStatusMessage()
        for y in range(5):    #    inverted
            for x in range(5):    #    inverted
                label = self.matrix[x][y]
                value = self.myBoard.getValue(x,y) #getvalue
                
                if value==0:
                    label['imag'] = self.empty
                elif value==1:
                    label['imag'] = self.proton
                elif value==2:
                    label['imag'] = self.eletron
                elif value==3:
                    label['imag'] = self.neutron


Table()