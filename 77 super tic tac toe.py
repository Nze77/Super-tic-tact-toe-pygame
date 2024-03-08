


import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
CELL_SIZE = 150
WIDTH, HEIGHT = 3 * CELL_SIZE, 3 * CELL_SIZE
LINE_WIDTH = 5
WHITE = (255, 255, 255)
GREEN = (119, 195, 119)
GREY = (204, 204, 204)
LINE_COLOR = (0, 0, 0)
FONT_SIZE = 30
currentgrid = 0
PLAYER = 'X'
LASTCLICKED = 0
next = 0
move = 0
x_wins = 0
o_wins = 0

#win conditions
board1_game = True
board2_game = True
board3_game = True
board4_game = True
board5_game = True
board6_game = True
board7_game = True
board8_game = True
board9_game = True


# Set up the screen
screen = pygame.display.set_mode((WIDTH+200, HEIGHT))
pygame.display.set_caption("Super Tic Tac Toe")

# Font
font = pygame.font.SysFont(None, FONT_SIZE)

# Draw the big grid
def draw_big_grid():
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (CELL_SIZE, 0), (CELL_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * CELL_SIZE, 0), (2 * CELL_SIZE, HEIGHT), LINE_WIDTH)
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, CELL_SIZE), (WIDTH, CELL_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * CELL_SIZE), (WIDTH, 2 * CELL_SIZE), LINE_WIDTH)



# Draw the small grid
def draw_small_grid1():
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (CELL_SIZE + 50, CELL_SIZE + 25), (CELL_SIZE + 50, 2 * CELL_SIZE - 25), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2*CELL_SIZE - 50 , CELL_SIZE + 25), (2*CELL_SIZE - 50, 2*CELL_SIZE - 25), LINE_WIDTH)
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (CELL_SIZE + 25 , CELL_SIZE + 50), (CELL_SIZE * 2 - 25, CELL_SIZE + 50), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (CELL_SIZE + 25 , CELL_SIZE + 100), (CELL_SIZE * 2 - 25, CELL_SIZE + 100), LINE_WIDTH)

def draw_small_grid2():
    k = 1
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (((k-1)*CELL_SIZE) + 50, ((k-1)*CELL_SIZE) + 25), ((k-1)*CELL_SIZE + 50, (k)* CELL_SIZE - 25), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (((k)*CELL_SIZE) - 50 , ((k-1)*CELL_SIZE) + 25), ((k)*CELL_SIZE - 50, (k)*CELL_SIZE - 25), LINE_WIDTH)
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, ((k-1)*CELL_SIZE + 25 , (k-1)*CELL_SIZE + 50), ((k)*CELL_SIZE - 25, (k-1)*CELL_SIZE + 50), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, ((k-1)*CELL_SIZE + 25 , (k)*CELL_SIZE - 50), ((k)*CELL_SIZE - 25, (k)*CELL_SIZE - 50), LINE_WIDTH)

def draw_small_grid3():
    k = 3
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (((k-1)*CELL_SIZE) + 50, ((k-1)*CELL_SIZE) + 25), ((k-1)*CELL_SIZE + 50, (k)* CELL_SIZE - 25), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (((k)*CELL_SIZE) - 50 , ((k-1)*CELL_SIZE) + 25), ((k)*CELL_SIZE - 50, (k)*CELL_SIZE - 25), LINE_WIDTH)
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, ((k-1)*CELL_SIZE + 25 , (k-1)*CELL_SIZE + 50), ((k)*CELL_SIZE - 25, (k-1)*CELL_SIZE + 50), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, ((k-1)*CELL_SIZE + 25 , (k)*CELL_SIZE - 50), ((k)*CELL_SIZE - 25, (k)*CELL_SIZE - 50), LINE_WIDTH)

