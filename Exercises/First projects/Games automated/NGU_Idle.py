#! python3
"""Automates the game NGU Idle."""

import logging, pyautogui, os, time, sys, datetime
pyautogui.PAUSE = 0.05
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')
# logging.disable(logging.DEBUG) # uncomment to block debug log messages

pictures_location = r'C:\Users\kenny\Desktop\GamesDoneQuick\ngu_idle'
os.chdir(pictures_location)
global rebirths
rebirths = 0


def setup():
    global start_time
    start_time = time.time()
    call_get_game_region()
    call_menu_buttons_setup()
    call_basic_training()
    call_fight()
    call_adventure()


def main():
    call_fight()
    call_inventory()
    call_basic_training()
    call_augmentation()
    rebirth(900, start_time)
    if start_time == range(30, 60):
        call_adventure()


def call_get_game_region():
    global game_region
    top_left_corner = pyautogui.locateOnScreen("top_left_corner.png")
    game_left = top_left_corner[0]
    game_top = top_left_corner[1]
    game_width = 1197
    game_height = 747
    game_region = (game_left, game_top, game_width, game_height)
    pyautogui.click(game_region[0] + 1, game_region[1] + 1, interval=0.5)


def call_menu_buttons_setup():
    global training_button, fight_boss, money_pit, adventure, inventory, augmentation, time_machine, nuke, milk_fusion, safety_scissors
    buttons_x = game_region[0] + 290

    training_button = [buttons_x, game_region[1] + 55]

    fight_boss = [buttons_x, game_region[1] + 90]
    nuke = [game_region[0] + 775, game_region[1] + 185]

    money_pit = [buttons_x, game_region[1] + 125]

    adventure = [buttons_x, game_region[1] + 160]

    inventory = [buttons_x, game_region[1] + 200]

    augmentation = [buttons_x, game_region[1] + 235]
    milk_fusion = [game_region[0] + 672.5, game_region[1] + 408]
    safety_scissors = [game_region[0] + 675.2, game_region[1] + 325]

    time_machine = [buttons_x, game_region[1] + 310]


def call_basic_training():
    cap_x = game_region[0] + 1140
    idle = game_region[1] + 175
    regular = game_region[1] + 220
    strong = game_region[1] + 260
    parry = game_region[1] + 300
    piercing = game_region[1] + 345
    ultimate = game_region[1] + 390
    pyautogui.click(training_button[0], training_button[1], clicks=2, pause=1, interval=0.25)
    pyautogui.click(cap_x, idle, clicks=2, pause=0.25)
    pyautogui.click(cap_x, regular, clicks=2, pause=0.25)
    pyautogui.click(cap_x, strong, clicks=2, pause=0.25)
    pyautogui.click(cap_x, parry, clicks=2, pause=0.25)
    pyautogui.click(cap_x, piercing, clicks=2, pause=0.25)
    pyautogui.click(cap_x, ultimate, clicks=2, pause=0.25)


def call_fight():
    pyautogui.click(fight_boss[0], fight_boss[1], clicks=2, pause=1, interval=0.25)
    pyautogui.click(nuke[0], nuke[1], clicks=2, pause=5, interval=0.25)


def call_adventure():
    time.sleep(1)
    pyautogui.click(adventure[0], adventure[1], clicks=2, pause=1, interval=0.25)
    time.sleep(1)
    for i in range(3):
        pyautogui.press('right', pause=0.25)
        time.sleep(0.1)


def call_inventory():
    pyautogui.click(inventory[0], inventory[1], clicks=2, pause=1, interval=0.25)
    row_start_y = game_region[1] + 410
    row_start_x = game_region[0] + 435
    row_length = 12
    row_count = 3
    pyautogui.moveTo(game_region[0] + 600, game_region[1] + 80)
    pyautogui.press('a')

    for row in range(row_count):
        row_number = row * 60
        for length in range(row_length):
            row_count = length * 62.5
            pyautogui.moveTo(row_start_x + row_count, row_start_y + row_number)
            # pyautogui.press('a')
            pyautogui.press('d')


def call_augmentation():
    pyautogui.click(augmentation[0], augmentation[1], clicks=2, interval=0.25)
    pyautogui.click(safety_scissors[0], safety_scissors[1], clicks=2, interval=0.25)


def rebirth(time_before_rebirth, time_start):
    rebirth_time = time.time() - time_start
    # print(time.strftime('%M Minutes and %S seconds.', time.struct_time(time.gmtime(rebirth_time))))
    if rebirth_time > time_before_rebirth:
        global rebirths
        pyautogui.click(game_region[0] + 100, game_region[1] + 525, clicks=2, pause=1, interval=0.25)
        pyautogui.click(game_region[0] + 675, game_region[1] + 650, clicks=2, pause=1, interval=0.25)
        pyautogui.click(game_region[0] + 540, game_region[1] + 400, clicks=2, pause=1, interval=0.25)
        rebirths += 1
        print('Total number of rebirths: ' + str(rebirths))
        try:
            rebirth_yes = pyautogui.locateOnScreen("rebirth_yes.png")
            rebirth_yes_location = pyautogui.locateCenterOnScreen(rebirth_yes)
            pyautogui.leftClick(rebirth_yes_location[0], rebirth_yes_location[1])
            # pyautogui.click(game_region[0] + 540, game_region[1] + 400, clicks=2, pause=1)
        except:
            pass

        setup()


setup()
while True:
    main()
