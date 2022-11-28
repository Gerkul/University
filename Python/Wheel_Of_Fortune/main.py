import random



def choice_game_difficulty():
    while True:
        choice = input("Enter a game difficulty. 1 - easy, 2 - normal, 3 - hard: ")

        if   choice == '1':
            return 7

        elif choice == '2':
            return 5

        elif choice == '3':
            return 3

        print("The choice was not enter corrently!")



class Game:
    def __init__(self):
        self.set_game_data()

        self.is_guessed_word = False
        self.is_guessed_letter = False
        self.is_running = True


    def running(self):
        while self.is_running:
            print(self.hidden_word, '@x', self.live_points)
            guess = input("Enter a letter or a word: "); print()

            self.check_the_guess(guess)
            self.check_the_game_status()



    def check_the_guess(self, guess):
        if len(guess) == 1:

            for i in range(len(self.gaming_word)):
                if self.gaming_word[i] == guess:

                    self.is_guessed_letter = True
                    self.guessed_letter = guess
                    self.hidden_word = self.hidden_word[:i] + guess + self.hidden_word[i + 1:]

                    if self.hidden_word.count('#') == 0:
                        self.is_guessed_word = True
                        self.is_guessed_letter = False

        elif guess == self.gaming_word:
            self.hidden_word = guess
            self.is_guessed_word = True


    def check_the_game_status(self):
        if self.is_guessed_letter:
            print(f"You guessed letter {self.guessed_letter}")
            self.is_guessed_letter = False

        elif self.is_guessed_word:
            print(f"You guessed word {self.hidden_word}")
            self.is_guessed_word = False

            if len(self.words) == 0:
                self.restart_game("Words is over. You won the party. Wonna play another? (yes/no): ")
            else:
                self.set_gaming_word()

        else:
            print("You less one 'live'")
            self.live_points -= 1

            if self.live_points == 0:
                self.restart_game("You lost the party. Wonna play another? (yes/no): ")


    def restart_game(self, message):
        while True:
            action = input(message)

            if action == "no":
                self.is_running = False
                return

            elif action == "yes":
                self.set_game_data()
                return


    def set_game_data(self):
        self.load_words()
        self.live_points = choice_game_difficulty()
        self.set_gaming_word()


    def set_gaming_word(self):
        print("Guess a new word")

        self.gaming_word = self.words.pop(random.randint(0, len(self.words) - 1))
        print(self.gaming_word)

        self.hidden_word = ''
        for _ in range(len(self.gaming_word)):
            self.hidden_word += '#'


    def load_words(self):
        with open("gaming_words.txt", 'r', encoding="UTF-8") as file:
            self.words = []
            for word in file.readlines():
                if word.endswith('\n'):
                    self.words.append(word[:-1])
                else:
                    self.words.append(word)



game = Game()
game.running()