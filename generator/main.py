import sys
from random import shuffle
from random import choice


def execute(params):

    validate_parameters(params)

    input_list = str(params[1]).strip()
    output_list = str(params[2]).strip()

    game_list = read_file(input_list)

    platforms = sort_platform(game_list)

    game_text = sort_games(platforms, game_list)

    save(output_list, game_text)


def validate_parameters(params):

    if len(params) != 3:
        raise Exception(
            'must supply input_list, output_list_path.')

    if not str(params[1]).strip():
        raise Exception('must supply input_list parameters')

    if not str(params[2]).strip():
        raise Exception('must supply output_list_path parameters')


def read_file(input_list_path):

    with open(input_list_path, 'r') as file:
        game_list = list(file)

    # remove line breaks
    game_list = [line.strip() for line in game_list]

    return game_list


def sort_platform(game_list):

    platform_list_raw = [game.split(';')[1] for game in game_list]
    platform_list = list(set(platform_list_raw))

    shuffle(platform_list)

    return platform_list


def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)


def sort_games(platform_list, game_list):

    sorted_game_list = list()

    for game in game_list:

        for platform in platform_list:
            filtered_games = [item.split(';')[0]
                              for item in game_list if platform in item]

            random_game = choice(filtered_games)

            # if the pick has a number try to get the first occurrence previous game
            if has_numbers(random_game):

                game_literal_name = ''.join(
                    [item for item in random_game if not item.isdigit()])

                found_games = [item.split(';')[0]
                               for item in game_list if game_literal_name.strip() in item]

                if len(found_games) > 1:
                    found_games.sort(key=str.lower)

                    for game_found in found_games:
                        if not game_found in sorted_game_list:
                            random_game = game_found
                            break

            if not random_game in sorted_game_list:
                sorted_game_list.append(random_game)

    return sorted_game_list


def save(path, game_text):
    with open(path + '/game_list.txt', 'w') as file:
        file.write("\n".join(game_text))
