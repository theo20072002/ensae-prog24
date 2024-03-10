"""This is the game module. It contain an interface pygame to play at the swap puzzle"""

import pygame
import sys
import random as rd
from solver import Solver
from grid import Grid
import copy

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
GREEN2=(0,128,0)
BLUE=(0,0,255)
FUCHSIA=(255,0,255)


# first window :

# Responsive game window
width_screen,height_screen=1500,800 
SCORE_SIZE=100 # size of the window dedicated to the score display
screen = pygame.display.set_mode((width_screen, height_screen))

#chose the color of the screen
screen.fill((0,0,0))

# font of the texte
font_question = pygame.font.SysFont("Arial", 90)
police_mode = pygame.font.SysFont(None, 60)
police_button = pygame.font.SysFont(None, 75)

# text on the question 
text_question= font_question.render("Chosissez votre niveau de jeu :", True, WHITE)

# Dimensions et position of the question
x_question,y_question=width_screen//2,50
question_rect= text_question.get_rect(center=(x_question,y_question))

# text on the differenet game mode
text_mode1= police_mode.render("Choisir une grille provenant de input :", True, BLUE)
text_mode2= police_mode.render("Gener une grille aléatoire:", True, BLUE)

# Dimensions and position of the question
x_mode1,y_mode1,x_mode2,y_mode2=20,height_screen//3,20,2*height_screen//3
mode1_rect= text_mode1.get_rect(topleft=(x_mode1,y_mode1))
mode2_rect= text_mode2.get_rect(topleft=(x_mode2,y_mode2))


# text on the buttons
text_buttons=[]
for i in range (5):
    text_buttons.append(police_button.render(str(i), True, BLACK))
text_buttons.append(police_button.render("aléatoire", True, BLACK))

