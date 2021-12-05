#import abc
#class Player(metaclass=abc.ABCMeta):
class Player():
    def __init__(self):
        self.symbol = None    #int
        self.turn = False    #boll
        self.name = ''    #string

    #@abstractmethod
    def enable(self):
        pass

    def initialize(self, aName, aSymbol):
        self.symbol = aSymbol    #int
        self.name = aName        #string
        self.turn = False        #bool
        self.winner = False        #bool

    def reset(self):
        self.turn = False		


    def disable(self):
        self.turn = False
     
    def getSymbol(self):
        return self.symbol
     
    def getName(self):
        return self.name
    
     
    def getTurn(self):
        return self.turn