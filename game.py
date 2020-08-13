import random
from prettytable import PrettyTable

answer = ""
answer_list = []
default_guess = ['-', '-', '-', '-']
final_list = []
current_guess = ""
highest_score = 0
letter_l_counter = 0
bad_guess_counter = 0


class Guess:
    def main_menu(self):
        global default_guess, current_guess
        print("** The great guessing game **")
        for char in default_guess:
            current_guess += char
        print("Current guess: " + current_guess)
        guess.option_selection()

    def option_selection(self):
        print("g = guess, t = tell me, l for a letter, and q to quit")
        user_option = input("Enter option: ")
        guess.option_func(user_option)

    def option_func(self, option):
        self.option = option
        global answer, answer_list, default_guess, letter_l_counter
        if True:
            if option == "g":
                user_guess = input("What is your 4 letter guess: ")
                # logic of handling guess
                if user_guess == answer:
                    print("You guessed it right the word was " + answer)
                    answer_list.append(answer)
                    stringDB.randomise()
                    game.game_number += 1
                    game.game_number_list.append(game.game_number)
                    game.game_status = True
                    game.game_status_list.append(game.game_status)
                    game.game_bad_guesses_list.append(game.game_bad_guesses)
                    game.game_bad_guesses = 0
                    game.game_missed_letters_list.append([])
                    game.calculate_score()
                    print("Current guess:" + current_guess)
                else:
                    print("Wrong guess")
                    print("".join(default_guess))
                    global bad_guess_counter
                    bad_guess_counter += 1
                    game.game_status = False
                    game.game_bad_guesses += 1
                guess.option_selection()

            elif option == "t":
                print("The 4 letter word is: " + answer)
                print("Current guess:" + current_guess)
                answer_list.append(answer)
                # answer = random.choice(final_list)
                game.game_number += 1
                game.game_status = False
                game.game_number_list.append(game.game_number)
                game.game_status_list.append(game.game_status)
                game.game_bad_guesses_list.append(game.game_bad_guesses)
                game.game_bad_guesses = 0
                index = []
                for i in range(len(default_guess)):
                    if default_guess[i] == "-":
                        index.append(i)
                letter_guess = list(answer)
                missed_list = []
                for i in index:
                    missed_list.append(letter_guess[i])
                game.game_missed_letters_list.append(missed_list)
                game.calculate_score()
                default_guess = ['-', '-', '-', '-']
                stringDB.randomise()
                guess.option_selection()

            elif option == "l":
                letter_l_counter += 1
                user_letter = input("Please enter your letter: ")
                # logic of handling letters
                letter_count = 0
                letter_guess = list(answer)
                for letter in letter_guess:
                    if letter == user_letter:
                        temp_index = (letter_guess.index(letter))
                        index = letter_guess.index(letter)
                        default_guess[index] = user_letter
                        letter_guess[temp_index] = '-'
                        letter_count += 1
                        check = letter_guess.count(letter)
                        if check == 0:
                            print("You found letter" + " '" + letter + "' " + str(letter_count) + " time")
                if "".join(default_guess) == answer:
                    print("You got it.")
                    answer_list.append(answer)
                    game.game_number += 1
                    game.game_number_list.append(game.game_number)
                    game.game_status = True
                    game.game_status_list.append(game.game_status)
                    game.game_bad_guesses_list.append(game.game_bad_guesses)
                    game.game_bad_guesses = 0
                    game.game_missed_letters_list.append([])
                    game.calculate_score()
                    stringDB.randomise()
                    print("Current guess:" + current_guess)
                    guess.option_selection()
                else:
                    print("".join(default_guess))
                    guess.option_selection()

            elif option == "q":

                print("Bye thank you for playing Your score is")

            else:
                print("Inappropriate option. Please choose again")
                guess.option_selection()

class Game:
    game_number = 0
    game_number_list = []
    game_status = bool
    game_status_list = []
    game_bad_guesses = 0
    game_bad_guesses_list = []
    game_missed_letters_list = []
    game_score = 0.0
    game_score_list = []
    score_dictionary = {'a': 8.17, 'b': 1.49, 'c': 2.78, 'd': 4.25, 'e': 12.20,
                        'f': 2.23, 'g': 2.02, 'h': 6.09, 'i': 6.97, 'j': 0.15, 'k': 0.77,
                        'l': 4.03, 'm': 2.41, 'n': 6.75, 'o': 7.51, 'p': 1.93, 'q': 0.10,
                        'r': 5.99, 's': 6.33, 't': 9.06, 'u': 2.76, 'v': 0.98, 'w': 2.36,
                        'x': 0.15, 'y': 1.97, 'z': 0.07
                        }

    def game_variables(self):
        global answer_list
        game_record = []
        #print(game.game_missed_letters_list)
        i = 0
        for ans in answer_list:
            record = [game.game_number_list[i], ans, game.game_status_list[i],
                      game.game_bad_guesses_list[i],
                      len(game.game_missed_letters_list[i]),
                      game.game_missed_letters_list[i], game.game_score_list[i]
                      ]
            game_record.append(record)
            i += 1
        game.score(game_record)

    def calculate_score(self):
        global highest_score, letter_l_counter, bad_guess_counter
        missed_letter_score = 0
        x = game.game_missed_letters_list[game.game_number - 1]
        for i in x:
            missed_letter_score += game.score_dictionary.get(i)
        # print(highest_score)
        # print(missed_letter_score)
        temp_score = highest_score - missed_letter_score
        if letter_l_counter != 0:
            temp_score = temp_score / letter_l_counter
        while bad_guess_counter > 0:
            temp_score = temp_score - (temp_score * 10) / 100
            bad_guess_counter -= 1
        temp_score = round(temp_score, 2)
        print(temp_score)
        game.game_score_list.append(temp_score)
        #print(game.game_score_list)

    def score(self, game_record):
        self.game_record = game_record
        final_score = 0
        t = PrettyTable(['Game No', 'Word', 'Status', 'Bad Guesses', 'Missed Letters', 'Score'])
        for record in self.game_record:
            record_number = record[0]
            record_word = record[1]
            record_status = record[2]
            record_badguesses = record[3]
            record_missedletters = record[4]
            record_score = record[6]
            if record_status:
                record_status = "Success"
            else:
                record_status = "Gave Up"
            t.add_row([record_number, record_word, record_status, record_badguesses,
                       record_missedletters, record_score])
            final_score += record_score
        print(t)
        print("Final score is :" + str(final_score))


class StringDatabase:
    def load_text_file(self):
        global final_list
        four_letters = open("four_letters.txt", "r")
        all_words = four_letters.readlines()
        final_list = []
        for word in all_words:
            raw_list = word.strip('\n').split(' ')
            final_list = final_list + raw_list
        stringDB.randomise()
        # print(answer)
        # print(highest_score)

    def randomise(self):
        global answer, highest_score
        highest_score = 0
        #answer = "dipt"
        answer = random.choice(final_list)
        list_of_answer = list(answer)
        for i in list_of_answer:
            highest_score += game.score_dictionary.get(i)


stringDB = StringDatabase()
guess = Guess()
game = Game()

stringDB.load_text_file()
guess.main_menu()
game.game_variables()
