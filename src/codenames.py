from utils import get_vocab
import random

class Game:
    def __init__(self, team_size: int, vocab_size: int) -> None:
        self.team_size = team_size
        self.vocab_size = vocab_size
        self.vocab = get_vocab(vocab_size)
        self.red = []
        self.blue = []
        self.neutral = []
        self.black = []

    def create_game_board(self):
        new_list = random.sample(self.vocab, (self.vocab_size*2+self.vocab_size+1))
        self.red = new_list[:self.vocab_size]
        self.blue = new_list[self.vocab_size:2*self.vocab_size]
        self.neutral = new_list[2*self.vocab_size:(self.vocab_size*2+self.vocab_size)]
        self.black.append(new_list[-1])


    def __repr__(self):
        return f"""red cards: {self.red}
        blue cards: {self.blue}
        neutral cards: {self.neutral}
        the black card:{self.black}
        """

if __name__ == "__main__":
    game = Game(3, 10)
    print(game)
    game.create_game_board()
    print(game)
