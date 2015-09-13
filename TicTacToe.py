# John Loeber | contact@johnloeber.com | Sep 12 2015 | Python 2.7.9

from time import sleep

def game_not_over(board):
    """
    -1: player loses. 0: tie. 1: player wins. 1000: game not over.
    """
    wins = [[(0,0), (1,0), (2,0)], [(0,1), (1,1), (2,1)], [(0,2), (1,2), (2,2)],
            [(0,0), (0,1), (0,2)], [(1,0), (1,1), (1,2)], [(2,0), (2,1), (2,2)],
            [(0,0), (1,1), (2,2)], [(0,2), (1,1), (2,0)]]
    for combination in wins:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != "   ":
            mapping = {" X ": 1, " O ": -1}
            return mapping[board[combination[0]]]
    if "   " in board.values():
        return 1000
    else:
        return 0

def print_board(board):
    print "---- ----- -----"
    for y in range(2,-1,-1):
        print board[(0,y)], "|", board[(1,y)], "|", board[(2,y)]
        print "---- ----- -----"

def get_move(board):
    print "Enter a coordinate."
    coord = raw_input().split()
    try:
        (x,y) = tuple([int(s) for s in coord if s.isdigit()])
        # generates an error if (x,y) is not in the board
        if board[(x,y)] == "   ":
            return (x,y)
        else:
            print "That square is occupied!"
            return get_move(board)
    except:
        print "Please enter a valid coordinate, like '1 1' or '0 2'."
        return get_move(board)

def make_move(board):
    print "Opponent is making a move..."
    
    return (1,1)

def game():
    board = {(x,y): "   " for x in range(3) for y in range(3)}
    print_board(board)
    mapping = {-1: " lost!", 1: " won!"}

    while True:
        # a bit of code-recycling going on below. Not too egregious.
        game_status = game_not_over(board)
        if game_status == 1000:
            (x,y) = get_move(board)
            board[(x,y)] = " X "
        else:
            print "You" + mapping[game_status]
            break

        print_board(board)
        sleep(1)

        game_status = game_not_over(board)
        if game_status == 1000:
            (x,y) = make_move(board)
            board[(x,y)] = " O "
        else:
            print "You" + mapping[game_status]
            break
        print_board(board)
    
    print "New Game? Enter 'y' or 'n'."
    command = raw_input().lower()
    if command=='y':
        game()

def main():
    print "Welcome to Tic-Tac-Toe! Play by entering coordinates where you wish to place a piece."
    print "(0,0) is the bottom left corner and (2,2) is the top-right. Example: '1 1' to place in the middle." 
    print "Your marker is X. The opponent's marker is denoted O."
    game() 
    
if __name__=='__main__':
    main()
