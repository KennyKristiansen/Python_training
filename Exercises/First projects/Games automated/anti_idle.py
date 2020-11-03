#! python3
"""Automates the game Anti-Idle"""

import logging, os, time, sys, datetime
import pyautogui as auto

auto.PAUSE = 0.05
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)  # uncomment to block debug log messages
# logging.debug('This is a log message.')

auto.FAILSAFE = True
pictures_location = r'C:\Users\kenny\Desktop\GamesDoneQuick\anti_idle'
os.chdir(pictures_location)


def run(mining_button):
    get_game_region()
    # button_game()
    mining(mining_button)


def click(x, y):
    auto.click(game_region[0] + x, game_region[1] + y, interval=0.25)


def locate(image_location):
    auto.locateOnScreen(image_location, region=(game_region[0], game_region[1], game_region[2], game_region[3]), )


def get_game_region():
    global game_region
    top_left_corner = auto.locateOnScreen("top_left_corner.png", confidence=0.96)
    game_left = top_left_corner[0]
    game_top = top_left_corner[1]
    game_width = 815
    game_height = 850
    game_region = (game_left, game_top, game_width, game_height)
    auto.click(game_region[0] + 1, game_region[1] + 1, interval=0.5)


def button_game():
    # Figure out the line
    get_game_region()
    button_line_found = False
    last_center = [300, 0]
    x_max = 0
    x_min = 1000
    y_max = 0
    y_min = 1000
    count = 0
    while button_line_found is False:
        button = auto.locateOnScreen("button.png", region=(game_region[0] + 40, game_region[1] + 200, 600, 200),
                                     confidence=0.86)
        while count != 100:
            button = auto.locateOnScreen("button.png", region=(game_region[0] + 40, game_region[1] + 200, 600, 200),
                                         confidence=0.86)
            time.sleep(0.1)
            if button is not None:
                center = auto.center(button)
                if center[0] > last_center[0]:
                    if center[0] > x_max:
                        x_max = center[0]
                        y_max = center[1]
                if last_center[0] > center[0]:
                    if x_min > center[0]:
                        x_min = center[0]
                        y_min = center[1]
                auto.click(center[0], center[1])
                last_center = center
                print(x_max, x_min, count)
                count += 1
        print('moving on')
        button_in_end_position = False
        while button_in_end_position is False:
            button = auto.locateOnScreen("button.png", region=(game_region[0] + 40, game_region[1] + 200, 600, 200),
                                         confidence=0.86)
            if button is not None:
                center = auto.center(button)
                if center[0] < x_max:
                    print(center[0], '=', x_max)
                    auto.click(center[0], center[1])

                if center[0] > x_max:
                    x_max = center[0]
                    y_max = center[1]

                if center[0] >= x_max-3:
                    button_in_end_position = True

        print('Button line is found')
        button_line_found = True

    time_len = 6.5
    time_diff_left = 1
    time_diff_right = 1
    while True:
        auto.keyDown('shift')
        auto.dragTo(x_min, y_min, time_len * time_diff_left)
        auto.keyUp('shift')
        time.sleep(1.5)
        button = auto.locateOnScreen("button.png", region=(game_region[0] + 40, game_region[1] + 200, 600, 200),
                                     confidence=0.86)
        print(button)
        if button is not None:
            center = auto.center(button)
            time_diff_left = float((x_min / center[0]))
            print(time_diff_left)
        auto.keyDown('shift')
        auto.dragTo(x_max, y_max, time_len * time_diff_right)
        auto.keyUp('shift')

        time.sleep(1.5)
        button = auto.locateOnScreen("button.png", region=(game_region[0] + 40, game_region[1] + 200, 600, 200),
                                     confidence=0.86)
        print(button)
        if button is not None:
            center = auto.center(button)
            time_diff_right = float((x_min / center[0]))
            print(x_max, center[0], time_diff_right)

        button_in_end_position = False
        while button_in_end_position is False:
            button = auto.locateOnScreen("button.png", region=(game_region[0] + 40, game_region[1] + 200, 600, 200),
                                         confidence=0.86)
            if button is not None:
                center = auto.center(button)
                if center[0] < x_max:
                    auto.click(center[0], center[1])

                if center[0] > x_max:
                    x_max = center[0]
                    y_max = center[1]

                if center[0] >= x_max-3:
                    button_in_end_position = True





