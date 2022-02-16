import move


class HumanPlayer():
    def __init__(self):
        self._symbol = None    #int
        self._turn = False    #boll
        self._name = ''    #string

    #@abstractmethod
    def enable(self):
        pass

    def initialize(self, aName, aSymbol):
        self._symbol = aSymbol    #int
        self._name = aName        #string
        self._turn = False        #bool
        self._winner = False        #bool

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