def draw_small_grid4():
    lxs = CELL_SIZE + 25
    lxe = 2*CELL_SIZE - 25 
    ly = 50
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (lxs, ly), (lxe,  ly), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (lxs, ly +50 ), (lxe, ly+50), LINE_WIDTH)
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (lxs + 25 , ly-25), (lxe - CELL_SIZE + 75 , ly + 75), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (lxs + 75 , ly-25), (lxe - CELL_SIZE + 75 +50 , ly + 75), LINE_WIDTH)

def draw_small_grid5():
    lxs = 2*CELL_SIZE + 25
    lxe = 3*CELL_SIZE - 25 
    ly = 50
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (lxs, ly), (lxe,  ly), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (lxs, ly +50 ), (lxe, ly+50), LINE_WIDTH)
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (lxs + 25 , ly-25), (lxe - CELL_SIZE + 75 , ly + 75), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (lxs + 75 , ly-25), (lxe - CELL_SIZE + 75 +50 , ly + 75), LINE_WIDTH)

def draw_small_grid6():
    lxs = 2*CELL_SIZE + 25
    lxe = 3*CELL_SIZE - 25 
    ly = CELL_SIZE+50
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (lxs, ly), (lxe,  ly), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (lxs, ly +50 ), (lxe, ly+50), LINE_WIDTH)
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (lxs + 25 , ly-25), (lxe - CELL_SIZE + 75 , ly + 75), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (lxs + 75 , ly-25), (lxe - CELL_SIZE + 75 +50 , ly + 75), LINE_WIDTH)

def draw_small_grid7():
    lxs = 0*CELL_SIZE + 25
    lxe = 1*CELL_SIZE - 25 
    ly = CELL_SIZE+50
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (lxs, ly), (lxe,  ly), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (lxs, ly +50 ), (lxe, ly+50), LINE_WIDTH)
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (lxs + 25 , ly-25), (lxe - CELL_SIZE + 75 , ly + 75), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (lxs + 75 , ly-25), (lxe - CELL_SIZE + 75 +50 , ly + 75), LINE_WIDTH)

def draw_small_grid8():
    lxs = 0*CELL_SIZE + 25
    lxe = lxs+CELL_SIZE - 50
    ly = 2*CELL_SIZE+50
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (lxs, ly), (lxe,  ly), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (lxs, ly +50 ), (lxe, ly+50), LINE_WIDTH)
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (lxs + 25 , ly-25), (lxe - CELL_SIZE + 75 , ly + 75), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (lxs + 75 , ly-25), (lxe - CELL_SIZE + 75 +50 , ly + 75), LINE_WIDTH)

def draw_small_grid9():
    lxs = 1*CELL_SIZE + 25
    lxe = lxs+CELL_SIZE - 50
    ly = 2*CELL_SIZE+50
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (lxs, ly), (lxe,  ly), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (lxs, ly +50 ), (lxe, ly+50), LINE_WIDTH)
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (lxs + 25 , ly-25), (lxe - CELL_SIZE + 75 , ly + 75), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (lxs + 75 , ly-25), (lxe - CELL_SIZE + 75 +50 , ly + 75), LINE_WIDTH)

board1 = [['' for _ in range(3)] for _ in range(3)]
board2 = [['' for _ in range(3)] for _ in range(3)]
board3 = [['' for _ in range(3)] for _ in range(3)]
board4 = [['' for _ in range(3)] for _ in range(3)]
board5 = [['' for _ in range(3)] for _ in range(3)]
board6 = [['' for _ in range(3)] for _ in range(3)]
board7 = [['' for _ in range(3)] for _ in range(3)]
board8 = [['' for _ in range(3)] for _ in range(3)]
board9 = [['' for _ in range(3)] for _ in range(3)]

def Lastsmallgrid(row, col):
    if row < 3 and row >= 0:
        if col < 3 and col >= 0:
            return 1
    if row < 6 and row >= 3:
        if col < 3 and col >= 0:
            return 2
    if row < 9 and row >= 6:
        if col < 3 and col >= 0:
            return 3
    if row >= 3 and row < 6:
        if col >= 3 and col < 6:
            return 5
    if row >= 6 and row < 9:
        if col >= 3 and col < 6:
            return 6
    if row < 3 and row >= 0:
        if col >= 3 and col < 6:
            return 4
    if row < 3 and row >= 0:
        if col < 9 and col >= 6:
            return 7
    if row >= 3 and row < 6:
        if col >= 6 and col < 9:
            return 8
    if row >= 6 and row < 9:
        if col >= 6 and col < 9:
            return 9


