import random, json, datetime

class Result():
    def __init__(self, attempts_obj, name_obj, date_obj, wrong_guesses_obj, correct_result_obj):
        self.attempts_obj = attempts_obj
        self.name_obj = name_obj
        self.date_obj = date_obj
        self.wrong_guesses_obj = wrong_guesses_obj
        self.correct_result_obj = correct_result_obj



class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def get_score_list():
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
        print(350 * "*")
        print("All scores: " + str(score_list))

        ## Sort the list based on a value within the dictionaries within the list
        from operator import itemgetter
        sorted_scores=sorted(score_list, key=itemgetter("attempts_obj"))
        print("Sorted scores: " + str(sorted_scores))
        print(350*"*")
        print("")

        ## Highscore output should only include top 3 results, so from index 0 to index 2
        for score_dict in sorted_scores[0:3]:
            print(color.BOLD + str(score_dict["attempts_obj"]) + color.END, " attempts, name: ", score_dict["name_obj"] + ", date: ", score_dict.get("date_obj"),", wrong guesses: " , color.RED + str(score_dict["wrong_guesses_obj"]) + color.END, ", secret number was: " , color.BOLD + color.BLUE + str(score_dict["correct_result_obj"])+ color.END)


def get_score_list_all():
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
        print(350 * "*")
        print("All scores: " + str(score_list))
        print(350*"*")
        print("")
        for score_dict in score_list:
            print(color.BOLD + str(score_dict["attempts_obj"]) + color.END, " attempts, name: ", score_dict["name_obj"] + ", date: ", score_dict.get("date_obj"),", wrong guesses: " , color.RED + str(score_dict["wrong_guesses_obj"]) + color.END, ", secret number was: " , color.BOLD + color.BLUE + str(score_dict["correct_result_obj"])+ color.END)


def play_game(level):
    secret = random.randint(1, 30)
    attempts = 0
    wrong_guesses = []  ## muss außerhalb der while loop definiert sein, weil ansonsten immer wieder die Liste geleert wird und nicht alle Fehlversuche gespeichert werden würden.
    correct_result = 0
    name = input("Please enter your name: ")
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())

    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))  ## Input without a value triggers error -> build if-clause to avoid error?
        attempts += 1

        if guess == secret:
            correct_result = guess
            score_data = Result(attempts,name, str(datetime.datetime.now()),wrong_guesses, correct_result)
            score_list.append(score_data.__dict__)

            with open("score_list.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))

            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break

        elif guess > secret and level == "easy":
            wrong_guesses.append(guess)
            print("Your guess is not correct... try something", color.BOLD + "smaller" + color.END, "(wrong guesses so far: ", wrong_guesses,")")
        elif guess < secret and level == "easy":
            wrong_guesses.append(guess)
            print("Your guess is not correct... try something", color.BOLD + "bigger" + color.END, "(wrong guesses so far: ", wrong_guesses,")")
        else:
            print("Your guess is not correct. Please try again")