def mining(button):
    count = 0
    while True:
        # print('pressing x')
        auto.keyDown('c')
        time.sleep(1)
        auto.keyUp('c')
        if count == 20:
            print('mana refilled')
            auto.keyDown('w')
            time.sleep(0.5)
            auto.keyUp('w')
            count = 0
        count += 1


import random


def ultimate_avoidance():
    get_game_region()
    time.sleep(5)
    ultimate_game_region = (game_region[0] + 16, game_region[1] + 136, 620, 330)

    while True:
        center = auto.center(ultimate_game_region)
        auto.moveTo(center)
        cursor_position = center
        print('here')
        while True:
            center = auto.locateOnScreen('ultimate_clear.png',
                                         region=(cursor_position[0] - 10, cursor_position[1] - 10, 20, 20),
                                         confidence=1)
            print(center)
            if center is not None:
                print('no move')
                continue
            left = auto.locateOnScreen('ultimate_clear.png',
                                       region=(cursor_position[0] - 20, cursor_position[1] - 10, 20, 20), confidence=1)
            if left is not None:
                auto.move(-5, 0)
                print('move left')
            right = auto.locateOnScreen('ultimate_clear.png',
                                        region=(cursor_position[0] + 20, cursor_position[1] - 10, 20, 20), confidence=1)
            if right is not None:
                auto.move(5, 0)
                print('move right')
            top = auto.locateOnScreen('ultimate_clear.png',
                                      region=(cursor_position[0] - 10, cursor_position[1] - 20, 20, 20), confidence=1)
            if top is not None:
                auto.move(0, -5)
                print('move up')
            bottom = auto.locateOnScreen('ultimate_clear.png',
                                         region=(cursor_position[0] - 10, cursor_position[1] + 10, 20, 20),
                                         confidence=1)

            if bottom is not None:
                auto.move(0, 5)
                print('move down')


def mouse():
    filename = random.randint(0, 1000)
    print(filename)
    get_game_region()
    seconds = time.time()
    print('grabbing')
    print(auto.getActiveWindow())
    auto.screenshot(str(filename) + '.png', region=game_region)
    seconds_total = time.time() - seconds
    print('done in ' + str(seconds_total))


def defender():
    get_game_region()
    while True:
        boss = auto.locateOnScreen('boss.png', region=(game_region[0] + 440, game_region[1] + 290, 20, 30))
        if boss is not None:
            boss_fight = True
            while boss_fight is True:
                boss = auto.locateOnScreen('boss.png', region=(game_region[0] + 440, game_region[1] + 290, 20, 30))
                if boss is not None:
                    print('Boss fight')
                    auto.keyDown('c')
                    auto.keyUp('c')
                    auto.keyDown('s')
                    auto.keyUp('s')
                else:
                    auto.keyDown('shift')
                    print('defend')
                enemy = auto.locateOnScreen('clear.png', region=(game_region[0] + 110, game_region[1] + 260, 30, 35))
                if enemy is None:
                    boss_fight = False

        area_clear = auto.locateOnScreen('area_clear.png', region=(game_region[0] + 120, game_region[1] + 275, 490, 10))
        if area_clear is not None:
            pass
        else:
            try:
                enemy = auto.locateOnScreen('clear.png', region=(game_region[0] + 110, game_region[1] + 260, 30, 35))
                if enemy is not None:
                    print('attack')
                    auto.keyUp('shift')
                    auto.keyDown('c')
                    auto.keyUp('c')
                    auto.keyDown('s')
                    auto.keyUp('s')
                else:
                    auto.keyDown('shift')
                    print('defend')

            except:
                pass


def fishing():
    get_game_region()
    auto.moveTo(game_region[0] + 510, game_region[1] + 500)
    while True:
        time_start = time.perf_counter()
        fish_perfect = auto.locateOnScreen('fish_click.png', region=(game_region[0] + 470, game_region[1] + 500, 35, 2),
                                           confidence=0.98)
        if fish_perfect is None:
            auto.keyDown('space')
            auto.keyUp('space')
        print(time.perf_counter() - time_start)
        print(' ')