def marksquare(row, col, PL):
    if row < 3 and row >= 0:
        if col < 3 and col >= 0:
            if board1[col][row] == '':
                if board1_game == True:
                    board1[col][row] = PL
                    return True
                return False
    if row < 6 and row >= 3:
        if col < 3 and col >= 0:
            if board2[col][row-3] == '':
                if board2_game == True:
                    board2[col][row-3] = PL
                    return True
                return False
    if row < 9 and row >= 6:
        if col < 3 and col >= 0:
            if board3[col][row-6] == '':
                if board3_game == True:
                    board3[col][row-6] = PL
                    return True
                return False
    if row >= 3 and row < 6:
        if col >= 3 and col < 6:
            if board5[col-3][row-3] == '':
                if board5_game == True:
                    board5[col-3][row-3] = PL
                    return True
                return False
    if row >= 6 and row < 9:
        if col >= 3 and col < 6:
            if board6[col-3][row-6] == '':
                if board6_game == True:
                    board6[col-3][row-6] = PL
                    return True
                return False
    if row < 3 and row >= 0:
        if col >= 3 and col < 6:
            if board4[col-3][row] == '':
                if board4_game == True:
                    board4[col-3][row] = PL
                    return True
                return False
    if row < 3 and row >= 0:
        if col < 9 and col >= 6:
            if board7[col-6][row] == '':
                if board7_game == True:
                    board7[col-6][row] = PL
                    return True
                return False
    if row >= 3 and row < 6:
        if col >= 6 and col < 9:
            if board8[col-6][row-3] == '':
                if board8_game == True:
                    board8[col-6][row-3] = PL
                    return True
                return False
    if row >= 6 and row < 9:
        if col >= 6 and col < 9:
            if board9[col-6][row-6] == '':
                if board9_game == True:
                    board9[col-6][row-6] = PL
                    return True
                return False
    
