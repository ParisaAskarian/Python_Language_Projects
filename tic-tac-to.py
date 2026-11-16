#Parisa Askarian - Fateme Akbari
class tic_tac_toc:

    def __init__(self,board = ['?']*9,player1 = "",player2 = "",winner_states = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.winner_state = winner_states

    def show_board(self):
        for i in range(9):
            if i%3 == 0:
                print()
            print(self.board[i],end=" ")
        print()

    def select_symbol(self):
        while True:  
             symbol = input("please select a symbol x or o: ")
             if symbol.lower() == 'x':
                 self.player1 = 'x'
                 self.player2 = 'o'
                 break
             elif symbol.lower() == 'o':
                 self.player2 = 'x'
                 self.player1 = 'o' 
                 break
             else:
                 continue

    def move_player(self,player):
        while True:
            index = int(input("please select an index from 0 to 8 :"))
            if index not in range(9):
                continue   
            elif self.board[index] == '?':
                self.board[index] = player
                break
            else:
                print("not empty")
                continue

    def check_winner(self,player):
        for index in self.winner_state:
            if self.board[index[0]] == self.board[index[1]] == self.board[index[2]] == player:
                return True
        return False

    def equal(self):
        for i in self.board:
            if i == '?':
                return False
        return True

game = tic_tac_toc() 

game.select_symbol()

game.show_board()

while True:
    game.move_player(game.player1)

    game.show_board()

    if game.check_winner(game.player1):
        print("congradualtion! player1 wins")
        break
    
    if game.equal():
        print("equal")
        break

    game.move_player(game.player2)

    game.show_board()

    if game.check_winner(game.player2):
        print("congradualtion! player2 wins")
        break
    
    if game.equal():
        print("equal")
        break

    