import os
import sys
import time
import textwrap  # <--- ОБЯЗАТЕЛЬНО ДОБАВЬ ЭТО В САМОЕ НАЧАЛО ФАЙЛА

def draw_box(lines):
    max_width = 70
    processed_lines = []
    for line in lines:
        if line == "---":
            processed_lines.append("---")
        elif not line:
            processed_lines.append("")
        else:
            processed_lines.extend(textwrap.wrap(line, width=max_width))
    content_lines = [l for l in processed_lines if l != "---"]
    if not content_lines:
        width = max_width
    else:
        width = max([len(line) for line in content_lines])
    print(f"╔{'═' * (width + 2)}╗")
    for line in processed_lines:
        if line == "---":
            print(f"╠{'═' * (width + 2)}╣")
        else:
            print(f"║ {line.ljust(width)} ║")
    print(f"╚{'═' * (width + 2)}╝")

def save_result(player_name, score, total_time):
    return

def draw_hud(current_lives, current_score):
    os.system('cls' if os.name == 'nt' else 'clear')
    stats=f"Жизни{"❤ " * current_lives} | Очки: {current_score}"
    print(stats.rjust(75))

def cat_anim():
    time.sleep(1)
    for i in range(5):
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
    os.system('cls' if os.name == 'nt' else 'clear')