def checkwinner(P):
    global board1_game, board2_game, board3_game, board4_game, board5_game, board6_game, board7_game, board8_game, board9_game, next, LASTCLICKED
    # ADD A LAST CLICKED VARIABLE FOR CHECKING THE WINNER.
    if P == 1:
        for row in board1:
            if row.count(row[0]) == len(row) and row[0] != '':
                board1_game = False
                if next == 1:
                    next = 0
                return True

        # Check columns
        for col in range(len(board1)):
            if board1[0][col] == board1[1][col] == board1[2][col] and board1[0][col] != '':
                board1_game = False
                if next == 1:
                    next = 0
                return True

        # Check diagonals
        if board1[0][0] == board1[1][1] == board1[2][2] != '':
            board1_game = False
            if next == 1:
                    next = 0
            return True
        if board1[0][2] == board1[1][1] == board1[2][0] != '':
            board1_game = False
            if next == 1:
                    next = 0
            return True

        return False

    if P == 2:
        for row in board2:
            if row.count(row[0]) == len(row) and row[0] != '':
                board2_game = False
                if next == 2:
                    next = 0
                return True

        # Check columns
        for col in range(len(board2)):
            if board2[0][col] == board2[1][col] == board2[2][col] and board2[0][col] != '':
                board2_game = False
                if next == 2:
                    next = 0
                return True

        # Check diagonals
        if board2[0][0] == board2[1][1] == board2[2][2] != '':
            board2_game = False
            if next == 2:
                    next = 0
            return True
        if board2[0][2] == board2[1][1] == board2[2][0] != '':
            board2_game = False
            if next == 2:
                    next = 0
            return True
        return False

    if P == 3:
        for row in board3:
            if row.count(row[0]) == len(row) and row[0] != '':
                board3_game = False
                if next == 3:
                    next = 0
                return True
    
        # Check columns
        for col in range(len(board3)):
            if board3[0][col] == board3[1][col] == board3[2][col] and board3[0][col] != '':
                board3_game = False
                if next == 3:
                    next = 0
                return True

        # Check diagonals
        if board3[0][0] == board3[1][1] == board3[2][2] != '':
            board3_game = False
            if next == 3:
                    next = 0
            return True
        if board3[0][2] == board3[1][1] == board3[2][0] != '':
            board3_game = False
            if next == 3:
                    next = 0
            return True
        return False
    
    if P == 4:
        for row in board4:
            if row.count(row[0]) == len(row) and row[0] != '':
                board4_game = False
                if next == 4:
                    next = 0
                return True

        # Check columns
        for col in range(len(board4)):
            if board4[0][col] == board4[1][col] == board4[2][col] and board4[0][col] != '':
                board4_game = False
                if next == 4:
                    next = 0
                return True

        # Check diagonals
        if board4[0][0] == board4[1][1] == board4[2][2] != '':
            board4_game = False
            if next == 4:
                    next = 0
            return True
        if board4[0][2] == board4[1][1] == board4[2][0] != '':
            board4_game = False
            if next == 4:
                    next = 0
            return True
        return False

    if P == 5:
        for row in board5:
            if row.count(row[0]) == len(row) and row[0] != '':
                board5_game = False
                if next == 5:
                    next = 0
                return True

        # Check columns
        for col in range(len(board5)):
            if board5[0][col] == board5[1][col] == board5[2][col] and board5[0][col] != '':
                board5_game = False
                if next == 5:
                    next = 0
                return True

        # Check diagonals
        if board5[0][0] == board5[1][1] == board5[2][2] != '':
            board5_game = False
            if next == 5:
                    next = 0
            return True
        if board5[0][2] == board5[1][1] == board5[2][0] != '':
            board5_game = False
            if next == 5:
                    next = 0
            return True
        return False

    if P == 6:
        for row in board6:
            if row.count(row[0]) == len(row) and row[0] != '':
                board6_game = False
                if next == 6:
                    next = 0
                return True

        # Check columns
        for col in range(len(board6)):
            if board6[0][col] == board6[1][col] == board6[2][col] and board6[0][col] != '':
                board6_game = False
                if next == 6:
                    next = 0
                return True

        # Check diagonals
        if board6[0][0] == board6[1][1] == board6[2][2] != '':
            board6_game = False
            if next == 6:
                    next = 0
            return True
        if board6[0][2] == board6[1][1] == board6[2][0] != '':
            board6_game = False
            if next == 6:
                    next = 0
            return True
        return False

    if P == 7:
        for row in board7:
            if row.count(row[0]) == len(row) and row[0] != '':
                board7_game = False
                if next == 7:
                    next = 0
                return True

        # Check columns
        for col in range(len(board7)):
            if board7[0][col] == board7[1][col] == board7[2][col] and board7[0][col] != '':
                board7_game = False
                if next == 7:
                    next = 0
                return True

        # Check diagonals
        if board7[0][0] == board7[1][1] == board7[2][2] != '':
            board7_game = False
            if next == 7:
                    next = 0
            return True
        if board7[0][2] == board7[1][1] == board7[2][0] != '':
            board7_game = False
            if next == 7:
                    next = 0
            return True
        return False

    if P == 8:
        for row in board8:
            if row.count(row[0]) == len(row) and row[0] != '':
                board8_game = False
                if next == 8:
                    next = 0
                return True

        # Check columns
        for col in range(len(board8)):
            if board8[0][col] == board8[1][col] == board8[2][col] and board8[0][col] != '':
                board8_game = False
                if next == 8:
                    next = 0
                return True

        # Check diagonals
        if board8[0][0] == board8[1][1] == board8[2][2] != '':
            board8_game = False
            if next == 8:
                    next = 0
            return True
        if board8[0][2] == board8[1][1] == board8[2][0] != '':
            board8_game = False
            if next == 8:
                    next = 0
            return True
        return False

    if P == 9:
        for row in board9:
            if row.count(row[0]) == len(row) and row[0] != '':
                board9_game = False
                if next == 9:
                    next = 0
                return True

        # Check columns
        for col in range(len(board9)):
            if board9[0][col] == board9[1][col] == board9[2][col] and board9[0][col] != '':
                board9_game = False
                if next == 9:
                    next = 0
                return True

        # Check diagonals
        if board9[0][0] == board9[1][1] == board9[2][2] != '':
            board9_game = False
            if next == 9:
                next = 0
            return True
        if board9[0][2] == board9[1][1] == board9[2][0] != '':
            board9_game = False
            if next == 9:
                next = 0
            return True

        return False

