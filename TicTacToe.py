# John Loeber | contact@johnloeber.com | Sep 12 2015 | Python 2.7.9

from time import sleep

# making the board a class provides an easy way to reset the board
class Board():
    def __init__(self):
        self.board = {(x,y): "   " for x in range(3) for y in range(3)}
    wins = [[(0,0), (1,0), (2,0)], [(0,1), (1,1), (2,1)], [(0,2), (1,2), (2,2)],
            [(0,0), (0,1), (0,2)], [(1,0), (1,1), (1,2)], [(2,0), (2,1), (2,2)],
            [(0,0), (1,1), (2,2)], [(0,2), (1,1), (2,0)]]

    def gameNotOver(self):
        """
        -1: player loses. 0: tie. 1: player wins. 1000: game not over.
        """
        for combination in self.wins:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != "   ":
                print self.board[combination[0]], "won!"
                return False
        if "   " in self.board.values():
            return 1000
        else:
            return 0

    def printBoard(self):
        print "---- ----- -----"
        for y in range(2,-1,-1):
            print self.board[(0,y)], "|", self.board[(1,y)], "|", self.board[(2,y)]
            print "---- ----- -----"

def getmove(board):
    print "Enter a coordinate."
    coord = raw_input().split()
    try:
        (x,y) = tuple([int(s) for s in coord if s.isdigit()])
        # generates an error if (x,y) is not in the board
        if board[(x,y)] == "   ":
            return (x,y)
        else:
            print "That square is occupied!"
            return getmove(board)
    except:
        print "Please enter a valid coordinate, like '1 1' or '0 2'."
        return getmove(board)

def makemove(board):
    print "Opponent is making a move..."
    
    return (1,1)

def game():
    global board
    board = Board()
    board.printBoard()
    while True:
        if board.gameNotOver():
            (x,y) = getmove(board.board)
            board.board[(x,y)] = " X "
        else:
            break
        board.printBoard()
        sleep(1)
        if board.gameNotOver():
            (x,y) = makemove(board.board)
            board.board[(x,y)] = " O "
        else:
            break
        board.printBoard()
    
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