# Dimensions and positions of the buttons
buttons_rect= []
for i in range(5):
    buttons_rect.append(text_buttons[i].get_rect(center=((2*i+1)*width_screen//10,y_mode1+height_screen//6)))
buttons_rect.append(text_buttons[5].get_rect(center=(width_screen//2,y_mode2+height_screen//6)))


mode_chosen = None
Run=True
# first loop to choose the game mode
while Run:
    for event in pygame.event.get():
        # Event handling
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # check if the mouth clic is on a button
            for i in range (len(buttons_rect)):
                if buttons_rect[i].collidepoint(event.pos):
                    Run=False
                    mode_chosen=i # select the chosen mode
    
    # Draw the question
    pygame.draw.rect(screen,BLACK, question_rect)
    screen.blit(text_question, question_rect)
    
    # draw the buttons
    for i in range (len(buttons_rect)):
        pygame.draw.rect(screen, RED, buttons_rect[i])
        screen.blit(text_buttons[i], buttons_rect[i])
    
    # draw the differents mode games
    pygame.draw.rect(screen, GRAY, mode1_rect)
    screen.blit(text_mode1, mode1_rect)
    pygame.draw.rect(screen, GRAY, mode2_rect)
    screen.blit(text_mode2, mode2_rect)
    
    pygame.display.flip()















# first mode :
    

if mode_chosen <5 :
    # input text file to use for the game
    grid = open("input/grid"+str(mode_chosen)+".in", "r")

    # extract dimensions of the grid from the first line of the input file
    dimensions = grid.readline().split()
    BOARD_HEIGHT = int(dimensions[0])
    BOARD_WIDTH = int(dimensions[1])

    # Size of a tile
    Y_TILE_SIZE,X_TILE_SIZE= (height_screen-SCORE_SIZE)//BOARD_HEIGHT, width_screen//BOARD_WIDTH

    # Responsive game window
    screen = pygame.display.set_mode((X_TILE_SIZE * BOARD_WIDTH, Y_TILE_SIZE * BOARD_HEIGHT+SCORE_SIZE))
    # Set up the game clock (frame rate)
    clock = pygame.time.Clock()

    # 2D array (game board representation)
    board = [[0 for _ in range (BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

    # use the input file to set the board
    for i in range(BOARD_HEIGHT):
        row = grid.readline().split()
        for j in range(BOARD_WIDTH):
            board[i][j] = int(row[j])















# second mode:
            

else :

    # Responsive game window
    screen = pygame.display.set_mode((width_screen, height_screen))

    #chose the color of the screen
    screen.fill((0,0,0))

    # font of the text
    font_question = pygame.font.SysFont("Arial", 60)
    font_answer = pygame.font.SysFont("Arial", 90)

    # text on the question 
    text_question= font_question.render("Tapez la tail de la grille souhaité sous la forme m,n :", True, WHITE)

    # Dimensions and position of the question
    x_question,y_question=width_screen//2,50
    question_rect= text_question.get_rect(center=(x_question,y_question))

    # Variables for the text input
    input_text = str()
    allowed_characters=[","]
    for i in range(10):
        allowed_characters.append(str(i))

    clock = pygame.time.Clock()

    #loop to chose the side of the board
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.quit()
            
            elif event.type == pygame.KEYDOWN: # check if the Keydown is used
                
                if event.key == pygame.K_RETURN: 
                    if len(input_text.split(","))!=2 :# check the shape of the answer
                        input_text="" # if the shape is wrong, restart the input 
                    else: 
                        running=False
                
                # cancel last character        
                elif event.key == pygame.K_BACKSPACE: 
                    input_text = input_text[:-1]
                
                # add a caracter to the answer
                elif event.unicode in allowed_characters : #check if the caracter is allowed
                    input_text += event.unicode

            #clean the screen 
            screen.fill((0,0,0))
            
            # text on the answer 
            text_answer= font_answer.render(input_text, True, WHITE)

            # Dimensions and position of the answer
            x_answer,y_answer=width_screen//2,height_screen//2
            answer_rect= text_answer.get_rect(center=(x_answer,y_answer))

            # Draw the answer
            pygame.draw.rect(screen,GREEN, answer_rect)
            screen.blit(text_answer, answer_rect)

            # Draw the question
            pygame.draw.rect(screen,BLACK, question_rect)
            screen.blit(text_question, question_rect)


            pygame.display.flip()
            clock.tick(30)
        

    # extract dimensions of the grid from the input
    dimensions=input_text.split(",")
    BOARD_HEIGHT = int(dimensions[0])
    BOARD_WIDTH = int(dimensions[1])

    # Size of a tile
    Y_TILE_SIZE,X_TILE_SIZE= (height_screen-SCORE_SIZE)//BOARD_HEIGHT, width_screen//BOARD_WIDTH

    # Responsive game window
    screen = pygame.display.set_mode((X_TILE_SIZE * BOARD_WIDTH, Y_TILE_SIZE * BOARD_HEIGHT+SCORE_SIZE))
    
    # Set up the game clock (frame rate)
    clock = pygame.time.Clock()

    # Set a random board
    random_permutation=list(range(1,BOARD_HEIGHT*BOARD_WIDTH+1))
    rd.shuffle(random_permutation)
    board=[]
    for i in range (BOARD_HEIGHT):
        board.append(random_permutation[i*BOARD_WIDTH:(i+1)*BOARD_WIDTH])













# interface where the player can play


# font of the text
font_score = pygame.font.SysFont("Arial", 36)
font_restart=pygame.font.SysFont("Arial", 36)

# text on the score 
text_score= font_score.render("votre nombre de coups est de:", True, BLACK)

# Dimensions and position of the text score
x_score,y_score=width_screen//2-50,height_screen-SCORE_SIZE
x_switch, y_switch= width_screen//2+200,height_screen-SCORE_SIZE
score_rect= text_score.get_rect(center=(x_score,y_score+SCORE_SIZE//2))

# initial selected tile (-1, -1 -> no tile is selected)
selected_row, selected_column = -1, -1

# final state:
final_state=[[i+1 for i in range(j*BOARD_WIDTH,(j+1)*BOARD_WIDTH)] for j in range(BOARD_HEIGHT)]

# initial state: 
initial_state=copy.deepcopy(board)

#  loop for the restart screen loop and Game loop
while True:
    # count the number of switch 
    switch_number=0
    # Game loop   
    run=True
    board=copy.deepcopy(initial_state)
    while run:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get the mouse position
                pos = pygame.mouse.get_pos()
                if pos[1] < height_screen-SCORE_SIZE: # chek if the mouse is on the game and not on the score
                    # Figure out which tile was clicked
                    column = pos[0] // X_TILE_SIZE
                    row = pos[1] // Y_TILE_SIZE
                    # If a tile is already selected, swap it with the clicked tile if they are adjacent or cancel th selection if the tile selcted again  
                    if selected_row != -1 and selected_column != -1:
                        # Check if the selected tile and the clicked tile are the same
                        if (abs(selected_row - row) + abs(selected_column - column)) == 0:
                            selected_row, selected_column = -1, -1
                        # Check if the selected tile and the clicked tile are adjacent
                        elif (abs(selected_row - row) + abs(selected_column - column)) == 1:
                            # Swap the selected tile with the clicked tile
                            board[row][column], board[selected_row][selected_column] = board[selected_row][selected_column], board[row][column]
                            # Reset the selected tile and increase number of switch
                            selected_row, selected_column = -1, -1
                            switch_number+=1
                            if board==final_state: # stop the game if the final state is reach
                                run=False
                    # Otherwise, select the clicked tile
                    else:
                        selected_row, selected_column = row, column

        # Draw the game screen
        screen.fill(WHITE)
        for row in range(BOARD_HEIGHT):
            for column in range(BOARD_WIDTH):
                color = GRAY
                # Highlight the selected tile
                if row == selected_row and column == selected_column:
                    color = GREEN
                pygame.draw.rect(screen, color, (column * X_TILE_SIZE, row * Y_TILE_SIZE, X_TILE_SIZE, Y_TILE_SIZE)) # Draw tile
                pygame.draw.rect(screen, WHITE, (column * X_TILE_SIZE, row * Y_TILE_SIZE, X_TILE_SIZE, Y_TILE_SIZE), 1)  # Draw border
                font = pygame.font.Font(None, 36) # Create a font object
                text = font.render(str(board[row][column]), True, WHITE) # Create a text surface
                text_rect = text.get_rect(center=(column * X_TILE_SIZE + X_TILE_SIZE // 2, row * Y_TILE_SIZE + Y_TILE_SIZE // 2))  # Center text
                screen.blit(text, text_rect) # Draw text

        # Draw the score
        pygame.draw.rect(screen,GREEN, score_rect)# highlight the text
        screen.blit(text_score, score_rect) # Draw text

        # Draw th numbers of switch
        text_switch=font_score.render(str(switch_number), True, BLACK) #create text surface
        switch_rect=text_switch.get_rect(center=(x_switch,y_switch+SCORE_SIZE//2)) #center the text
        pygame.draw.rect(screen,RED, switch_rect)# highlight the text
        screen.blit(text_switch, switch_rect) # Draw text

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)


















    #solve the puzzle with A*
    s=Solver()
    grid=Grid(BOARD_HEIGHT,BOARD_WIDTH,initial_state)
    if BOARD_HEIGHT*BOARD_WIDTH<=12:
        solution_state=s.Astar(grid,"heuristic_manhattan")[0]
    elif BOARD_HEIGHT*BOARD_WIDTH<15:
        solution_state=s.Astar(grid,"heuristic_manhattan2")[0]
    else :
        solution_state=s.Astar(grid,"heuristic_manhattan3")[0]

    #minimum number of swap required
    min_switch_number= len(solution_state)-1

    # path possible to solve the puzzle
    solution_swap=grid.performed_swap_seq(solution_state)#transform the list of 2D array in required swap 
    grid.state=copy.deepcopy(initial_state)

    solution=[] # list of the row of teh solution
    max_swap_row=12 # number max of swap per row for the display
    count_swap_row=0 #number of swap in the current row 
    solution_row=str()
    for i in range(min_switch_number):
        count_swap_row+=1
        if count_swap_row==12 or i==min_switch_number-1:
            (x1,y1),(x2,y2)=solution_swap[i]
            solution_row+=str(grid.state[x1][y1])+" -> " +str(grid.state[x2][y2])# the number of the case switched are stockd in row
            grid.swap((x1,y1),(x2,y2)) # update the state of teh swap after the switch
            solution.append(solution_row)
            solution_row=str() # resart a new row
            count_swap_row=0
        else :
            (x1,y1),(x2,y2)=solution_swap[i]
            solution_row+=str(grid.state[x1][y1])+" -> " +str(grid.state[x2][y2]) +" , "# the number of the case switched are stockd in row
            grid.swap((x1,y1),(x2,y2)) # update the state of teh swap after the switch












    # interface to give a solution and restart to solve the same grid 

    # text on the restart screen:
    text_restarts=[font_restart.render("Le nombre de coups utiliser pour resoudre le puzzle est de:", True, WHITE)]
    text_restarts.append(font_restart.render(str(switch_number), True, BLACK))
    if BOARD_HEIGHT*BOARD_WIDTH<=12:# if A* can give an exact solution
        text_restarts.append(font_restart.render("Le nombre minimal de coups pour resoudre ce puzzle est de: ", True, WHITE))
    else: 
        text_restarts.append(font_restart.render("Une bonne aproximation du nombre minimal de coups pour resoudre ce puzzle est de: ", True, WHITE))
    text_restarts. append(font_restart.render(str(min_switch_number), True, BLACK))
    text_restarts.append(font_restart.render("Une solution minimal possible est : ", True, WHITE))
    for i in range (len(solution)):
        text_restarts. append(font_restart.render(solution[i], True, GREEN))
    text_restarts. append(font_restart.render("restart", True, WHITE))

    # Dimensions and position of the text on the restart screeen
    Y_RESTART_TILE= height_screen//(2*len(text_restarts)+1)
    restarts_position=[(width_screen//2,(2*i+1)*Y_RESTART_TILE) for i in range(len(text_restarts))]
    restarts_rect=[]
    for i in range(len(restarts_position)):
        restarts_rect.append(text_restarts[i].get_rect(center=restarts_position[i]))

    # Coror of the rectangle behind the text
    rect_colors=[BLACK, BLUE, BLACK, FUCHSIA, BLACK]
    for i in range (len(solution)):
        rect_colors.append(GREEN2)
    rect_colors.append(RED)

    #loop for the restart screen    
    restart=False
    while not(restart): # while the player don't decide to restart the game, keep the screen
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # check if there is a mouse click on the button restart
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                if restarts_rect[-1].collidepoint(event.pos): 
                    restart=True

        
        # Draw the restart screeen
        screen.fill(BLACK)
        for i in range (len(restarts_rect)):
            pygame.draw.rect(screen,rect_colors[i], restarts_rect[i])# highlight the text
            screen.blit(text_restarts[i], restarts_rect[i]) # Draw text


        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

pygame.quit()