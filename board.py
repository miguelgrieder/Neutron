import field
import player
import humanPlayer
import move
import random
import neutron

#    Estados do jogo
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
        self.neutron = neutron.Neutron()
        self.player1=humanPlayer.HumanPlayer()
        self.player2=humanPlayer.HumanPlayer()
        self.player1.initialize("Jogador Próton", 1)
        self.player2.initialize("Jogador Elétron", 2)
        self.matchStatus = -1
        #Define as posicoes no "backend"
        self.fields=[]
        self.message = 1
        self.initialPieces()
        
    def initialPieces(self):
        #Define as posicaos iniciais do tabuleiro
        for y in range(5):
            column = []
            for x in range(5):
                    column.append(field.Field(None))
            self.fields.append(column)

        for i in range(5):
            self.fields[i][0] = field.Field(self.player1)
        for i in range(5):
            self.fields[i][4] = field.Field(self.player2)

        self.fields[2][2] = field.Field(self.neutron)

    def getStatus(self):
        #Retorna o estado do jogo
        # -1 - antes de partida iniciar
        # 0 - vez  de selecionar a peca do time
        # 1 - vez de selecionar local vazio para onde mover a peca time
        # 2 - vez de selecionar local vazio para onde mover o  neutron
        return self.matchStatus

    def setStatus(self, value):
        #Define o estado do jogo
        self.matchStatus = value

    def getStatusMessage(self):
        # Retorna a mensagem de estado
        status = self.getStatus()
        jogador = (self.getEnabledPlayer().getName())

        if (status == 0): 
            self.statusMessage = (jogador + " - Selecione uma peça sua para mover - status0")
        elif (status == 1):
            self.statusMessage = (jogador + " - Selecione a posição para mover sua peça - status1")
        elif (status == 2): 
            self.statusMessage = (jogador + " - Selecione a posição para mover o Neutron - status2")
        else:
            self.statusMessage = status
        return self.statusMessage

    def setMessage(self, message):
        self.message = message

    def getMessage(self):
        # Retorna a mensagem de advertencia
        message = self.message
        jogador = (self.getEnabledPlayer().getName())

        if (message == 1): 
            self.message = ""
        elif (message == 2): 
            self.message = ("Local vazio. Selecione novamente")

        elif (message == 10): 
            self.message = ""#(jogador + " deve selecionar para onde mover") 
        elif (message == 11): 
            self.message = ("Local incorreto. Jogue novamente")

        elif (message == 20): 
            self.message = ""#("Agora selecione para onde o neutron movera" + jogador)
        
        elif (message == 30): 
            self.message = ("A peça clicada é do oponente! Jogue novamente")
        elif (message == 31): 
            self.message = ("A peça clicada é o Neutron! Jogue novamente")
        elif (message == 32): 
            self.message = ("")
        
        return self.message
        
    
    def getField(self, aMove):
        #Retorna o estado da posicao indicada 
        x = aMove.getLine() - 1
        y = aMove.getColumn() - 1
        return self.fields[x][y]

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

    def getValue(self, x, y):  
        #Retorna o tipo de peça de um campo
        if (self.fields[x][y].occupied()):    
            value = (self.fields[x][y].getOccupant()).getSymbol()        
        else:
            value = 0   
        return value
    
    
    def proceedMove(self, aMove):
        #Realiza a jogada, e testa qual condica
        selectedField = self.getField(aMove)
        enabledPlayer = self.getEnabledPlayer()
        disabledPlayer = self.getDisabledPlayer()
        status = self.getStatus()
        if status == -1:
            self.setStatus(0)
            self.setMessage(1)

        else:
            if not selectedField.occupied(): #CLIQUE EM LOCAL VAZIO 
                if status == 0:# x + na  vez selecionar peça time 
                    self.setMessage(2)
                    
                elif status == 2:  #move o neutron
                    enabledPlayer.disable()
                    newMove = disabledPlayer.enable()
                    self.setStatus(0)
                    self.setMessage(1)
                    if (newMove.getLine()!=0):
                        self.proceedMove(newMove)

                elif status == 1: # Move a peca do time
                    self.setStatus(2)
                    self.setMessage(20)
                
            elif selectedField.getOccupant() == enabledPlayer: #Clicou na peça do mesmo time
                
                if status == 0: # X + selecionou peça certa
                    self.setMessage(10)
                    self.setStatus(1)

                else:  # X + devia ser para onde VAZIO
                    self.setMessage(11)

        
            elif selectedField.getOccupant() == self.neutron: #Clicou no Neutron
                self.setMessage(31)
            else: #Sobra apenas clicar no oponente 
                self.setMessage(30)


    def startMatch(self):
        # Comeca uma nova partida
        self.reset()
        if random.randint(1,2)==1:
            aMove = self.player1.enable()
            self.proceedMove(aMove)
        else:
            aMove = self.player2.enable()
            self.proceedMove(aMove)

    def click(self, line, column):
        # Realiza os processos ao jogador clicar em uma posicao
        if (self.getStatus()==-1):
            self.startMatch()
        else:
            aMove = move.Move(line, column)
            self.proceedMove(aMove)
    
    def reset(self):
        #Reinicia o tabuleiro com todas posicoes vazias
        for x in range(5):
            for y in range(5):
                self.fields[x][y].empty()
        self.player1.reset()
        self.player2.reset()
        self.initialPieces()
                
