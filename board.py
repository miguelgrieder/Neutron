import field
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


class Board:  # Realiza a gerencia real do tabuleiro "back-end"

    def __init__(self):
        # Define os jogadores
        super().__init__()
        self.neutron = neutron.Neutron()
        self.player1 = humanPlayer.HumanPlayer()
        self.player2 = humanPlayer.HumanPlayer()
        self.player1.initialize("Jogador Próton", 1)
        self.player2.initialize("Jogador Elétron", 2)
        self.matchStatus = -1

        # Define as posicoes no "backend"

        self.fields = []  # tabuleiro
        self.neutronPosition = [2, 2]
        self.aMovePiece = None
        self.message = 1
        self.passedFirstMatch = False
        self.initialPieces()

    def getPassedFirstMatch(self):
        # Retorna bool caso ja passou a primeira jogada(onde nao controla neutron)
        return self.passedFirstMatch

    def setFirstMatch(self, boolean):
        # Define bool de primeira jogada
        self.passedFirstMatch = boolean

    def initialPieces(self):
        # Define as posicaos iniciais do tabuleiro
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
        # Retorna o estado do jogo
        # -1 - antes de partida iniciar
        # 0 - vez  de selecionar a peca do time
        # 1 - vez de selecionar local vazio para onde mover a peca time
        # 2 - vez de selecionar local vazio para onde mover o  neutron
        return self.matchStatus

    def setStatus(self, value):
        # Define o estado do jogo
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

        if (message == 1):  # 1+ - status -1 , o
            self.message = ""
        elif (message == 2):
            self.message = ("Local vazio. Jogue novamente")

        elif (message == 10):  # 10+ - status 10
            self.message = ""
        elif (message == 11):
            self.message = ("Local incorreto. Jogue novamente")

        elif (message == 20):  # 20+ - status 20
            self.message = ""

        elif (message == 30):
            self.message = ("A peça clicada é do oponente! Jogue novamente")
        elif (message == 31):
            self.message = ("A peça clicada é o Neutron! Jogue novamente")
        elif (message == 32):
            self.message = ("")

        return self.message

    def getField(self, aMove):
        # Retorna o estado da posicao indicada
        x = aMove.getLine() - 1
        y = aMove.getColumn() - 1
        return self.fields[x][y]

    def getEnabledPlayer(self):
        # Retorna o jogador da rodada
        if self.player1.getTurn():
            return self.player1
        else:
            return self.player2

    def getDisabledPlayer(self):
        # Retorna o jogador da proxima rodada
        if self.player1.getTurn():
            return self.player2
        else:
            return self.player1

    def getValue(self, x, y):
        # Retorna o tipo de peça de um campo
        if (self.fields[x][y].occupied()):
            value = (self.fields[x][y].getOccupant()).getSymbol()
        else:
            value = 0
        return value

    def moveNeutron(self, aMove):
        x = self.neutronPosition[0]
        y = self.neutronPosition[1]
        self.fields[x][y].empty()

        x_final = aMove.getLine() - 1
        y_final = aMove.getColumn() - 1
        self.fields[x_final][y_final].setOccupant(self.neutron)
        self.neutronPosition = [x_final, y_final]

    def movePiece(self, aMoveDestiny, player):

        x_start = self.aMovePiece.getLine() - 1
        y_start = self.aMovePiece.getColumn() - 1

        x_final = aMoveDestiny.getLine() - 1
        y_final = aMoveDestiny.getColumn() - 1

        x_diference = x_final - x_start
        y_diference = y_final - y_start


        can_move_more, legit_diagonal, more_moves, x_diference, y_diference, x_start, x_final, y_start, y_final, on_limit = self.diagonalCheck(x_diference, y_diference, x_start, x_final, y_start, y_final)
        if legit_diagonal:
            can_move_more, legit_diagonal, more_moves, x_diference, y_diference, x_start, x_final, y_start, y_final, on_limit = self.moveMore(can_move_more, legit_diagonal, more_moves, x_diference, y_diference, x_start, x_final, y_start, y_final, on_limit)
            legit_diagonal = self.moveResults(player, legit_diagonal, x_start, x_final,y_start, y_final)
            return legit_diagonal
        else:
            return False


        #dict_diagonalCheck = self.diagonalCheck(x_diference, y_diference, x_start, x_final, y_start, y_final)
        #if dict_diagonalCheck['legit_diagonal']:
         #   dict_moreMove = self.moveMore()
         #   legit_diagonal = self.moveResults(**dict_moreMove.values())
         #   return legit_diagonal
        #else:
        #    return False



    def diagonalCheck(self, x_diference, y_diference, x_start, x_final,y_start, y_final):
        legit_diagonal = False
        on_limit = False
        more_moves = 0
        can_move_more = False
        if abs(x_diference) == abs(y_diference):
            legit_diagonal = True
            can_move_more = True
            on_limit = False
            more_moves = 0
            if x_diference > 0 and y_diference > 0:
                for i in range(abs(x_diference)):  # Checa se o caminho esta livre
                    if self.fields[x_start + i + 1][y_start + i + 1].occupied():
                        legit_diagonal = False
                        break

                for j in range(1, 4, 1):
                    try:
                        if not self.fields[x_final + 1][y_final + 1].occupied():
                            more_moves = j
                        else:
                            can_move_more = False
                    except:
                        can_move_more = False
                    finally:
                        if can_move_more:

                            if x_final + 1 not in [0, 1, 2, 3, 4]:
                                on_limit = True
                                break
                            if y_final + 1 not in [0, 1, 2, 3, 4]:
                                on_limit = True
                                break
                            if not on_limit:
                                x_final = x_final + 1
                                y_final = y_final + 1

        return can_move_more, legit_diagonal, more_moves, x_diference, y_diference, x_start, x_final,y_start, y_final, on_limit
        #return {'can_move_more': can_move_more, 'legit_diagonal': legit_diagonal, 'more_moves': more_moves, 'x_diference': x_diference,'y_diference': y_diference,
        #        'x_start': x_start, 'x_final': x_final,'y_start': y_start, 'y_final': y_final, 'on_limit': on_limit}

    def moveResults(self,player, legit_diagonal, x_start, x_final,y_start, y_final):
        if legit_diagonal:
            self.fields[x_start][y_start].empty()
            self.aMovePiece = None
            self.fields[x_final][y_final].setOccupant(player)
            return True
        else:
            return False

    def moveMore(self, can_move_more, legit_diagonal, more_moves, x_diference, y_diference, x_start, x_final,y_start, y_final, on_limit): #can_move_more, legit_diagonal, more_moves, x_diference, y_diference, x_start, x_final,y_start, y_final, on_limit
        if x_diference > 0 > y_diference:
            for i in range(abs(x_diference)):  # Checa se o caminho esta livre
                if self.fields[x_start + i + 1][y_start - i - 1].occupied():
                    legit_diagonal = False
                    break

            for j in range(1, 4, 1):
                try:
                    if not self.fields[x_final + 1][y_final - 1].occupied():
                        more_moves = j
                    else:
                        can_move_more = False
                except:
                    can_move_more = False
                finally:
                    if can_move_more:

                        if x_final + 1 not in [0, 1, 2, 3, 4]:
                            on_limit = True
                            break
                        if y_final - 1 not in [0, 1, 2, 3, 4]:
                            on_limit = True
                            break
                        if not on_limit:
                            x_final = x_final + 1
                            y_final = y_final - 1

        if x_diference < 0 and y_diference > 0:  # MAIN
            for i in range(abs(x_diference)):  # Checa se o caminho esta livre
                if self.fields[x_start - i - 1][y_start + i + 1].occupied():
                    legit_diagonal = False
                    break

            for j in range(1, 4, 1):
                try:
                    if not self.fields[x_final - 1][y_final + 1].occupied():
                        more_moves = j
                    else:
                        can_move_more = False
                except:
                    can_move_more = False
                finally:
                    if can_move_more:

                        if x_final - 1 not in [0, 1, 2, 3, 4]:
                            on_limit = True
                            break
                        if y_final + 1 not in [0, 1, 2, 3, 4]:
                            on_limit = True
                            break
                        if not on_limit:
                            x_final = x_final - 1
                            y_final = y_final + 1

        if x_diference < 0 and y_diference < 0:
            for i in range(abs(x_diference)):  # Checa se o caminho esta livre
                if self.fields[x_start - i - 1][y_start - i - 1].occupied():
                    legit_diagonal = False
                    break

            for j in range(1, 4, 1):
                try:
                    if not self.fields[x_final - 1][y_final - 1].occupied():
                        more_moves = j
                    else:
                        can_move_more = False
                except:
                    can_move_more = False
                finally:
                    if can_move_more:

                        if x_final - 1 not in [0, 1, 2, 3, 4]:
                            on_limit = True
                            break
                        if y_final - 1 not in [0, 1, 2, 3, 4]:
                            on_limit = True
                            break
                        if not on_limit:
                            x_final = x_final - 1
                            y_final = y_final - 1
        return can_move_more, legit_diagonal, more_moves, x_diference, y_diference, x_start, x_final, y_start, y_final, on_limit
        #return {'legit_diagonal': legit_diagonal, 'more_moves': more_moves, 'x_diference': x_diference, 'y_diference': y_diference,
        #        'x_start': x_start, 'x_final': x_final, 'y_start': y_start, 'y_final': y_final, 'on_limit': on_limit}

    def proceedMove(self, aMove):
        # Realiza a jogada, e testa qual condica
        selectedField = self.getField(aMove)
        enabledPlayer = self.getEnabledPlayer()
        disabledPlayer = self.getDisabledPlayer()
        status = self.getStatus()
        if status == -1:
            self.setStatus(0)
            self.setMessage(1)

        else:
            if not selectedField.occupied():  # CLIQUE EM LOCAL VAZIO
                if status == 0:  # x + na  vez selecionar peça time
                    self.setMessage(2)

                elif status == 2:  # move o neutron
                    self.moveNeutron(aMove)
                    enabledPlayer.disable()
                    newMove = disabledPlayer.enable()
                    self.setStatus(0)
                    self.setMessage(1)
                    if newMove.getLine() != 0:
                        self.proceedMove(newMove)

                elif status == 1:  # Move a peca do time
                    if self.getPassedFirstMatch():
                        couldMove = self.movePiece(aMove, enabledPlayer)
                        if couldMove:
                            self.setStatus(2)
                            self.setMessage(20)
                    else:  # Primeira rodada - não tem status 2 (neutron)
                        self.setFirstMatch(True)
                        couldMove = self.movePiece(aMove, enabledPlayer)
                        if couldMove:
                            enabledPlayer.disable()
                            newMove = disabledPlayer.enable()
                            self.setStatus(0)
                            self.setMessage(1)
                            if (newMove.getLine() != 0):
                                self.proceedMove(newMove)



            elif selectedField.getOccupant() == enabledPlayer:  # Clicou na peça do mesmo time

                if status == 0:  # X + selecionou peça certa
                    self.setMessage(10)
                    self.setStatus(1)
                    self.aMovePiece = aMove

                else:  # X + devia ser para onde VAZIO
                    self.setMessage(11)


            elif selectedField.getOccupant() == self.neutron:  # Clicou no Neutron
                self.setMessage(31)
            else:  # Sobra apenas clicar no oponente
                self.setMessage(30)

    def startMatch(self):
        # Comeca uma nova partida
        self.reset()
        self.setFirstMatch(False)
        if random.randint(1, 2) == 1:
            aMove = self.player1.enable()
            self.proceedMove(aMove)
        else:
            aMove = self.player2.enable()
            self.proceedMove(aMove)

    def click(self, line, column):
        # Realiza os processos ao jogador clicar em uma posicao
        if self.getStatus() == -1:
            self.startMatch()
        else:
            aMove = move.Move(line, column)
            self.proceedMove(aMove)

    def reset(self):
        # Reinicia o tabuleiro com todas posicoes vazias
        for x in range(5):
            for y in range(5):
                self.fields[x][y].empty()
        self.player1.reset()
        self.player2.reset()
        self.initialPieces()

