import pygame, sys, time, math
import Othello
import numpy as np
import copy



# This function calls pygame to exit the display and then exit pygame and end the program. The pygame.quit() part is in case pygame.display.quit() doesn't work so its sort of a safety precaution.
def quit():
    pygame.display.quit()
    pygame.quit()
    sys.exit()

TILE_SIZE = 75
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255, 255, 255)


#This is the board class which will handle the GUI aspect of the prgram
class Othello_Board(object):

    #When the board is created the option for ai is set to none as the user hasn't indicated whether to create it or not. 
    def __init__(self):
        self.ai = None
        self.pieces = {}
        #keeps track of what key is currently being held down.
        #this key will be removed when the key is let go.
        self.keys_pressed_down = list()
        self.game = Othello.Othello()

    # When the game start up several things need to occur. First the screen size needs to be set, a caption for Othello needs to be made and then the board needs to be created.
    def gameStartUp(self):
        pygame.init()

        # Sets the screen to be x width and y height
        self.surface = pygame.display.set_mode((600, 600))
        #Sets the header of the pygame program.
        pygame.display.set_caption('Othello')
        #This will fill the screen with the color green. As Othello is played on a green board.
        self.surface.fill((0,255,0))
        #The next set of lines is what draws the black lines onto the board.
        #The function pygame.draw.line takes this parameter (surface to be drawn on, color (rgb format), where the line should start, where the line should end, and the thickness of the line)
        pygame.draw.line(self.surface, (0,0,0), (0,75), (600,75), 2)
        pygame.draw.line(self.surface, (0,0,0), (0,150),(600,150),2)
        pygame.draw.line(self.surface, (0,0,0), (0,225), (600,225), 2)
        pygame.draw.line(self.surface, (0,0,0), (0,300), (600,300), 2)
        pygame.draw.line(self.surface, (0,0,0), (0,375), (600,375), 2)
        pygame.draw.line(self.surface, (0,0,0), (0,450), (600,450), 2)
        pygame.draw.line(self.surface, (0,0,0), (0,525), (600,525), 2)
        pygame.draw.line(self.surface, (0,0,0), (75,0), (75,600), 2)
        pygame.draw.line(self.surface, (0,0,0), (150,0), (150,600), 2)
        pygame.draw.line(self.surface, (0,0,0), (225,0), (225,600), 2)
        pygame.draw.line(self.surface, (0,0,0), (300,0), (300,600), 2)
        pygame.draw.line(self.surface, (0,0,0), (375,0), (375,600), 2)
        pygame.draw.line(self.surface, (0,0,0), (450,0), (450,600), 2)
        pygame.draw.line(self.surface, (0,0,0), (525,0), (525,600), 2)
        #This function creates an object to keep track of the time taken.
        self.clock = pygame.time.Clock()

        #after the screen and board is created we need to draw the pieces onto the board
        self.draw_board()  


    #The goal of this function is to create a starting screen for the Othello game board. Essentially this will create a rectangle set to hold text to inform the players of the options for the game
    # pygame.font.SysFont is used to set the font style and the font size
    # font.render is used to render a string statement into your desired font size, and allows you to set the color of you text
    #.get_rect() allows you to create a text box to hold your text and allows you to position where the text should go.
    #surface.blit allows you to display an object onto the screen without drawing over it
    def starting_screen(self):
        text = "Welcome to Othello:"
        font = pygame.font.SysFont('Helvetica', 36)
        text = font.render(text, 1, (255, 215, 0))
        textbox = text.get_rect()
        textbox.topleft = ((300+50)//2,300//2)
        text2 = "I) Player Vs. Ai = Ctrl+a"
        text2 = font.render(text2, 1, (255, 215, 0))
        textbox2 = text.get_rect()
        textbox2.topleft = (120,200)
        text3 = "II) Player Vs. Player = Ctrl+p"
        text3 = font.render(text3, 1, (255, 215, 0))
        textbox3 = text.get_rect()
        textbox3.topleft = (120,270)
        text4 = "III) Exit = Ctrl+q"
        text4 = font.render(text4, 1, (255, 215, 0))
        textbox4 = text.get_rect()
        textbox4.topleft = (120,340)

        pygame.draw.rect(self.surface, (105,105,105, 128), (100,300//2, 400, 300), 0)
        self.surface.blit(text,textbox)
        self.surface.blit(text2,textbox2)
        self.surface.blit(text3, textbox3)
        self.surface.blit(text4, textbox4)
        

    #This is similar to starting screen except it's set to display who won the game, how many tiles each color took over, and displays information in case they want to exit or start a new game.
    def victory_screen(self, text, text2, font, font2, surface, x, y):
        text = font.render(text, 1, (255,215,0))
        textbox = text.get_rect()
        textbox.topleft = ((x+100)//2,y//2)
        text2 = font2.render(text2, 1, (255,215,0))
        textbox2 = text.get_rect()
        textbox2.topleft = ((x + 50)//2,(y+100)//2)
        text3 = "I) New Game = Ctrl+n"
        text3 = font.render(text3, 1, (255, 215, 0))
        textbox3 = text.get_rect()
        textbox3.topleft = ((x + 50)//2,240)
        text4 = "II) Exit = Ctrl+q"
        text4 = font.render(text4, 1, (255, 215, 0))
        textbox4 = text.get_rect()
        textbox4.topleft = ((x + 50)//2,300)

        pygame.draw.rect(self.surface, (105,105,105, 128), (100,300//2, 400, 300), 0)
        surface.blit(text, textbox)
        surface.blit(text2, textbox2)
        surface.blit(text3, textbox3)
        surface.blit(text4, textbox4)
    

    #This functions job is to draw the board onto the screen determine if the game is at a terminal and if so display the victor, and finally to display the available moves to the player.
    def draw_board(self):
        
        #This checks each tile on the board to see if a piece is on it. If so it will draw the corresponding piece onto the board using pygames draw circle function.
        for x in range(0,8):
            for y in range(0,8):
                if (self.game.board[x][y] == 1):
                    pygame.draw.circle(self.surface, BLACK, ((y * 75) +37 , (x * 75)+37), 20)
                elif (self.game.board[x][y] == 2):
                    pygame.draw.circle(self.surface, WHITE, ((y * 75) +37,(x * 75)+37) , 20)
                elif self.game.board[x][y] == 0:
                    pygame.draw.circle(self.surface, GREEN, ((y * 75) +37,(x * 75)+37) , 20)   
        
        
        if len(self.game.actions(self.game.board)) == 0:
            if(self.game.player == 1):
                self.game.player = 2
            elif(self.game.player == 2):
                self.game.player = 1
            if len(self.game.actions(self.game.board) ) == 0:
                print("Game Over")
                print("Game Utility: ", self.game.utility())
                font = pygame.font.SysFont('Helvetica', 36)
                font2 = pygame.font.SysFont('Helvetica', 18)
                if self.game.utility() == 1:
                    win = "Victory to Black" 
                    win2 = "Black = " + str(self.game.total_black_piece(self.game.board)) + " pieces" + "   White = " + str(self.game.total_white_piece(self.game.board)) + " pieces"
                    self.victory_screen(win, win2, font, font2, self.surface, 300, 300)
                elif self.game.utility() == -1:
                    win = "Victory to White"
                    win2 = "Black = " + str(self.game.total_black_piece(self.game.board)) + " pieces" + "   White = " + str(self.game.total_white_piece(self.game.board)) + " pieces"
                    self.victory_screen(win, win2, font, font2, self.surface, 300, 300)
                elif self.game.utility() == 0:
                    win = "Tie Game"
                    win2 = "Black = " + str(self.game.total_black_piece(self.game.board)) + " pieces" + "   White = " + str(self.game.total_white_piece(self.game.board)) + " pieces"
                    self.victory_screen(win, win2, font, font2, self.surface, 300, 300)
            

        


        for x in self.game.actions(self.game.board):
            if(self.ai):
                if(self.game.player ==1):
                    pygame.draw.circle(self.surface, (255, 0, 0), ((x[-1][1] * 75)+37, (x[-1][0] * 75) +37), 5)
            else:
                pygame.draw.circle(self.surface, (255, 0, 0), ((x[-1][1] * 75)+37, (x[-1][0] * 75) +37), 5)

            
   
        
        
        pygame.display.update()


    def key_pressed_down_event(self, event):
        self.keyboard_commands(event)

    def key_let_go_event(self, event):
        pass
    
    def handle_mousedown(self, event):
        pass
    
    def handle_mouseup(self, event):
        x, y = event.pos
        #convert the mouse coordinates so it can match our 8x8 board.
        x_position = math.floor(x/75)
        y_position = math.floor(y/75)
        
        self.game.board = self.game.result( x_position, y_position, self.game.board)
        
       # self.game.move() to be implemented

    def handle_mousemove(self, event):
        pass #not applicable in this game.

    def keyboard_commands(self, event):
        
        # Ctrl + n equal restart game. Shortcut
        if event.key == pygame.K_n and pygame.key.get_mods() and pygame.KMOD_CTRL:
            self.game.__init__()
            self.start_game()
        # Ctrl + q means to quit the game shortcut
        #if self.keys_pressed_down[0] == pygame.KMOD_CTRL and self.keys_pressed_down[1] == pygame.K_q:
        if event.key == pygame.K_q and pygame.key.get_mods() and pygame.KMOD_CTRL:
            quit()
            sys.exit()
        #Crtlr + a activates and turns on ai
        if event.key == pygame.K_a and pygame.key.get_mods() and pygame.KMOD_CTRL:
            self.ai = True
        #Ctrl + p turns on player vs. player
        if event.key == pygame.K_p and pygame.key.get_mods() and pygame.KMOD_CTRL:
            self.ai = False
            

    #restarts the game by resetting the board inside the othello class
    def new_game(self):
        self.game.__init__()

    # starts up the game and sets all the parameter
    def start_game(self):
        self.ai = None
        self.gameStartUp()
        self.starting_screen()
        pygame.display.update()
        #This makes it that the only way to get out of the starting screen is by entering whether or not you want to play against ai or another player
        while True:
            if(self.ai != None):
                break
            for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        self.key_pressed_down_event(event)
                    elif event.type == pygame.KEYUP:
                        self.key_let_go_event(event)

                    elif event.type == pygame.MOUSEBUTTONUP:
                        pass
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        pass
                    elif event.type == pygame.MOUSEMOTION:
                        pass
                    elif event.type == pygame.QUIT:
                        quit()
                    else:
                        pass
        #This is needed to reset the screen without the starting menu text.
        self.gameStartUp()
        self.new_game()

        
        #This will take in commands until the game concludes
        while True:
            #check if ai is set if so then the second player will perform the ai actions
            if (self.ai and self.game.player == 2):
                print(self.game.terminal_test == False)
                state = copy.deepcopy(self.game.board)
                best_move = alpha_beta_cutoff_search(state, self.game)
                self.game.print_board()
                print()
                #covers the case if the ai can't make a move
                if (best_move == None):
                    self.player = 1
                    self.game.board_change = True
                else:
                    self.game.board = self.game.result(best_move[-1][1], best_move[-1][0], self.game.board)
                
            
            else:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        self.key_pressed_down_event(event)
                    elif event.type == pygame.KEYUP:
                        self.key_let_go_event(event)
                    elif event.type == pygame.MOUSEBUTTONUP:
                        self.handle_mouseup(event)
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        self.handle_mousedown(event)
                    elif event.type == pygame.MOUSEMOTION:
                        self.handle_mousemove(event)
                    elif event.type == pygame.QUIT:
                        quit()
                    else:
                        pass
        
            if self.game.board_change == True:
                self.draw_board()
                self.game.board_change = False
                
            #sets the fps to 40
            self.clock.tick(40)
        quit()

# note this is the section that could prob see the most improvement given time
# Given the nature of python everything is passed by object so I used deepcopy from the copy function
# in order bypass python's pass by object nature in order to get the code to work.
# This function effectively determines the ai actions. Its set only to explore up to a depth of 3 due to 
# significant slowdown when the ai is given many moves to make. 
# the evaluation function can be found in the Othello class.
def alpha_beta_cutoff_search(state, game, d=3, cutoff_test=None, eval_fn=None):
    """Search game to determine best action; use alpha-beta pruning.
    This version cuts off search and uses an evaluation function."""
    

    # Functions used by alpha_beta 
    def max_value(state, alpha, beta, depth):
        board_copy = copy.deepcopy(state)
        if cutoff_test(state, depth):
            return eval_fn(state)
        v = -np.inf
        for a in game.actions(state):
            state = copy.deepcopy(board_copy)
            v = max(v, min_value(game.result(a[-1][1], a[-1][0], state), alpha, beta, depth + 1))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        state = copy.deepcopy(board_copy)
        return v

    def min_value(state, alpha, beta, depth):
        board_copy = copy.deepcopy(state)
        if cutoff_test(state, depth):
            return eval_fn(state)
        v = np.inf
        for a in game.actions(state):
            state = copy.deepcopy(board_copy)
            v = min(v, max_value(game.result(a[-1][1], a[-1][0], state), alpha, beta, depth + 1))
            if v <= alpha:
                return v
            beta = min(beta, v)
        state = copy.deepcopy(board_copy)
        return v

    # Body of alpha_beta_cutoff_search starts here:
    # The default test cuts off at depth d or at a terminal state
    cutoff_test = (cutoff_test or (lambda state, depth: depth > d or game.terminal_test(state)))
    eval_fn = eval_fn or (lambda state: game.advanced_evaluation(state))
    best_score = -np.inf
    beta = np.inf
    best_action = None
    board_copy = copy.deepcopy(state)
    for a in game.actions(state):
        state = copy.deepcopy(board_copy)
        v = min_value(game.result(a[-1][1], a[-1][0], state), best_score, beta, 1)
        if v > best_score:
            best_score = v
            best_action = a
            print(v)
            print(best_action)
    game.player = 2
    return best_action

if __name__ == '__main__':
    Othello = Othello_Board()
    Othello.start_game()
                        
            




        

        

        
