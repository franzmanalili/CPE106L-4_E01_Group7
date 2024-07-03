import os
import random
import oxo_data

class Game:
    def __init__(self):
        self.game = self.new_game()

    def new_game(self):
        ''' Return a new empty game '''
        return list(" " * 9)

    def save_game(self):
        ''' Save the current game to disk '''
        oxo_data.saveGame(self.game)

    def restore_game(self):
        ''' Restore previously saved game. 
        If game not restored successfully, return new game '''
        try:
            game = oxo_data.restoreGame()
            if len(game) == 9:
                self.game = game
            else:
                self.game = self.new_game()
        except IOError:
            self.game = self.new_game()

    def _generate_move(self):
        ''' Generate a random cell from those available. 
        If all cells are used, return -1 '''
        options = [i for i in range(len(self.game)) if self.game[i] == " "]
        if options:
            return random.choice(options)
        else:
            return -1

    def _is_winning_move(self):
        ''' Check if the current move is a winning move '''
        wins = (
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        )

        for a, b, c in wins:
            chars = self.game[a] + self.game[b] + self.game[c]
            if chars == 'XXX' or chars == 'OOO':
                return True
        return False

    def user_move(self, cell):
        ''' Process the user move '''
        if self.game[cell] != ' ':
            raise ValueError('Invalid cell')
        else:
            self.game[cell] = 'X'
        if self._is_winning_move():
            return 'X'
        else:
            return ""

    def computer_move(self):
        ''' Process the computer move '''
        cell = self._generate_move()
        if cell == -1:
            return 'D'
        self.game[cell] = 'O'
        if self._is_winning_move():
            return 'O'
        else:
            return ""

    def play(self):
        ''' Test the game logic '''
        result = ""
        self.game = self.new_game()
        while not result:
            print(self.game)
            try:
                result = self.user_move(self._generate_move())
            except ValueError:
                print("Oops, that shouldn't happen")
            if not result:
                result = self.computer_move()

            if not result:
                continue
            elif result == 'D':
                print("It's a draw")
            else:
                print("Winner is:", result)
            print(self.game)

if __name__ == "__main__":
    game = Game()
    game.play()