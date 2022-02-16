class Field:
    # Representa uma posicao do tabuleiro
    def __init__(self, player):
        self.setOccupant(player)

    def occupied(self):
        return (self._occupant is not None)

    def setOccupant(self, aPlayer):
        self._occupant = aPlayer

    def getOccupant(self):
        return self._occupant

    def empty(self):
        self._occupant = None
