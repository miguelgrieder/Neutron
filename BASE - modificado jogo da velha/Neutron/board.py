import position
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
        self.player1=humanPlayer.HumanPlayer()
        self.player2=humanPlayer.HumanPlayer()
        self.player1.initialize("Jogador Vermelho", 1)
        self.player2.initialize("Jogador Branco", 2)
        self.matchStatus = 1
        #Define as posicoes no "backend"
        self.positions=[]
        self.initialPieces()
        
        
    def initialPieces(self):
        for y in range(5):
            column = []
            for x in range(5):
                if y == 0:                
                    column.append(position.Position(self.player1))
                elif y == 4:
                    column.append(position.Position(self.player2))
                else:
                    column.append(position.Position(None))
                self.positions.append(column)
        self.positions[2][2] = position.Position(neutron.Neutron())

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
        self.initialPieces()
        self.setStatus(1)

    
        
    
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

    def setMessage(self, text):
        self.message = text

    def getMessage(self):
        return self.message

    

    def getState(self):

        # Retorna a mensagem do estado
        if (self.getStatus() == 1): 
            self.setMessage("Clique em qualquer posição para iniciar")
        elif (self.getStatus() == 2):
            self.setMessage((self.getEnabledPlayer()).getName() + " deve selecionar uma peça")    
        elif (self.getStatus() == 3): 
            self.setMessage("Local vazio - jogue novamente")
        elif (self.getStatus() == 6): 
            self.setMessage((self.getEnabledPlayer()).getName() + " deve selecionar para onde mover")
        elif (self.getStatus() == 5): 
            self.setMessage("A partida terminou empatada")
        elif (self.getStatus() == 4): 
            self.setMessage("A peça clicada é do oponente!")

        return self.getMessage()

    def getValue(self):
        for x in range(5):
            for y in range(5):
                if (self.positions[x][y].occupied()):
                    value = (self.positions[x][y].getOccupant()).getSymbol()        
                else:
                    value = 0
        print(value)
        return value




    def proceedMove(self, aMove):
        #Realiza a jogada, e testa qual condica
        selectedPosition = self.getPosition(aMove)
        if selectedPosition.occupied():
            print('Clique em local vazio!')
            self.setStatus(3)    #Local vazio
        if True:
            print('Clique em peça mesmo time')
            enabledPlayer = self.getEnabledPlayer()
            disabledPlayer = self.getDisabledPlayer()
            selectedPosition.setOccupant(enabledPlayer)

            self.setStatus(6)
            #selecionar para onde mover
            newState = self.getState()
            enabledPlayer.disable()
            newMove = disabledPlayer.enable()
            if (newMove.getLine()!=0):
                self.proceedMove(newMove)
        else:
            print('Clique em peça do oponente!')
            self.setStatus(6)    #Local ocupado pelo oponente

        #Jogada regular, testar resultado
            



    def startMatch(self):
        # Comeca uma nova partida
        self.reset()
        self.setStatus(2)
        if random.randint(1,2)==1:
            self.player1.enable()
        else:
            aMove = self.player2.enable()
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
                