def checkdraw():
    global next
    if next == 1:
        if all('' not in row for row in board1):
            next = 0
    if next == 2:
        if all('' not in row for row in board2):
            next = 0
    if next == 3:
        if all('' not in row for row in board3):
            next = 0
    if next == 4:
        if all('' not in row for row in board4):
            next = 0
    if next == 5:
        if all('' not in row for row in board5):
            next = 0
    if next == 6:
        if all('' not in row for row in board6):
            next = 0
    if next == 7:
        if all('' not in row for row in board7):
            next = 0
    if next == 8:
        if all('' not in row for row in board8):
            next = 0
    if next == 9:
        if all('' not in row for row in board9):
            next = 0


def nextmove(row, col):
    if [row, col] in [[0,0], [0,3], [0,6], [3,0], [3,3], [3,6], [6,0], [6,3], [6,6]]:
        return 1 if board1_game else 0
    elif [row, col] in [[1,0], [4,0], [7,0], [1,3], [4,3], [7,3], [1,6], [4,6], [7,6]]:
        return 2 if board2_game else 0
    elif [row, col] in [[2,0], [5,0], [8,0], [2,3], [5,3], [8,3], [2,6], [5,6], [8,6]]:
        return 3 if board3_game else 0
    elif [row, col] in [[0,1], [3,1], [6,1], [0,4], [3,4], [6,4], [0,7], [3,7], [6,7]]:
        return 4 if board4_game else 0
    elif [row, col] in [[1,1], [4,1], [7,1], [1,4], [4,4], [7,4], [1,7], [4,7], [7,7]]:
        return 5 if board5_game else 0
    elif [row, col] in [[2,1], [5,1], [8,1], [2,4], [5,4], [8,4], [2,7], [5,7], [8,7]]:
        return 6 if board6_game else 0
    elif [row, col] in [[0,2], [3,2], [6,2], [0,5], [3,5], [6,5], [0,8], [3,8], [6,8]]:
        return 7 if board7_game else 0
    elif [row, col] in [[1,2], [4,2], [7,2], [1,5], [4,5], [7,5], [1,8], [4,8], [7,8]]:
        return 8 if board8_game else 0
    else:
        return 9 if board9_game else 0
    