def wack_a_mole():
    get_game_region()
    time.sleep(5)
    ultimate_game_region = (game_region[0] + 25, game_region[1] + 165, 600, 300)

    while True:
        center = auto.center(ultimate_game_region)
        auto.moveTo(center)
        while True:
            smiley = auto.locateOnScreen('smiley.png', region=ultimate_game_region, confidence=0.75)
            if smiley is not None:
                auto.click(smiley)
            icon = auto.locateOnScreen('icon.png', region=ultimate_game_region, confidence=0.8)
            if icon is not None:
                auto.click(icon)
            multiplier = auto.locateOnScreen('multiplier.png', region=ultimate_game_region, confidence=0.8)
            time.sleep(0.2)
            # white_coin = auto.locateOnScreen('white_coin.png', region=ultimate_game_region, confidence=0.85)
            if multiplier is not None:
                auto.click(multiplier)
            # if white_coin is not None:
            #    auto.click(white_coin)


dungeon_location = r'C:\Users\kenny\Desktop\GamesDoneQuick\anti_idle\dungeon'


def dungeon():
    get_game_region()
    os.chdir(dungeon_location)
    print(game_region)
    completed = 0
    timed_runs = []
    while True:
        entrance = auto.locateOnScreen('entrance.png', region=game_region, confidence=0.95)
        if entrance is not None:
            complete = False
            click(330, 225)  # clicks dungeon door
            time.sleep(0.5)
            click((100), 225)  # clicks free option
            row = 0
            column = 0
            move_left = True
            move_right = False
            start = time.time()
            while True:
                if complete is True:
                    completed += 1
                    print('Dungeon completed ' + str(completed) + ' times.')
                    time_taken = stop - start
                    timed_runs.append(int(time_taken))
                    print('This run took ' + str(round(int(time_taken), 0)) + ' seconds')
                    total_time = 0
                    for times in range(len(timed_runs)):
                        total_time += timed_runs[times]
                    average_time = total_time / len(timed_runs)
                    print('The average run takes ' + str(round(int(average_time), 0)) + ' seconds.')

                    break
                auto.keyUp('c')
                time.sleep(0.1)
                auto.keyDown('c')
                arrow_left = auto.locateOnScreen('arrow_left.png',
                                                 region=(game_region[0] + 20, game_region[1] + 200, 50, 50),
                                                 confidence=0.93)
                arrow_up = auto.locateOnScreen('arrow_up.png',
                                               region=(game_region[0] + 300, game_region[1] + 150, 50, 50),
                                               confidence=0.93)
                # arrow_right = auto.locateOnScreen('arrow_right.png', region=(game_region[0] + 575, game_region[1] + 200, 50, 50), confidence=0.93)
                chest = auto.locateOnScreen('chest.png', region=game_region, confidence=0.95)
                if chest is not None:
                    auto.keyDown('shift')
                    time.sleep(0.25)
                    auto.keyUp('shift')
                time.sleep(1)

                if move_left is True:
                    if arrow_up is not None:
                        click(40, 225)  # clicking arrow left
                        column += 1
                        time.sleep(1)
                        if column is 5:
                            move_right = True
                            move_left = False
                            time.sleep(1)
                            while column is 5:
                                chest = auto.locateOnScreen('chest.png', region=game_region, confidence=0.95)
                                if chest is not None:
                                    auto.keyDown('shift')
                                    time.sleep(0.25)
                                    auto.keyUp('shift')
                                arrow_up = auto.locateOnScreen('arrow_up.png', region=(
                                game_region[0] + 300, game_region[1] + 150, 50, 50), confidence=0.96)
                                if arrow_up is not None:
                                    click(320, 170)
                                    row += 1
                                    time.sleep(1)
                                    break
                # arrow_left = auto.locateOnScreen('arrow_left.png', region=(game_region[0] + 20, game_region[1] + 200, 50, 50), confidence=0.93)
                # arrow_up = auto.locateOnScreen('arrow_up.png', region=(game_region[0] + 300, game_region[1] + 150, 50, 50), confidence=0.93)
                arrow_right = auto.locateOnScreen('arrow_right.png',
                                                  region=(game_region[0] + 575, game_region[1] + 200, 50, 50),
                                                  confidence=0.93)
                if chest is not None:
                    auto.keyDown('shift')
                    time.sleep(0.25)
                    auto.keyUp('shift')

                if move_right is True:
                    if arrow_right is not None:
                        click(600, 220)
                        column -= 1
                        time.sleep(1)
                        if column is 0:
                            move_right = False
                            move_left = True
                            time.sleep(1)
                            while column is 0:
                                chest = auto.locateOnScreen('chest.png', region=game_region, confidence=0.95)
                                if chest is not None:
                                    auto.keyDown('shift')
                                    time.sleep(0.25)
                                    auto.keyUp('shift')
                                if row is 5:
                                    if column is 0:
                                        click(610, 520)
                                        click(360, 500)
                                        complete = True
                                        stop = time.time()
                                        break
                                arrow_up = auto.locateOnScreen('arrow_up.png', region=(
                                game_region[0] + 300, game_region[1] + 150, 50, 50), confidence=0.96)
                                if arrow_up is not None:
                                    click(320, 170)
                                    row += 1
                                    time.sleep(1)
                                    break


