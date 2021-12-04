class Position:
    #Representa uma posicao do tabuleiro
    def __init__(self, player):
        self.setOccupant(player)
     
    def occupied(self):
        return (self.occupant != None)
     
    def setOccupant(self, aPlayer):
        self.occupant = aPlayer
     
    def getOccupant(self):
        return self.occupant
     
    def empty(self):
        self.occupant = None