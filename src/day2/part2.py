if __name__ == '__main__':

    colour_round_maximums = {'red': 0, 'green': 0, 'blue': 0}
    power_of_minimum_required_coloured_cube = 0
    sum_of_power_of_minimum_coloured_cubes = 0
    with open('puzzle_input.csv', 'r') as file:
        lines = [line.rstrip() for line in file]

        for line in lines:
            game_round_split_string = line.split(':')
            game_string = game_round_split_string[0]
            rounds_list = game_round_split_string[1]
            rounds = rounds_list.split(';')
            for round in rounds:
                cubes = round.split(',')
                for colour in colour_round_maximums.keys():
                    for cube in cubes:
                        if colour in cube:
                            if colour_round_maximums[colour] < int(cube.split(' ')[1]):
                                colour_round_maximums[colour] = int(cube.split(' ')[1])
            power_of_minimum_required_coloured_cube = colour_round_maximums['red'] * colour_round_maximums['green'] * colour_round_maximums['blue']
            sum_of_power_of_minimum_coloured_cubes += power_of_minimum_required_coloured_cube
            colour_round_maximums = dict((k, 0) for k in colour_round_maximums)
    print(sum_of_power_of_minimum_coloured_cubes)