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
        self._neutron = neutron.Neutron()
        self._player1 = humanPlayer.HumanPlayer()
        self._player2 = humanPlayer.HumanPlayer()
        self._player1.initialize("Jogador Próton", 1)
        self._player2.initialize("Jogador Elétron", 2)
        self._matchStatus = -1
        self._statusMessage = None

        # Define as posicoes no "backend"

        self._fields = []  # tabuleiro
        self._neutronPosition = [2, 2]
        self._aMovePiece = None
        self._message = 1
        self._passedFirstMatch = False
        self.initialPieces()

    def getPassedFirstMatch(self):
        # Retorna bool caso ja passou a primeira jogada(onde nao controla neutron)
        return self._passedFirstMatch

    def setFirstMatch(self, boolean):
        # Define bool de primeira jogada
        self._passedFirstMatch = boolean

    def initialPieces(self):
        # Define as posicaos iniciais do tabuleiro
        for y in range(5):
            column = []
            for x in range(5):
                column.append(field.Field(None))
            self._fields.append(column)

        for i in range(5):
            self._fields[i][0] = field.Field(self._player1)
        for i in range(5):
            self._fields[i][4] = field.Field(self._player2)
        self._neutronPosition = [2, 2]
        self._fields[2][2] = field.Field(self._neutron)

    def getStatus(self):
        # Retorna o estado do jogo
        # -1 - antes de partida iniciar
        # 0 - vez  de selecionar a peca do time
        # 1 - vez de selecionar local vazio para onde mover a peca time
        # 2 - vez de selecionar local vazio para onde mover o  neutron
        return self._matchStatus

    def setStatus(self, value):
        # Define o estado do jogo
        self._matchStatus = value

    def getStatusMessage(self):
        # Retorna a mensagem de estado
        status = self.getStatus()
        jogador = (self.getEnabledPlayer().getName())

        if status == -1:
            self._statusMessage = "Clique para reiniciar o jogo!"
        elif status == 0:
            self._statusMessage = (jogador + " - Selecione a posição para mover o Neutron - status0")
        elif status == 1:
            self._statusMessage = (jogador + " - Selecione uma peça sua para mover - status1")
        elif status == 2:
            self._statusMessage = (jogador + " - Selecione a posição para mover sua peça - status2")
        elif status == 3:
            self._statusMessage = "Fim de jogo! - status3"
        else:
            self._statusMessage = status
        return self._statusMessage

    def setMessage(self, message):
        self._message = message

    def getMessage(self):
        message = self._message
        if message == 1:
            self._message = ""
        elif message == 2:
            self._message = "Local inválido. Jogue novamente"
        elif message == 3:
            self._message = "Movimento inválido. Jogue novamente"
        elif message == 91:
            self._message = "O Próton Venceu!"
        elif message == 92:
            self._message = "O Elétron Venceu!"
        return self._message

    def getField(self, aMove):
        # Retorna o estado da posicao indicada
        x = aMove.getLine() - 1
        y = aMove.getColumn() - 1
        return self._fields[x][y]

    def getEnabledPlayer(self):
        # Retorna o jogador da rodada
        if self._player1.getTurn():
            return self._player1
        else:
            return self._player2

    def getDisabledPlayer(self):
        # Retorna o jogador da proxima rodada
        if self._player1.getTurn():
            return self._player2
        else:
            return self._player1

    def getValue(self, x, y):
        # Retorna o tipo de peça de um campo
        if self._fields[x][y].occupied():
            value = (self._fields[x][y].getOccupant()).getSymbol()
        else:
            value = 0
        return value

    def moveNeutron(self, aMove):
        could_move = self.movePiece(aMove, None)
        return could_move

    def linearCheck(self, x_difference, y_difference, x_start, x_final, y_start, y_final):
        legit_linear = True
        list_0_to_4 = [0, 1, 2, 3, 4]
        if x_difference == 0 and y_difference > 0:
            for i in range(abs(y_difference)):  # Checa se o caminho esta livre
                if self._fields[x_start][y_start + i + 1].occupied():
                    legit_linear = False
                    break

            if legit_linear:
                for j in range(1, 4, 1):  # tenta mover a mais caso for casas vazias
                    try:
                        if  not self._fields[x_final][y_final + 1].occupied():
                            if y_final + 1 in list_0_to_4:
                                y_final = y_final + 1
                    except IndexError:
                        break

        elif x_difference == 0 and y_difference < 0:
            for i in range(abs(y_difference)):  # Checa se o caminho esta livre
                if self._fields[x_start][y_start - i - 1].occupied():
                    legit_linear = False
                    break

            if legit_linear:
                for j in range(1, 4, 1):  # tenta mover a mais caso for casas vazias
                    try:
                        if  not self._fields[x_final][y_final - 1].occupied():
                            if y_final - 1 in list_0_to_4:
                                y_final = y_final - 1
                    except IndexError:
                        break

        elif y_difference == 0 and x_difference > 0:
            for i in range(abs(x_difference)):  # Checa se o caminho esta livre
                if self._fields[x_start + 1 + i][y_start].occupied():
                    legit_linear = False
                    break

            if legit_linear:
                for j in range(1, 4, 1):  # tenta mover a mais caso for casas vazias
                    try:
                        if  not self._fields[x_final + 1][y_final].occupied():
                            if x_final + 1 in list_0_to_4:
                                x_final = x_final + 1
                    except IndexError:
                        break

        elif y_difference == 0 and x_difference < 0:
            for i in range(abs(x_difference)):  # Checa se o caminho esta livre
                if self._fields[x_start - 1 - i][y_start].occupied():
                    legit_linear = False
                    break

            if legit_linear:
                for j in range(1, 4, 1):  # tenta mover a mais caso for casas vazias
                    try:
                        if  not self._fields[x_final - 1][y_final].occupied():
                            if x_final - 1 in list_0_to_4:
                                x_final = x_final - 1
                    except IndexError:
                        break

        return legit_linear, x_final, y_final


    def movePiece(self, aMoveDestiny, player):
        if player:
            x_start = self._aMovePiece.getLine() - 1
            y_start = self._aMovePiece.getColumn() - 1
        else:
            x_start = self._neutronPosition[0]
            y_start = self._neutronPosition[1]

        x_final = aMoveDestiny.getLine() - 1
        y_final = aMoveDestiny.getColumn() - 1

        x_difference = x_final - x_start
        y_difference = y_final - y_start
        if x_difference == 0 or y_difference ==0: #Checa se o movimento linear é valido
            legit_linear, x_final, y_final = self.linearCheck(x_difference, y_difference, x_start, x_final, y_start, y_final)
            self.moveResults(player, legit_linear, x_start, x_final, y_start, y_final)
            return legit_linear

        if abs(x_difference) == abs(y_difference): #Checa se o movimento diagonal é valido
            legit_diagonal, x_final, y_final = self.moveDiagonal( x_difference, y_difference, x_start, x_final,y_start, y_final)
            self.moveResults(player, legit_diagonal, x_start, x_final,y_start, y_final)
            return legit_diagonal

        else:
            return False


    def moveDiagonal(self, x_difference, y_difference, x_start, x_final,y_start, y_final):
        legit_diagonal = True
        list_0_to_4 = [0, 1, 2, 3, 4]
        if x_difference > 0 and y_difference > 0:
            for i in range(abs(x_difference)):  # Checa se o caminho esta livre
                if self._fields[x_start + i + 1][y_start + i + 1].occupied():
                    legit_diagonal = False
                    break

            for j in range(1, 4, 1):
                try:
                    if not self._fields[x_final + 1][y_final + 1].occupied():
                        if x_final + 1 in list_0_to_4 and y_final + 1 in list_0_to_4:
                            x_final = x_final + 1
                            y_final = y_final + 1
                except IndexError:
                    break

        elif x_difference > 0 > y_difference:
            for i in range(abs(x_difference)):  # Checa se o caminho esta livre
                if self._fields[x_start + i + 1][y_start - i - 1].occupied():
                    legit_diagonal = False
                    break

            for j in range(1, 4, 1):
                try:
                    if not self._fields[x_final + 1][y_final - 1].occupied():
                        if x_final + 1 in list_0_to_4 and y_final - 1 in list_0_to_4:
                            x_final = x_final + 1
                            y_final = y_final - 1
                except IndexError:
                    break

        elif x_difference < 0 and y_difference > 0:  # MAIN
            for i in range(abs(x_difference)):  # Checa se o caminho esta livre
                if self._fields[x_start - i - 1][y_start + i + 1].occupied():
                    legit_diagonal = False
                    break

            for j in range(1, 4, 1):
                try:
                    if not self._fields[x_final - 1][y_final + 1].occupied():
                        if x_final - 1 in list_0_to_4 and y_final + 1 in list_0_to_4:
                            x_final = x_final - 1
                            y_final = y_final + 1
                except IndexError:
                    break

        elif x_difference < 0 and y_difference < 0:
            for i in range(abs(x_difference)):  # Checa se o caminho esta livre
                if self._fields[x_start - i - 1][y_start - i - 1].occupied():
                    legit_diagonal = False
                    break

            for j in range(1, 4, 1):
                try:
                    if not self._fields[x_final - 1][y_final - 1].occupied():
                        if x_final - 1 in list_0_to_4 and y_final - 1 in list_0_to_4:
                            x_final = x_final - 1
                            y_final = y_final - 1
                except IndexError:
                    break

        return legit_diagonal, x_final, y_final

    def moveResults(self, player, legit_move, x_start, x_final, y_start, y_final):
        if legit_move:
            self._fields[x_start][y_start].empty()
            if player:
                    self._aMovePiece = None
                    self._fields[x_final][y_final].setOccupant(player)
            else: # move o neutron
                    self._fields[x_final][y_final].setOccupant(self._neutron)
                    self._neutronPosition = [x_final, y_final]


    def checkWin(self):
        # Verifica se algum time venceu
        y_final = self._neutronPosition[1]
        if y_final == 0: # proton venceu
            self.setStatus(3)
            self.setMessage(91)

        if y_final == 4: # eletron venceu
            self.setStatus(3)
            self.setMessage(92)

    def moveStatus0(self, aMove, selectedField, status, enabledPlayer, disabledPlayer):
        # Move neutron
        if not selectedField.occupied():
            couldMove = self.moveNeutron(aMove)
            if couldMove:
                self.setStatus(1)
                self.setMessage(1)
                self.checkWin()
            else:
                self.setMessage(3)
        else:
            self.setMessage(2)

    def moveStatus1(self, aMove, selectedField, status, enabledPlayer, disabledPlayer):
        # Seleciona peça do time
        if selectedField.getOccupant() == enabledPlayer:

            self.setMessage(1)
            self.setStatus(2)
            self._aMovePiece = aMove
        else:
            self.setMessage(2)

    def moveStatus2(self, aMove, selectedField, status, enabledPlayer, disabledPlayer):
        # Move peça do time
        if not selectedField.occupied():
            couldMove = self.movePiece(aMove, enabledPlayer)
            if couldMove:
                self.setStatus(0)
                self.setMessage(1)
                self.setFirstMatch(True)
                enabledPlayer.disable()
                newMove = disabledPlayer.enable()
                if newMove.getLine() != 0:
                    self.proceedMove(newMove)
            else:
                self.setMessage(3)
        else:
            self.setMessage(2)

    def finishedMatchStatus3(self, *args):
        # Fim daa partidaa
        self.setStatus(-1)
        self.setMessage(1)

    def proceedMove(self, aMove):
        # Procede a jogada, e seleciona o tipo de jogada conforme o status
        selectedField = self.getField(aMove)
        enabledPlayer = self.getEnabledPlayer()
        disabledPlayer = self.getDisabledPlayer()
        status = self.getStatus()
        if status == -1:
            self.setStatus(0) if self.getPassedFirstMatch() else self.setStatus(1)
            self.setMessage(1)
        else:
            dict_methods = {0: self.moveStatus0, 1: self.moveStatus1, 2: self.moveStatus2, 3:self.finishedMatchStatus3}
            func = dict_methods[status]
            func_args = [aMove, selectedField, status, enabledPlayer, disabledPlayer]
            func(*func_args)


    def startMatch(self):
        # Comeca uma nova partida
        self.reset()
        self.setFirstMatch(False)
        if random.randint(1, 2) == 1:
            aMove = self._player1.enable()
            self.proceedMove(aMove)
        else:
            aMove = self._player2.enable()
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
                self._fields[x][y].empty()
        self._player1.reset()
        self._player2.reset()
        self.initialPieces()

