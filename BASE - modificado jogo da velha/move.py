class Move:
    def __init__(self, argLine, argColumn):
        self.line = argLine
        self.column = argColumn

    def getLine(self):
        return self.line  
    
    def getColumn(self):
        return self.column        
    
    def setValues (self, argLine, argColumn):
        self.line = argLine
        self.column = argColumn