def start_game():
    os.system('cls' if os.name == 'nt' else 'clear')
    player_name=input("Дай имя котику: ")
    lives=3
    score=0
    start_time=time.time()
    #Глава 1
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        draw_hud(lives, score)
        print(r"""
                   |\      _,,,---,,_
            ZZZzz /,`.-'`'    -.  ;-;;,_
                 |,4-  ) )-,_. ,\ (  `'-'
                '---''(_/--'  `-'\_)
        """)
        draw_box([f"{player_name} открывает один глаз. Солнечный луч медленно ползет по ковру, дразня \nпылинки. В квартире тихо, слышно только сопение кожаных мешков под одеялом. \n{player_name} потягивается, чувствуя каждую мышцу. Его желудок урчит так громко, что этот \nзвук мог бы разбудить соседей. Голод — не тетка, голод — это {player_name}. Пора действовать.",
                    "---",
                    "1. Прыгнуть хозяину на живот.",
                    "2. Пойти на кухню и орать.",
                    "3. Подрать диван."
                    ])
        ans=int(input("Ваш выбор: "))
        os.system('cls' if os.name == 'nt' else 'clear')
        match ans:
            case 1:
                lives-=1
                input(f"-1 жизнь.\n{player_name} делает «бомбочку» на спящего человека. Хозяин с перепугу рефлекторно откидывает кота. \nПолет в стену заканчивается больно.")
            case 2:
                score+=20
                input(f"+20 очков.\n{player_name} славно поточил когти. Диван испорчен, а {player_name} доволен.")
            case 3:
                score+=10
                input(f"+10 очков.\n{player_name} идет на кухню и выдает требовательное «МЯУ!». Сонный хозяин, чтобы заткнуть этот сирену, насыпает полную миску корма.")
            case _:
                print("Выбор у тебя не особо велик...")
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("В чем дело? Надо цифру ввести, а не букву")
    os.system('cls' if os.name == 'nt' else 'clear')
    #Глава 2
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        draw_hud(lives, score)
        draw_box([f"Квартира пуста. Кожаные мешки ушли добывать ресурсы, оставив {player_name} полноправным властелином этих земель. \nНа подоконнике красуется кактус. Тишину нарушает лишь наглое жужжание. На оконном стекле сидит ОНА. \nЖирная, черная муха. Она потирает лапки, словно насмехаясь над хищником. \n{player_name} чувствует, как дергается его хвост. Инстинкт убийцы проснулся.",
                    "---",
                    "1. Устроить засаду на подоконнике.",
                    "2. Просто поспать в луче солнца.",
                    "3. Съесть кактус."
                    ])
        ans=int(input("Ваш выбор: "))
        os.system('cls' if os.name == 'nt' else 'clear')
        match ans:
            case 1:
                score+=20
                input(f"+20 очков.\nРезкий прыжок! ХВАТЬ! Муха оказывается в зубах. {player_name} хрустит добычей.")
            case 2:
                score+=10
                input(f"+10 очков.\n{player_name} игнорирует муху и растекается лужицей на солнечном пятне. Энергия восстанавливается.")
            case 3:
                lives-=1
                input(f"-1 жизнь.\n{player_name} кусает «зеленую муху». Ошибка! Рот полон иголок. Он бегает и плюется.")
            case _:
                print("Выбор у тебя не особо велик...")
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("В чем дело? Надо цифру ввести, а не букву")
    #Глава 3
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        draw_hud(lives, score)
        print(r"""
                   .---.
                 _/_____\_
                (_________)  <-- РОБОТ-УБИЙЦА
                 |_______|
               __|_______|__
              /             \
             |               |
             |  ВЖЖЖУУУХ!!!  |
             |_______________|
        """)
        draw_box([f"Внезапную тишину разрывает адский рев. Из угла выезжает ОН — Робот-пылесос. \nКруглый диск дьявола, пожиратель носков и враг всего живого. {player_name} шипит, \nвыгибая спину дугой. Чудовище медленно, но верно ползет в сторону любимой \nлежанки кота. Это война.",
                    "---",
                    "1. Атаковать кнопку выключения.",
                    "2. Занять высоту на холодильнике.",
                    "3. Понюхать вращающуюся щетку."
                    ])
        ans=int(input("Ваш выбор: "))
        os.system('cls' if os.name == 'nt' else 'clear')
        match ans:
            case 1:
                score+=10
                input(f"+10 очков.\n{player_name} занимает стратегическую высоту. Робот ползает внизу, бессильный достать царя горы.")
            case 2:
                score+=20
                input(f"+20 очков.\nСерия ударов лапой! БИП! Огни гаснут, монстр затих. {player_name} победил восстание машин.")
            case 3:
                lives-=1
                input(f"-1 жизнь.\n{player_name} сует нос под бампер. ВЖУХ! Усы намотало на валик! Пришлось вырываться силой, оставив клок шерсти.")
            case _:
                print("Выбор у тебя не особо велик...")
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("В чем дело? Надо цифру ввести, а не букву")
    if lives<=0:
        end_time=time.time()
        total_time=end_time-start_time
        print(f"Ты умер... \nТвои очки:{score}\nВремя прохождения:{total_time}\n")
        input("Нажми любую клавишу чтобы вернуться в меню...")
        return
    #Глава 4
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        draw_hud(lives, score)
        draw_box([f"Хозяева вернулись. На кухне пахнет жареной курицей так сильно, что у {player_name} \nкружится голова. Хозяин отвернулся, нарезая салат. На краю стола стоит тарелка с \nостывающими кусочками филе. Этот запах сводит с ума.",
                    "---",
                    "1. Прыгнуть на плиту.",
                    "2. Сделать милые глазки.",
                    "3. Украсть курицу."
                    ])
        ans=int(input("Ваш выбор: "))
        os.system('cls' if os.name == 'nt' else 'clear')
        match ans:
            case 1:
                lives-=1
                input(f"-1 жизнь.\n{player_name} промахивается мимо стола и приземляется на горячую конфорку. ПШШШ! Запах паленой шерсти и дикий визг.\n-1 жизнь")
            case 2:
                score+=10
                input(f"+10 очков.\n{player_name} трется об ноги и мурчит. Хозяин тает: «Ну на, не плачь». Легальный кусочек получен.\n+10 очков!")
            case 3:
                score+=20
                input("+20 очков.\nЛовкость лап и никакого мошенничества. Пока хозяин отвернулся, кусок филе исчез под диван. Вкусно!")
            case _:
                print("Выбор у тебя не особо велик...")
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("В чем дело? Надо цифру ввести, а не букву")
    if lives<=0:
        end_time = time.time()
        total_time = end_time - start_time
        print(f"Ты умер... \nТвои очки:{score}\nВремя прохождения:{total_time}\n")
        input("Нажми любую клавишу чтобы вернуться в меню...")
        return
    #Глава 5
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        draw_hud(lives, score)
        draw_box([f"Глубокая ночь. Луна светит в окно. Все нормальные существ спят, но у {player_name} \nрасширяются зрачки. Древние демоны скорости вселяются в его пушистое тело. \nЭнергия переполняет лапы. Ему нужно бежать. Быстро. Везде. СЕЙЧАС.",
                    "---",
                    "1. Уронить вазу.",
                    "2. Влететь в дверь.",
                    "3. Паркур по стенам."
                    ])
        ans=int(input("Ваш выбор: "))
        os.system('cls' if os.name == 'nt' else 'clear')
        match ans:
            case 1:
                score+=20
                input(f"+20 очков.\nЛапа толкает фарфор. БДЫЩ!!! Осколки везде. Хозяин орет, но {player_name} доволен хаосом.")
            case 2:
                lives-=1
                input("-1 жизнь.\nРазгон до 100 км/ч... и удар головой о закрытую стеклянную дверь. БОНЬК! Птички в глазах.")
            case 3:
                score+=10
                input(f"+10 очков.\n{player_name} бегает по стенам коридора, не касаясь пола. Гравитация для слабаков.")
            case _:
                print("Выбор у тебя не особо велик...")
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("В чем дело? Надо цифру ввести, а не букву")
    if lives<=0:
        end_time = time.time()
        total_time = end_time - start_time
        save_result(player_name, score, total_time)
        print(f"Ты умер... \nТвои очки:{score}\nВремя прохождения:{total_time}\n")
        input("Нажми любую клавишу чтобы вернуться в меню...")
        return
    elif score<100:
        end_time = time.time()
        total_time = end_time - start_time
        save_result(player_name, score, total_time)
        print(r"""
            __________________
            |                |
            | ТЫ ПОБЕДИЛ!    |
            | КОРОЛЬ КВАРТИРЫ|
            |________________|
                |\__/| ||
                (•ㅅ•) ||
                / 　 づ        
        """)
    elif score==100:
        end_time = time.time()
        total_time = end_time - start_time
        save_result(player_name, score, total_time)
        print(r"""
            __________________
            |                |
            | ТЫ ПОБЕДИЛ!    |
            | КОРОЛЬ КВАРТИРЫ|
            |________________|
                |\__/| ||
                (•ㅅ•) ||
                / 　 づ        
        """)
        input(f"Ого! котик {player_name} набрал максимальное кол-во очков!\nПоздравляем!")
    return

def list_score():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Under Construction")
    return

def exit_game():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        ans_1=input("Вы уверены, что хотите выйти из игры?(Y/N): ")
        os.system('cls' if os.name == 'nt' else 'clear')
        match ans_1:
            case "Y" | "y":
                print("До встречи!")
                sys.exit()
            case "N" | "n":
                return
            case _:
                print("Тебе же сказали y/n. А ты что хуйню пишешь?")

def main():
    while True:
        try:
            draw_box([
            "Кошачий переполох♥",
            "---",
            "1. Играть!",
            "2. Таблица рекордов.",
            "3. Котик?!",
            "4. Выход :("
            ])
            ans=int(input("Выберите цифру меню: "))
            os.system('cls' if os.name == 'nt' else 'clear')
            match ans:
                case 1:
                    start_game()
                case 2:
                    list_score()
                case 3:
                    cat_anim()
                case 4:
                    exit_game()
                    break
                case _:
                    print("А ты что, видишь тут больше 4??")
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Ты ебанат?) Попросили же блять цифру...")

if __name__ == "__main__":
    main()