doom_location = r'C:\Users\kenny\Desktop\GamesDoneQuick\anti_idle\doom'


def doom():
    get_game_region()
    os.chdir(doom_location)
    enemy_time_dict = {'1': 2, '2': 2, '3': 2, '4': 2, '5': 2, '6': 2, '7': 2, '8': 2, '9': 1.5, '10': 1.5, '11': 1.5,
                       '12': 0, '13': 0, '14': 0, '15': 0, '16': 0, '17': 0, '18': 0, '19': 0, }
    while True:
        enemy_count = 0
        entrance = auto.locateOnScreen('doom_entrance.png', region=game_region, confidence=0.83)
        if entrance is not None:
            click(490, 125)
        else:
            continue
        auto.keyDown('c')
        time.sleep(3)
        auto.keyUp('c')
        empty_arena = auto.locateOnScreen('empty_arena.png', region=game_region, confidence=0.98)
        if empty_arena is None:
            continue
        while True:
            if enemy_count == 18:
                break
            empty_arena = auto.locateOnScreen('empty_arena.png', region=game_region, confidence=0.98)
            if empty_arena is None:
                enemy_present = True
                enemy_spawn = time.perf_counter()
                auto.keyDown('c')
                enemy_count += 1
                print('enemy number ' + str(enemy_count) + ' has spawned.')
                while enemy_present is True:
                    empty_arena = auto.locateOnScreen('empty_arena.png', region=game_region, confidence=0.98)
                    if empty_arena is not None:
                        enemy_present = False
                        enemy_death = time.perf_counter()
                        auto.keyUp('c')
                        auto.keyDown('w')
                        time.sleep(1)
                        auto.keyUp('w')
                        taunt = enemy_time_dict[str(int(enemy_count) + 1)]
                        auto.keyDown('c')
                        if taunt > 0:
                            time.sleep(int(taunt))
                        auto.keyUp('c')
                        enemy_time = enemy_death - enemy_spawn
                        enemy_time = int(enemy_time)
                        if 10 > enemy_time:
                            if 2 > enemy_time_dict[str(enemy_count)]:
                                time_to_add = ((10 - enemy_time) / 50)
                                enemy_time_dict[str(enemy_count)] = enemy_time_dict[str(enemy_count)] + time_to_add
                                if enemy_time_dict[str(enemy_count)] > 2:
                                    enemy_time_dict[str(enemy_count)] = 2
                                print(enemy_time_dict[str(enemy_count)])

                        if enemy_time > 15:
                            if enemy_time_dict[str(enemy_count)] > 0:
                                time_to_deduct = ((enemy_time - 15) / 50)
                                enemy_time_dict[str(enemy_count)] = enemy_time_dict[str(enemy_count)] - time_to_deduct
                                if 0 > enemy_time_dict[str(enemy_count)]:
                                    enemy_time_dict[str(enemy_count)] = 0
                                print(enemy_time_dict[str(enemy_count)])
                        print(('Taunting enemy %s for ' + str(taunt) + ' seconds.') % (str(int(enemy_count) + 1)))
                    if enemy_count == 18:
                        print('Tower finished')
                        break


# doom()
# dungeon()
# button_game()
# wack_a_mole()ccc
fishing()
# defender()
# mouse()
# run('x')
# ultimate_avoidance()
