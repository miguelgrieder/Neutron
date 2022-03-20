import move


class HumanPlayer():
    def __init__(self):
        self._symbol = None    #int
        self._turn = None    #boll
        self._name = ''    #string

    def initialize(self, aName, aSymbol):
        self._symbol = aSymbol    #int
        self._name = aName        #string
        self._turn = False        #bool

    def reset(self):
        self._turn = False		

    def disable(self):
        self._turn = False
     
    def getSymbol(self):
        return self._symbol
     
    def getName(self):
        return self._name
    
    def getTurn(self):
        return self._turn

    def enable(self):
        self._turn = True
        return move.Move(0, 0)