def draw_figures():
    for row in range(3):
        for col in range(3):
            if board1[col][row] == 'X':
                pygame.draw.line(screen, LINE_COLOR, (50*row+10, 50*col+10), (50*(row+1)-10, 50*(col+1)-10), 3)
                pygame.draw.line(screen, LINE_COLOR, (50*(row+1)-10, 50*col+10), (50*(row)+10, 50*(col+1)-10), 3)
            if board1[col][row] == 'O':
                pygame.draw.circle(screen, LINE_COLOR, (row*50+25, col*50+25), 15, 3)
            if board2[col][row] == 'X':
                pygame.draw.line(screen, LINE_COLOR, (50*(row+3)+10, 50*col+10), (50*(row+4)-10, 50*(col+1)-10), 3)
                pygame.draw.line(screen, LINE_COLOR, (50*(row+4)-10, 50*col+10), (50*(row+3)+10, 50*(col+1)-10), 3)
            if board2[col][row] == 'O':
                pygame.draw.circle(screen, LINE_COLOR, ((row+3)*50+25, col*50+25), 15, 3)
            if board3[col][row] == 'X':
                pygame.draw.line(screen, LINE_COLOR, (50*(row+6)+10, 50*col+10), (50*(row+7)-10, 50*(col+1)-10), 3)
                pygame.draw.line(screen, LINE_COLOR, (50*(row+7)-10, 50*col+10), (50*(row+6)+10, 50*(col+1)-10), 3)
            if board3[col][row] == 'O':
                pygame.draw.circle(screen, LINE_COLOR, ((row+6)*50+25, col*50+25), 15, 3)
            if board4[col][row] == 'X':
                pygame.draw.line(screen, LINE_COLOR, (50*row+10, 50*(col+3)+10), (50*(row+1)-10, 50*(col+4)-10), 3)
                pygame.draw.line(screen, LINE_COLOR, (50*(row+1)-10, 50*(col+3)+10), (50*(row)+10, 50*(col+4)-10), 3)
            if board4[col][row] == 'O':
                pygame.draw.circle(screen, LINE_COLOR, (row*50+25, (col+3)*50+25), 15, 3)
            if board5[col][row] == 'X':
                pygame.draw.line(screen, LINE_COLOR, (50*(row+3)+10, 50*(col+3)+10), (50*(row+4)-10, 50*(col+4)-10), 3)
                pygame.draw.line(screen, LINE_COLOR, (50*(row+4)-10, 50*(col+3)+10), (50*(row+3)+10, 50*(col+4)-10), 3)
            if board5[col][row] == 'O':
                pygame.draw.circle(screen, LINE_COLOR, ((row+3)*50+25, (col+3)*50+25), 15, 3)
            if board6[col][row] == 'X':
                pygame.draw.line(screen, LINE_COLOR, (50*(row+6)+10, 50*(col+3)+10), (50*(row+7)-10, 50*(col+4)-10), 3)
                pygame.draw.line(screen, LINE_COLOR, (50*(row+7)-10, 50*(col+3)+10), (50*(row+6)+10, 50*(col+4)-10), 3)
            if board6[col][row] == 'O':
                pygame.draw.circle(screen, LINE_COLOR, ((row+6)*50+25, (col+3)*50+25), 15, 3)
            if board7[col][row] == 'X':
                pygame.draw.line(screen, LINE_COLOR, (50*row+10, 50*(col+6)+10), (50*(row+1)-10, 50*(col+7)-10), 3)
                pygame.draw.line(screen, LINE_COLOR, (50*(row+1)-10, 50*(col+6)+10), (50*(row)+10, 50*(col+7)-10), 3)
            if board7[col][row] == 'O':
                pygame.draw.circle(screen, LINE_COLOR, (row*50+25, (col+6)*50+25), 15, 3)
            if board8[col][row] == 'X':
                pygame.draw.line(screen, LINE_COLOR, (50*(row+3)+10, 50*(col+6)+10), (50*(row+4)-10, 50*(col+7)-10), 3)
                pygame.draw.line(screen, LINE_COLOR, (50*(row+4)-10, 50*(col+6)+10), (50*(row+3)+10, 50*(col+7)-10), 3)
            if board8[col][row] == 'O':
                pygame.draw.circle(screen, LINE_COLOR, ((row+3)*50+25, (col+6)*50+25), 15, 3)
            if board9[col][row] == 'X':
                pygame.draw.line(screen, LINE_COLOR, (50*(row+6)+10, 50*(col+6)+10), (50*(row+7)-10, 50*(col+7)-10), 3)
                pygame.draw.line(screen, LINE_COLOR, (50*(row+7)-10, 50*(col+6)+10), (50*(row+6)+10, 50*(col+7)-10), 3)
            if board9[col][row] == 'O':
                pygame.draw.circle(screen, LINE_COLOR, ((row+6)*50+25, (col+6)*50+25), 15, 3)

                
