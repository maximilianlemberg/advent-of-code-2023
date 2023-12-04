path_to_input = "input.txt"

max_red = 12
max_green = 13
max_blue = 14

def load_document():
    with open(path_to_input) as f:
        lines = f.read().splitlines()
        return lines


def found_too_much(turns_in_one_game):
    turns = turns_in_one_game.removeprefix(" ").split("; ")
    too_much = False
    for turn in turns:
        colors = turn.split(", ")
        for color in colors:
            print(color)
            if "blue" in color:
                num = color.removesuffix(" blue")
                if int(num) > max_blue:
                    too_much = True
                    print("Found too much blue")
            elif "red" in color:
                num = color.removesuffix(" red")
                if int(num) > max_red:
                    too_much = True
                    print("Found too much red")
            elif "green" in color:
                num = color.removesuffix(" green")
                if int(num) > max_green:
                    too_much = True
                    print("Found too much green")

    return too_much


def power_of_game(turns_in_one_game):
    turns = turns_in_one_game.removeprefix(" ").split("; ")
    biggest_blue = 0
    biggest_red = 0
    biggest_green = 0
    for turn in turns:
        colors = turn.split(", ")
        for color in colors:
            print(color)
            if "blue" in color:
                num = color.removesuffix(" blue")
                if int(num) > biggest_blue:
                    biggest_blue = int(num)
                    print("Biggest blue is now: " + num)
            elif "red" in color:
                num = color.removesuffix(" red")
                if int(num) > biggest_red:
                    biggest_red = int(num)
                    print("Biggest red is now: " + num)
            elif "green" in color:
                num = color.removesuffix(" green")
                if int(num) > biggest_green:
                    biggest_green = int(num)
                    print("Biggest green is now: " + num)
    power = biggest_blue * biggest_green * biggest_red
    print(power)
    return power


def main():
    lines = load_document()
    total = 0
    for line in lines:
        line_data = list(line.split(":"))
        if len(line_data) != 2:
            raise Exception("wrong format")
        game_id = line_data[0].removeprefix("Game ")
        print("---------Game " + game_id + "------------")
        turns = line_data[1]
        pog = power_of_game(turns)
        total += pog
    print(total)


if __name__ == "__main__":
    main()
