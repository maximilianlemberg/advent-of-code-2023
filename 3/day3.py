import re

path_to_input = "input.txt"

def load_document():
    with open(path_to_input) as f:
        lines = f.read().splitlines()
        return lines


def string_has_special_char(line):
    positions = []
    for (index, char) in enumerate(line):
        if char.isalnum() is False and char != ".":
            positions.append(index)
    return len(positions) > 0


def get_special_positions_in_line(line):
    asterisks = []
    for match in re.finditer("\*", line):
        asterisks.append((match.group(), match.start(), match.end()))
    return asterisks


def get_numbers_positions_in_line(line):
    numbers = []
    numbers_plain = re.findall(r'\d+', line)
    for match in re.finditer(r'\d+', line):
        numbers.append((match.group(), match.start(), match.end()))
    return numbers


def find_bounding_numbers(start, end, line):
    numbers = get_numbers_positions_in_line(line)
    bounding_numbers = []
    for number in numbers:
        number_start = number[1]
        number_end = number[2]
        if number_end >= start and number_start <= end:
            bounding_numbers.append(number[0])

    return bounding_numbers


def process_line(index, lines, special_positions_in_line):
    numbers_array = []

    # Upper, current & lower line
    lines_to_inspect = []
    if index > 0: lines_to_inspect.append(lines[index-1])
    lines_to_inspect.append(lines[index])
    if index + 1 < len(lines): lines_to_inspect.append(lines[index + 1])

    for special_tuple in special_positions_in_line:

        start_index = max(special_tuple[1], 0)
        end_index = min(special_tuple[2], 140)
        bounding_numbers = []
        for line in lines_to_inspect:
            bounding_numbers_for_line = find_bounding_numbers( start_index, end_index, line)
            for i in bounding_numbers_for_line:
                bounding_numbers.append(i)

        if len(bounding_numbers) == 2:
            result = int(bounding_numbers[0]) * int(bounding_numbers[1])
            numbers_array.append(result)

    return numbers_array



# def process_line(index, lines, number_positions_in_line):
#     numbers_array = []
#
#     # Upper, current & lower line
#     lines_to_inspect = []
#     if index > 0: lines_to_inspect.append(lines[index-1])
#     lines_to_inspect.append(lines[index])
#     if index + 1 < len(lines): lines_to_inspect.append(lines[index + 1])
#
#     for number_tuple in number_positions_in_line:
#         number = number_tuple[0]
#         start_index = max(number_tuple[1] - 1, 0)
#         end_index = min(number_tuple[1] + len(number) + 1, 140)
#         for line in lines_to_inspect:
#             string_range = line[start_index:end_index]
#             if number == "1": print(string_range)
#             if string_has_special_char(string_range):
#                 numbers_array.append(int(number))
#     return numbers_array


def get_total(sum_array):
    total = 0
    for i in sum_array:
        total += i

    return total


def main():
    lines = load_document()
    total = 0
    for (index, line) in enumerate(lines):
        # number_positions_in_line = get_numbers_positions_in_line(line)
        sepcial_positions_in_line = get_special_positions_in_line(line)
        surrounding_numbers = process_line(index, lines, sepcial_positions_in_line)
        total += get_total(surrounding_numbers)

    print(total)

if __name__ == "__main__":
    main()