def wins():
    text1 = "X score:-"
    font = pygame.font.Font(None, 36)
    text1_surface = font.render(text1, True, LINE_COLOR)
    text1_rect = text1_surface.get_rect()
    text1_rect.center = (525, 50)
    screen.blit(text1_surface, text1_rect)
    text2 = "O score:-"
    font = pygame.font.Font(None, 36)
    text2_surface = font.render(text2, True, LINE_COLOR)
    text2_rect = text2_surface.get_rect()
    text2_rect.center = (525, 100)
    screen.blit(text2_surface, text2_rect)
    x_wins_surface = font.render(str(x_wins), True, LINE_COLOR)
    x_wins_rect = x_wins_surface.get_rect()
    x_wins_rect.center = (585, 52)
    screen.blit(x_wins_surface, x_wins_rect)
    y_wins_surface = font.render(str(o_wins), True, LINE_COLOR)
    y_wins_rect = y_wins_surface.get_rect()
    y_wins_rect.center = (585, 102)
    screen.blit(y_wins_surface, y_wins_rect)

def plug():
    plug_insta = "@aryanze.77"
    plug_insta_surface = font.render(plug_insta, True, LINE_COLOR)
    plug_insta_rect = plug_insta_surface.get_rect()
    plug_insta_rect.center = (575, 400)
    screen.blit(plug_insta_surface, plug_insta_rect)
    plug1_insta = "on insta"
    plug1_insta_surface = font.render(plug1_insta, True, LINE_COLOR)
    plug1_insta_rect = plug1_insta_surface.get_rect()
    plug1_insta_rect.center = (595, 425)
    screen.blit(plug1_insta_surface, plug1_insta_rect)



# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(GREY)
    

    if next == 0:
        screen.fill(GREEN)
    elif next == 1:
        pygame.draw.rect(screen, GREEN,(0,0,150,150))
    elif next == 2:
        pygame.draw.rect(screen, GREEN,(150,0,150,150))
    elif next == 3:
        pygame.draw.rect(screen, GREEN,(300,0,150,150))
    elif next == 4:
        pygame.draw.rect(screen, GREEN,(0,150,150,150))
    elif next == 5:
        pygame.draw.rect(screen, GREEN,(150,150,150,150))
    elif next == 6:
        pygame.draw.rect(screen, GREEN,(300,150,150,150))
    elif next == 7:
        pygame.draw.rect(screen, GREEN,(0,300,150,150))
    elif next == 8:
        pygame.draw.rect(screen, GREEN,(150,300,150,150))
    elif next == 9:
        pygame.draw.rect(screen, GREEN,(300,300,150,150))

    # Draw the big grid
    draw_big_grid()

    # Draw the small grid
    draw_small_grid1()
    draw_small_grid2()
    draw_small_grid3()
    draw_small_grid4()
    draw_small_grid5()
    draw_small_grid6()
    draw_small_grid7()
    draw_small_grid8()
    draw_small_grid9()
    draw_figures()
    wins()
    plug()

    mouse_pressed = False

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and not mouse_pressed and running:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                move += 1
                
                mouse_pressed = True

                clicked_row = mouseX // 51
                clicked_col = mouseY // 51
                #print(board1)
                
                
                if move == 1:
                    if marksquare(clicked_row, clicked_col, PLAYER):
                        next = nextmove(clicked_row, clicked_col)
                        PLAYER = 'O'
                
                if move > 1:
                    LASTCLICKED = Lastsmallgrid(clicked_row, clicked_col) if next != 0 else 0
                    if LASTCLICKED == next:
                        if marksquare(clicked_row, clicked_col, PLAYER):
                                next = nextmove(clicked_row,clicked_col)
                                checkdraw()

                                if checkwinner(LASTCLICKED):
                                    print(f"{PLAYER} wins")
                                    if PLAYER == 'X':
                                        x_wins += 1
                                    else:
                                        o_wins += 1
                                    PLAYER = 'O' if PLAYER == 'X' else 'X'
                                else:
                                    PLAYER = 'O' if PLAYER == 'X' else 'X'
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_pressed = False

               

                
            



    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
