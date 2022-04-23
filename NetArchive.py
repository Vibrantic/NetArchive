import json
import sys, time, os, random

char_set = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
            "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
os.system("cls")
os.system('color 2')


def start_screen():
    t = 0
    while t < 30:
        print(random.randrange(1, 5) * " ", random.choice(char_set), random.randrange(1, 5) * " ",
              random.choice(char_set),
              random.randrange(1, 5) * " ", random.choice(char_set), random.randrange(1, 5) * " ",
              random.choice(char_set),
              random.randrange(1, 5) * " ", random.choice(char_set), random.randrange(1, 5) * " ",
              random.choice(char_set),
              random.randrange(1, 5) * " ", random.choice(char_set), random.randrange(1, 5) * " ",
              random.choice(char_set),
              random.randrange(1, 5) * " ", random.choice(char_set), random.randrange(1, 5) * " ",
              random.choice(char_set),
              random.randrange(1, 5) * " ", random.choice(char_set), random.randrange(1, 5) * " ",
              random.choice(char_set),
              random.randrange(1, 5) * " ", random.choice(char_set), random.randrange(1, 5) * " ",
              random.choice(char_set),
              random.randrange(1, 5) * " ", random.choice(char_set), random.randrange(1, 5) * " ",
              random.choice(char_set),
              random.randrange(1, 5) * " ", random.choice(char_set), random.randrange(1, 5) * " ",
              random.choice(char_set),
              random.randrange(1, 5) * " ", random.choice(char_set), random.randrange(1, 5) * " ",
              random.choice(char_set),
              random.randrange(1, 5) * " ", random.choice(char_set), random.randrange(1, 5) * " ",
              random.choice(char_set),
              random.randrange(1, 5) * " ", random.choice(char_set), random.randrange(1, 5) * " ",
              random.choice(char_set),
              random.randrange(1, 5) * " ", random.choice(char_set), random.randrange(1, 5) * " ",
              random.choice(char_set),
              random.randrange(1, 5) * " ", random.choice(char_set), random.randrange(1, 5) * " ",
              random.choice(char_set),
              random.randrange(1, 5) * " ", random.choice(char_set), random.randrange(1, 5) * " ",
              random.choice(char_set),
              )

        t += 1
        time.sleep(0.05)
        if t == 30:
            os.system("cls")
        else:
            pass


def new_game():
    print(f"Sucess!")
    pass


def user_input():
    while True:
        try:
            ui = input(">>:")
            if len(ui) == 0:
                raise ValueError("Empty string!")

            elif ui == "n" or "new":
                new_game()

        except ValueError as error:
            print(error)


start_screen()
user_input()
