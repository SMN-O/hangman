import random 

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(self.word)
        self.word_list = list(self.word)
        self.letters_guessed = []

    def ask_for_input(self):
        while True:
            guess = input("Please guess a single letter: ")
            if guess.isalpha():
                break
            else:
                print("Try again. {num_lives} lives left")
                self.num_lives -= 1


    def check_guess(self, letter):
        guess = guess.lower()


def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        game.ask_for_input()
        game.check_guess()
        if game.num_lives == 0:
            print("GAME OVER")
            break
        elif game.word_guessed == game.word:
            print("YOU WIN")
            break  


if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
  