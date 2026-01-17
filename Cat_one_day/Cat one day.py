import os
import sys
import time

def cat_anim():
    time.sleep(1)
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(r"""
          /\_/\
         ( o.o )
          > ^ <
         /     \
        |       |\__
         \_____/  `*)
        """)
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(r"""
          /\_/\
         ( -.- )
          > ^ <
         /     \
        |       |\__
         \_____/  `*)
        """)
        time.sleep(0.2)

def start_game():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Under Construction")

def list_score():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Under Construction")

def exit_game():
    os.system('cls' if os.name == 'nt' else 'clear')
    ans_1=input("Вы уверены, что хотите выйти из игры?(Y/N): ")
    match ans_1:
        case "Y" | "y":
            print("До встречи!")
            sys.exit()
        case "N" | "n":
            return

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Кошачий переполох")
        print("""\t1. Играть!
        \t2. Таблица рекордов.
        \t3. Выход :(""")
        ans=int(input("Выберите пункт меню: "))
        match ans:
            case 1:
                start_game()
            case 2:
                list_score()
            case 3:
                exit_game()