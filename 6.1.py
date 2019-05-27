import json

class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds

class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


if __name__=="__main__":

    player_list=[]

    kev_dur = BasketballPlayer(first_name="Kevin", last_name="Durant", height_cm=210, weight_kg=108, points=27.2, rebounds=7.1, assists=4)

    print(kev_dur.last_name)
    print(kev_dur.rebounds)
    print(kev_dur.weight_to_lbs())

    messi = FootballPlayer(first_name="Lionel", last_name="Messi", height_cm=170, weight_kg=67, goals=575, yellow_cards=67, red_cards=0)

    print(messi.first_name)
    print(messi.goals)
    print(messi.weight_to_lbs())

    print("")
    print(50*"*")
    print("")

    while True:
        new_player=input("Do you want to add a new player to the database? (y/n): ")
        if new_player in ("y","yes","Y","Yes"):
            ## Input general player properties
            player_shortcut=input("Define a shortcut for your new player: ")

            first_name_new=input("First name: ")
            last_name_new=input("Last name: ")
            height_cm_new=int(input("Height in cm: "))
            weight_kg_new=int(input("weight in kg: "))

            player_type_input=input("(a) Basketball Player or (b) Football Player?: ")
            if player_type_input in ("a","A","(a)","(A)"):
                ## input player type specific properties
                player_type=BasketballPlayer
                var1=float(input("Points: "))
                var2=float(input("Rebounds: "))
                var3=float(input("Assists: "))
                ## Creating a new Player object + saving into player_list
                player_shortcut = player_type(first_name=first_name_new, last_name=last_name_new,
                                              height_cm=height_cm_new, weight_kg=weight_kg_new, points=var1,
                                              rebounds=var2, assists=var3)
                player_list.append(player_shortcut)

            elif player_type_input in ("b","B","(b)","(B)"):
                ## input player type specific properties
                player_type=FootballPlayer
                var1=int(input("Goals: "))
                var2=int(input("Yellow Cards: "))
                var3=int(input("Red Cards: "))
                ## Creating a new Player object + saving into player_list
                player_shortcut = player_type(first_name=first_name_new, last_name=last_name_new,
                                              height_cm=height_cm_new, weight_kg=weight_kg_new, goals=var1, yellow_cards=var2,
                                              red_cards=var3)
                player_list.append(player_shortcut)

            else:
                print("Error, please choose (a) or (b).")

        else:
            with open("Players.txt", "r") as f:
                player_list_dict = json.loads(f.read())

            with open("Players.txt","w") as f:
                for player_shortcut in player_list:
                    player_list_dict.append(player_shortcut.__dict__)
                f.write(json.dumps(player_list_dict))
            print("")
            print("Thank you, the Playerlist was saved in file Players.txt! Goodbye!")
            break
