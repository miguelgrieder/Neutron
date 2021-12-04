import player
import move

class HumanPlayer(player.Player):
    #Jogador humano, metodos principais herdados
    def __init__(self):
        super().__init__()

    def enable(self):
        self.turn = True
        return move.Move(0, 0)