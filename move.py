class Move:
    #Representa uma jogada, com as posicoes do tabuleiro dela
    def __init__(self, argLine, argColumn):
        self._line = argLine
        self._column = argColumn

    def getLine(self):
        return self._line  
    
    def getColumn(self):
        return self._column        
    
    def setValues (self, argLine, argColumn):
        self._line = argLine
        self._column = argColumn