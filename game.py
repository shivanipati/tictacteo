from player import HumanPlayer , RandomClassPlayer
# import Time
class TicTacToe:
    def __init__(self):
        self.board =[' ' for _ in range(9)] # we will use a single list to rep 3*3 board
        self.current_winner = None # keep treck on winner

    def print_board(self):
        # this is just getting the row
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print( '| ' +' | '.join(row)+ ' |  ')

    @staticmethod
    def print_board_nums():
        #0|1|2 etc

        number_board = [[str(i) for i in range(j*3,(j+1)*3)]for j in range(3)]
        for row in number_board:
            print(' | ' +' | '.join(row)+' |')


    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board


    def num_empty_squares(self):
        return self.board.count(' ')



    def make_move(self,square,letter):
        if self.board[square]== ' ':
            self.board[square]= letter
            if self.winner(square , letter ):
                self .current_winner = letter

            return True
        return False
    def winner(self,square, letter):
        row_ind = square // 3
        row = self.board[row_ind * 3 : (row_ind +1) *3]
        if all([spot == letter for spot in row]):
            return True

        #check coloum
        col_ind = square %3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check diagonal
        if square %2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]] # left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                 return True
            diagonal2 = [self.board[i] for i in [2,4,6]] # right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                 return True

        return False

def play(game,x_player,o_player,print_game =True):
    if print_game:
        game.print_board_nums()

    letter = 'X' # starting letter
    while game.empty_squares():
         if letter == 'O':
             square = o_player.get_move(game)
         else:
             square = x_player.get_move(game)

         # let define a function to make a move
         if game.make_move(square,letter):
             if print_game:
                 print(letter +f' make a move square {square}')
                 game.print_board()
                 print('')#just empty line

             if game.current_winner:
                 if print_game:
                     print(letter + 'Wins!')

                 return letter


             letter  = 'O' if letter == 'X' else 'X'
         #tiny break
         # time.sleep(0.8)

             # if letter == 'X':
             #     letter = 'O'
             # else:
             #     letter == 'X'

         if print_game:
             print('its a tie!')

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomClassPlayer('O')
    t = TicTacToe()
    play(t,x_player,o_player , print_game=True)





