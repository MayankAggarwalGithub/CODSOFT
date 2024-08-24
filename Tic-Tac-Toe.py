import os
import math

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def board_setup():
    return [' ' for _ in range(9)]

def show_board(b):
    print()
    for row in [b[i*3:(i+1)*3] for i in range(3)]:
        row_display = '| '
        for spot in row:
            spot_display = f'{spot}   ' if spot != ' ' else '    '
            row_display += spot_display + '| '
        print(row_display)
    print()

def check_win(b, p):
    wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
            (0, 3, 6), (1, 4, 7), (2, 5, 8), 
            (0, 4, 8), (2, 4, 6)]           
    return any(b[i] == b[j] == b[k] == p for i, j, k in wins)

def check_draw(b):
    return ' ' not in b

def open_spots(b):
    return [i for i, spot in enumerate(b) if spot == ' ']

def minmax(b, depth, alpha, beta, maxing):
    if check_win(b, 'O'):
        return 1
    elif check_win(b, 'X'):
        return -1
    elif check_draw(b):
        return 0
    
    if maxing:
        best = -math.inf
        for spot in open_spots(b):
            b[spot] = 'O'
            val = minmax(b, depth + 1, alpha, beta, False)
            b[spot] = ' '
            best = max(best, val)
            alpha = max(alpha, val)
            if beta <= alpha:
                break
        return best
    else:
        best = math.inf
        for spot in open_spots(b):
            b[spot] = 'X'
            val = minmax(b, depth + 1, alpha, beta, True)
            b[spot] = ' '
            best = min(best, val)
            beta = min(beta, val)
            if beta <= alpha:
                break
        return best

def ai_turn(b):
    best_val = -math.inf
    best_spot = None
    for spot in open_spots(b):
        b[spot] = 'O'
        val = minmax(b, 0, -math.inf, math.inf, False)
        b[spot] = ' '
        if val > best_val:
            best_val = val
            best_spot = spot
    b[best_spot] = 'O'

def game():
    b = board_setup()
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, AI is O")
    
    while True:
        clear()
        show_board(b)
        
        try:
            player_turn = int(input("Your move (1-9): ")) - 1
            if b[player_turn] != ' ':
                print("Invalid move! Try again.")
                continue
        except (ValueError, IndexError):
            print("Please enter a valid move (1-9).")
            continue

        b[player_turn] = 'X'
        
        if check_win(b, 'X'):
            clear()
            show_board(b)
            print("You win!")
            break
        elif check_draw(b):
            clear()
            show_board(b)
            print("It's a draw!")
            break
        
        ai_turn(b)
        
        if check_win(b, 'O'):
            clear()
            show_board(b)
            print("AI wins!")
            break
        elif check_draw(b):
            clear()
            show_board(b)
            print("It's a draw!")
            break
            
game()
