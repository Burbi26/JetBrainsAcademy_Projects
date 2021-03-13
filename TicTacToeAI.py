import random

state = 1
coord = []
count = [0, 0]


#this class includes all the methods for the Tic-Tac-Toe fame
class Game:
    def init(self):
        global coord
        global count
        coord = "_________"
        coord.split()
        for x in coord:
            if x == "O":
                count[0] += 1
        for x in coord:
            if x == "X":
                count[1] += 1
        coord = [[coord[0], coord[1], coord[2]], [coord[3], coord[4], coord[5]], [coord[6], coord[7], coord[8]]]
    
    #this method prints the current state of the game in the console
    def print_coord(self):
        global coord
        print("""---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------""".format(coord[0][0], coord[0][1], coord[0][2], coord[1][0], coord[1][1], coord[1][2], coord[2][0], coord[2][1], coord[2][2]))

    #this method verifies the coordinates of a move and stores the value if it's valid
    def check_coordinates(self, checkInput):
        checkInput = checkInput.split(' ')
        if len(checkInput) > 2:
            return 0
        try:
            checkInput[0] = int(checkInput[0])
            checkInput[1] = int(checkInput[1])
        except:
            print("You should enter numbers!")
            return 0
        if checkInput[0] > 3 or checkInput[1] > 3 or checkInput[0] < 1 or checkInput[1] < 1:
            print("Coordinates should be from 1 to 3!")
            return 0
        global coord
        if coord[checkInput[0] - 1][checkInput[1] - 1] == "X" or coord[checkInput[0] - 1][checkInput[1] - 1] == "O":
            print("This cell is occupied! Choose another one!")
            return 0
        if count[0] == count[1]:
            coord[checkInput[0] - 1][checkInput[1] - 1] = "X"
            count[1] += 1
        else:
            coord[checkInput[0] - 1][checkInput[1] - 1] = "O"
            count[0] += 1
        return 1
    
    #this method takes the user's move
    def user_input(self):
        print("Enter the coordinates:")
        userInput = input()
        while self.check_coordinates(userInput) == 0:
            userInput = input()
        self.print_coord()
    
    #this method verifies if the game is finished and returns the results
    def check_victory(self):
        global coord
        global count
        for x in range(0, 3):
            if coord[x][0] == coord[x][1] and coord[x][1] == coord[x][2]:
                if coord[x][0] == "X":
                    return 2
                elif coord[x][0] == "O":
                    return 3
            if coord[0][x] == coord[1][x] and coord[0][x] == coord[2][x]:
                if coord[0][x] == "X":
                    return 2
                elif coord[0][x] == "O":
                    return 3
        if coord[0][0] == coord[1][1] and coord[1][1] == coord[2][2]:
            if coord[1][1] == "X":
                return 2
            elif coord[1][1] == "O":
                return 3
        if coord[0][2] == coord[1][1] and coord[1][1] == coord[2][0]:
            if coord[1][1] == "X":
                return 2
            elif coord[1][1] == "O":
                return 3
        for i in range(0, 3):
            for j in range(0, 3):
                if coord[i][j] == "_":
                    return 0
        return 1
    
    #this method prints the result of the game in the console
    def print_result(self, result):
        if result == 1:
            print("Draw")
            print()
        elif result == 2:
            print("X wins")
            print()
        elif result == 3:
            print("O wins")
            print()
    
    #this method takes the user's input and tells the main function which type of game to run 
    def check_state(self):
        type = 0
        gameCommand = input("Input command:")
        if gameCommand == "exit":
            return type
        else:
            try:
                gameType = gameCommand.split(' ')
                if gameType[0] == "start":
                    if gameType[1] == "user":
                        type += 1
                    elif gameType[1] == "easy":
                        type += 2
                    elif gameType[1] == "medium":
                        type += 3
                    elif gameType[1] == "hard":
                        type += 4
                    if gameType[2] == "user":
                        type += 10
                    elif gameType[2] == "easy":
                        type += 20
                    elif gameType[2] == "medium":
                        type += 30
                    elif gameType[2] == "hard":
                        type += 40
                    return type
                else:
                    print("Bad parameters!")
                    type += 1
                    return type
            except:
                print("Bad parameters!")
                type += 1
                return type
    
    #this method runs the easiest computer difficulty which makes random moves
    def easyAI(self):
        print("Making move level \"easy\"")
        easyInput = str(random.randint(1, 3)) + " " + str(random.randint(1, 3))
        while self.check_coordinates(easyInput) == 0:
            easyInput = str(random.randint(1, 3)) + " " + str(random.randint(1, 3))
        self.print_coord()
    
    #this method rune the intermediate difficulty which wins or denies a win if it can or makes random moves
    def mediumAI(self):
        print("Making move level \"medium\"")
        moveFound = 0
        global count
        global coord
        if moveFound == 0:
            for x in range(0, 3):
                if coord[x][0] == coord[x][1] and moveFound == 0 and coord[x][0] != "_":
                    mediumInput = "{} 3".format(x+1)
                    if self.check_coordinates(mediumInput) == 1:
                        if self.check_victory() == 1:
                            moveFound = 1
                        else:
                            coord[x][2] = "_"
                            if count[0] == count[1]:
                                count[0] -= 1
                            else:
                                count[1] -= 1
                if coord[x][1] == coord[x][2] and moveFound == 0 and coord[x][1] != "_":
                    mediumInput = "{} 1".format(x+1)
                    if self.check_coordinates(mediumInput) == 1:
                        if self.check_victory() == 1:
                            moveFound = 1
                        else:
                            coord[x][0] = "_"
                            if count[0] == count[1]:
                                count[0] -= 1
                            else:
                                count[1] -= 1
                if coord[x][0] == coord[x][2] and moveFound == 0 and coord[x][0] != "_":
                    mediumInput = "{} 2".format(x+1)
                    if self.check_coordinates(mediumInput) == 1:
                        if self.check_victory() == 1:
                            moveFound = 1
                        else:
                            coord[x][1] = "_"
                            if count[0] == count[1]:
                                count[0] -= 1
                            else:
                                count[1] -= 1
                if coord[0][x] == coord[1][x] and moveFound == 0 and coord[0][x] != "_":
                    mediumInput = "3 {}".format(x+1)
                    if self.check_coordinates(mediumInput) == 1:
                        if self.check_victory() == 1:
                            moveFound = 1
                        else:
                            coord[2][x] = "_"
                            if count[0] == count[1]:
                                count[0] -= 1
                            else:
                                count[1] -= 1
                if coord[1][x] == coord[2][x] and moveFound == 0 and coord[1][x] != "_":
                    mediumInput = "1 {}".format(x+1)
                    if self.check_coordinates(mediumInput) == 1:
                        if self.check_victory() == 1:
                            moveFound = 1
                        else:
                            coord[0][x] = "_"
                            if count[0] == count[1]:
                                count[0] -= 1
                            else:
                                count[1] -= 1
                if coord[0][x] == coord[2][x] and moveFound == 0 and coord[0][x] != "_":
                    mediumInput = "2 {}".format(x+1)
                    if self.check_coordinates(mediumInput) == 1:
                        if self.check_victory() == 1:
                            moveFound = 1
                        else:
                            coord[1][x] = "_"
                            if count[0] == count[1]:
                                count[0] -= 1
                            else:
                                count[1] -= 1
            if coord[0][0] == coord[1][1] and moveFound == 0 and coord[0][0] != "_":
                mediumInput = "3 3"
                if self.check_coordinates(mediumInput) == 1:
                    if self.check_victory() == 1:
                        moveFound = 1
                    else:
                        coord[2][2] = "_"
                        if count[0] == count[1]:
                            count[0] -= 1
                        else:
                            count[1] -= 1
            if coord[0][0] == coord[2][2] and moveFound == 0 and coord[0][0] != "_":
                mediumInput = "2 2"
                if self.check_coordinates(mediumInput) == 1:
                    if self.check_victory() == 1:
                        moveFound = 1
                    else:
                        coord[1][1] = "_"
                        if count[0] == count[1]:
                            count[0] -= 1
                        else:
                            count[1] -= 1
            if coord[2][2] == coord[1][1] and moveFound == 0 and coord[2][2] != "_":
                mediumInput = "1 1"
                if self.check_coordinates(mediumInput) == 1:
                    if self.check_victory() == 1:
                        moveFound = 1
                    else:
                        coord[0][0] = "_"
                        if count[0] == count[1]:
                            count[0] -= 1
                        else:
                            count[1] -= 1
            if coord[0][2] == coord[1][1] and moveFound == 0 and coord[0][2] != "_":
                mediumInput = "3 1"
                if self.check_coordinates(mediumInput) == 1:
                    if self.check_victory() == 1:
                        moveFound = 1
                    else:
                        coord[2][0] = "_"
                        if count[0] == count[1]:
                            count[0] -= 1
                        else:
                            count[1] -= 1
            if coord[2][0] == coord[1][1] and moveFound == 0 and coord[2][0] != "_":
                mediumInput = "1 3"
                if self.check_coordinates(mediumInput) == 1:
                    if self.check_victory() == 1:
                        moveFound = 1
                    else:
                        coord[0][2] = "_"
                        if count[0] == count[1]:
                            count[0] -= 1
                        else:
                            count[1] -= 1
            if coord[2][0] == coord[0][2] and moveFound == 0 and coord[2][0] != "_":
                mediumInput = "2 2"
                if self.check_coordinates(mediumInput) == 1:
                    if self.check_victory() == 1:
                        moveFound = 1
                    else:
                        coord[1][1] = "_"
                        if count[0] == count[1]:
                            count[0] -= 1
                        else:
                            count[1] -= 1
        if moveFound == 0:
            for x in range(0, 3):
                if coord[x][0] == coord[x][1] and moveFound == 0 and coord[x][0] != "_":
                    mediumInput = "{} 3".format(x+1)
                    if self.check_coordinates(mediumInput) == 1:
                        moveFound = 1
                if coord[x][1] == coord[x][2] and moveFound == 0 and coord[x][1] != "_":
                    mediumInput = "{} 1".format(x+1)
                    if self.check_coordinates(mediumInput) == 1:
                        moveFound = 1
                if coord[x][0] == coord[x][2] and moveFound == 0 and coord[x][0] != "_":
                    mediumInput = "{} 2".format(x+1)
                    if self.check_coordinates(mediumInput) == 1:
                        moveFound = 1
                if coord[0][x] == coord[1][x] and moveFound == 0 and coord[0][x] != "_":
                    mediumInput = "3 {}".format(x+1)
                    if self.check_coordinates(mediumInput) == 1:
                        moveFound = 1
                if coord[1][x] == coord[2][x] and moveFound == 0 and coord[1][x] != "_":
                    mediumInput = "1 {}".format(x+1)
                    if self.check_coordinates(mediumInput) == 1:
                        moveFound = 1
                if coord[0][x] == coord[2][x] and moveFound == 0 and coord[0][x] != "_":
                    mediumInput = "2 {}".format(x+1)
                    if self.check_coordinates(mediumInput) == 1:
                        moveFound = 1
            if coord[0][0] == coord[1][1] and moveFound == 0 and coord[0][0] != "_":
                mediumInput = "3 3"
                if self.check_coordinates(mediumInput) == 1:
                    moveFound = 1
            if coord[0][0] == coord[2][2] and moveFound == 0 and coord[0][0] != "_":
                mediumInput = "2 2"
                if self.check_coordinates(mediumInput) == 1:
                    moveFound = 1
            if coord[2][2] == coord[1][1] and moveFound == 0 and coord[2][2] != "_":
                mediumInput = "1 1"
                if self.check_coordinates(mediumInput) == 1:
                    moveFound = 1
            if coord[0][2] == coord[1][1] and moveFound == 0 and coord[0][2] != "_":
                mediumInput = "3 1"
                if self.check_coordinates(mediumInput) == 1:
                    moveFound = 1
            if coord[2][0] == coord[1][1] and moveFound == 0 and coord[2][0] != "_":
                mediumInput = "1 3"
                if self.check_coordinates(mediumInput) == 1:
                    moveFound = 1
            if coord[2][0] == coord[0][2] and moveFound == 0 and coord[2][0] != "_":
                mediumInput = "2 2"
                if self.check_coordinates(mediumInput) == 1:
                    moveFound = 1
        if moveFound == 0:
            mediumInput = str(random.randint(1, 3)) + " " + str(random.randint(1, 3))
            while self.check_coordinates(mediumInput) == 0:
                mediumInput = str(random.randint(1, 3)) + " " + str(random.randint(1, 3))
        self.print_coord()
    
    #this is the maximing method for the MinMax algorithm
    def max(self):
        maxv = -2
        x = None
        y = None
        result = self.check_victory()
        if result == 2:
            return -1, 0, 0
        elif result == 3:
            return 1, 0, 0
        elif result == 1:
            return 0, 0, 0
        for i in range(0, 3):
            for j in range(0, 3):
                if coord[i][j] == "_":
                    coord[i][j] = "O"
                    m, min_i, min_j = self.min()
                    if m > maxv:
                        maxv = m
                        x = i
                        y = j
                    coord[i][j] = "_"
        return maxv, x, y
    
    #this is the minimizing method for the MinMax algorithm
    def min(self):
        minv = 2
        x = None
        y = None
        result = self.check_victory()
        if result == 2:
            return -1, 0, 0
        elif result == 3:
            return 1, 0, 0
        elif result == 1:
            return 0, 0, 0
        for i in range(0, 3):
            for j in range(0, 3):
                if coord[i][j] == "_":
                    coord[i][j] = "X"
                    m, max_i, max_j = self.max()
                    if m < minv:
                        minv = m
                        x = i
                        y = j
                    coord[i][j] = "_"
        return minv, x, y
    
    #this is the hardest computer difficulty which makes the most optimal move everytime using MinMax algorithm
    #users can't win at this difficulty, they can only draw or lose
    def hardAI(self, player1):
        print("Making move level \"hard\"")
        if player1 == 4:
            m, row, col = self.min()
            self.check_coordinates(str(row + 1) + " " + str(col + 1))
        else:
            m, row, col = self.max()
            self.check_coordinates(str(row + 1) + " " + str(col + 1))
        self.print_coord()
    
    #this is the main method for running the game
    def running_game(self, type):
        self.print_coord()
        victory = 0
        player1 = type % 10
        player2 = int(type / 10)
        while victory == 0:
            if player1 == 1:
                self.user_input()
            elif player1 == 2:
                self.easyAI()
            elif player1 == 3:
                self.mediumAI()
            elif player1 == 4:
                self.hardAI(player1)
            victory = self.check_victory()
            self.print_result(victory)
            if victory == 0:
                if player2 == 1:
                    self.user_input()
                elif player2 == 2:
                    self.easyAI()
                elif player2 == 3:
                    self.mediumAI()
                elif player2 == 4:
                    self.hardAI(player1)
                victory = self.check_victory()
                self.print_result(victory)
        self.reset_board()
        return 1
    
    #this method set the atributes for a new game
    def reset_board(self):
        global coord
        global count
        coord = "_________"
        coord.split()
        coord = [[coord[0], coord[1], coord[2]], [coord[3], coord[4], coord[5]], [coord[6], coord[7], coord[8]]]
        count = [0, 0]

game = Game()
game.init()
while state != 0:
    state = game.check_state()
    while state > 1:
        state = game.running_game(state)
