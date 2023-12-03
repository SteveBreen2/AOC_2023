if __name__ == '__main__':
    max_red_cubes = 12
    max_blue_cubes = 14
    max_green_cubes = 13
    colour_round_totals = {'red': 0, 'green': 0, 'blue': 0}
    sum_of_playable_round_ids = 0

    with open('puzzle_input.csv', 'r') as file:
        lines = [line.rstrip() for line in file]

        for line in lines:
            game_round_split_string = line.split(':')
            game_string = game_round_split_string[0]
            rounds_list = game_round_split_string[1]
            rounds = rounds_list.split(';')
            for round in rounds:
                cubes = round.split(',')
                for colour in colour_round_totals.keys():
                    for cube in cubes:
                        if colour in cube:
                            if colour_round_totals[colour] < int(cube.split(' ')[1]):
                                colour_round_totals[colour] = int(cube.split(' ')[1])
            if colour_round_totals['red'] <= max_red_cubes and colour_round_totals['blue'] <= max_blue_cubes and colour_round_totals['green'] <= max_green_cubes:
                sum_of_playable_round_ids += int(game_string.split(' ')[1])
            colour_round_totals = dict((k, 0) for k in colour_round_totals)
    print(sum_of_playable_round_ids)
