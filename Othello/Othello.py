import pygame



class Othello():
    #Note in this case 0 will represent an empty board. 1 will represent black (player 1) and 2 will represent white (player 2). Also an improvement to make it easier to switch between players would be to use -1 and 1.
    #This sets all the initial board positions. 
    def __init__(self):
        
        self.turn = 1
        self.player = 1
        self.board_change = False
        self.board = [
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,2,1,0,0,0],
            [0,0,0,1,2,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]
        ]
     #This will keep track of pieces currently on board {x=row,y=column}. Used to shorten the time spent finding available actions
        
    
    #the utility returns who won the game.
    def utility(self):
        
        player1 = 0
        player2 = 0
        for x in range(0,8):
            for y in range(0,8):
                if(self.board[x][y] == 1):
                    player1+=1
                elif(self.board[x][y] == 2):
                    player2+=1
        if(player1 > player2):
            return 1
        elif (player2 > player1):
            return -1
        else:
            return 0

    #This function prints the board. This is used for debugging purposes.
    def print_board(self):

        for x in range (0,8):
            for y in range (0,8):
                print(self.board[x][y], end = " ")
            print()


    #This function calculates all the available moves a player or ai can make. It also keeps track the path of each of the move to allow for easy flipping of the pieces.
    # Essentially it returns a 2d list which details not only a valid move but the pieces that need to flip as it pushes the pieces that need to flip onto the list. 
    # The 'valid move' is located at the end of each row as it is always appended last.
    def actions(self, state):
        available_moves = []
        for i in range(0,8):
            for j in range(0,8):

            
                if(state[i][j] == self.player):
                    #check upwards:
                    if(i != 0 and state[i-1][j] != self.player and state[i-1][j] != 0):
                        path = []
                        for y in range(i-1, -1, -1):
                            if(state[y][j] == self.player):
                                break
                            elif (state[y][j] == 0):
                                path.append((y,j))
                                available_moves.append(path)
                                break
                            path.append((y, j))
            
                    #check right:
                    if(j != 7 and state[i][j+1] != self.player and state[i][j+1] != 0):
                        path = []
                        for y in range(j+1, 8):
                            if(state[i][y] == self.player):
                                break
                            elif (state[i][y] == 0):
                                path.append((i,y))
                                available_moves.append(path)
                                break
                            path.append((i,y))
            
                    # check down
                    if(i != 7 and state[i+1][j] != self.player and state[i+1][j] != 0):
                        path = []
                        for y in range(i+1, 8):
                            if(state[y][j] == self.player):
                                break
                            elif (state[y][j] == 0):
                                path.append((y,j))
                                available_moves.append(path)
                                break
                            path.append((y, j))
            
                    #check left
                    if (i != 0 and state[i][j-1] != self.player and state[i][j-1] != 0):
                        path = []
                        for y in range(j-1, -1, -1):
                            if(state[i][y] == self.player):
                                break
                            if(state[i][y] == 0):
                                path.append((i,y))
                                available_moves.append(path)
                                break
                            path.append((i,y))
            
                    #check up-right
                    if (i != 0 and j != 7 and state[i-1][j+1] != self.player and state[i-1][j+1] != 0 ):
                        path = []
                        up = i - 1
                        right = j + 1

                        while (up != -1 and right != 8):
                            if state[up][right] == self.player:
                                break
                            if state[up][right] == 0:
                                path.append((up,right))
                                available_moves.append(path)
                                break
                            path.append((up, right))
                            up = up - 1
                            right = right + 1
            
                    #check down right
                    if (i != 7 and j != 7 and state[i+1][j+1] != self.player and state[i+1][j+1] != 0 ):
                        path = []
                        down = i + 1
                        right = j + 1

                        while (down != 8 and right != 8):
                            if state[down][right] == self.player:
                                break
                            if state[down][right] == 0:
                                path.append((down, right))
                                available_moves.append(path)
                                break
                            path.append((down, right))
                            down = down + 1
                            right = right + 1
                    # check down left
                    if (i != 7 and j != 0 and state[i+1][j-1] != self.player and state[i+1][j-1] != 0):
                        path = []
                        down = i + 1 
                        left = j - 1

                        while (down != 8 and left != -1):
                            if state[down][left] == self.player:
                                break
                            if state[down][left] == 0:
                                path.append((down, left))
                                available_moves.append(path)
                                break
                            path.append((down, left))
                            down = down + 1
                            left = left - 1

                    #check up left
                    if (i != 0 and j != 0 and state[i-1][j-1] != self.player and state[i-1][j-1] != 0):
                        path = []
                        up = i - 1
                        left = j - 1

                        while (up != -1 and left != -1):
                            if state[up][left] == self.player:
                                break
                            if state[up][left] == 0:
                                path.append((up, left))
                                available_moves.append(path)
                                break
                            path.append((up, left))
                            up = up - 1
                            left = left - 1

        return available_moves
    
    #returns the number of black pieces. Used for the victory screen.
    def total_black_piece(self, state):
        count = 0
        for x in range(0,8):
            for y in range(0,8):
                if(state[x][y] == 1):
                    count = count + 1
        return count

    #return the total number of white pieces.
    def total_white_piece(self, state):
        count = 0
        for x in range(0,8):
            for y in range(0,8):
                if(state[x][y] == 2):
                    count = count + 1
        return count
    
    #checks to see if we are at a terminal state. 
    def terminal_test(self, state):
        if (self.player == 1):
            
            if(len(self.actions(state)) == 0):
                self.player = 2
                if (len(self.actions(state)) == 0):
                    return True
        elif (self.player == 2):
            if(len(self.actions(state)) == 0):
                self.player = 1
                if (len(self.actions(state)) == 0):
                    return True
        return False

    #This function is used to return the result of a move. Essentially it does the job of turning pieces that need to be flipped and placing the new piece down.
    def result(self, x_position, y_position, state):
        
        piece_added = False
        if (self.player == 1):
            for x in self.actions(state):
                if (x[-1] == (y_position,x_position)):
                    for y in x:
                        state[y[0]][y[1]] = 1
                    piece_added = True
                    self.board_change = True
            
        
        elif (self.player == 2):
            for x in self.actions(state):
                if (x[-1] == (y_position,x_position)):
                    for y in x:
                        state[y[0]][y[1]] = 2
                    piece_added = True
                    self.board_change = True

        if(self.board_change == True or len(self.actions(state)) == 0):
            if(self.player == 1):
                self.player = 2
            elif(self.player == 2):
                self.player = 1
        return state


    # This is a advanced evaluation function. Essentially this determines how good having a piece on the board at any point of time. This does make
    # the ai try to gain the corners more though even if it isn't the best move at the time.
    def advanced_evaluation(self, state):
        evaluation = 0
        board2 =  [ 
            [1, -0.25, 0.1, 0.05, 0.05, 0.1, -0.25, 1],
            [-0.25, -0.25, 0.01, 0.01, 0.01, 0.01, -0.25, -0.25],
            [0.1, 0.01, 0.05, 0.02, 0.02, 0.05, 0.01, 0.1],
            [0.05, 0.01, 0.02, 0.01,0.01,0.02,0.01,0.05],
            [0.05, 0.01, 0.02, 0.01,0.01,0.02,0.01,0.05],
            [0.1, 0.01, 0.05, 0.02, 0.02, 0.05, 0.01, 0.1],
            [-0.25, -0.25, 0.01, 0.01, 0.01, 0.01, -0.25, -0.25],
            [1, -0.25, 0.1, 0.05, 0.05, 0.1, -0.25,1 ]
        ]

        for x in range(0,8):
            for y in range(0,8):

                if (state[x][y] == 2):
                    evaluation += board2[x][y]
                elif (state[x][y] == 1):
                    evaluation -= board2[x][y]
        return evaluation

    #this is a much simpler function that just tells the ai to make the move that leads to the most captured pieces. This tended to make the ai too easy to put up a decent fight.
    #other ideas for this would be to yield extra points for certain positions similar to the advanced_evaluation function.
    def evaluation (self, state):
        return self.total_white_piece(state) - self.total_black_piece(state)

      


        
                    




                    
      


   
        