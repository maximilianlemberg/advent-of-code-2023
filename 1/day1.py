# Day 1 of Advent of code
path_to_input = "./1/input.txt"
numbers_as_strings = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}


# Load input
def load_document():
    with open(path_to_input) as f:
        lines = f.read().splitlines()
        return lines


# Get first and last digit
def extract_digits(string):
    all_digits = []
    tmp = string.lower()
    while len(tmp) > 0:
        char = tmp[0]
        if char.isalpha():
            for (key, value) in numbers_as_strings.items():
                if tmp.startswith(value):
                    all_digits.append(key)

        elif char.isnumeric():
            all_digits.append(int(char))

        tmp = tmp.replace(char, "", 1)
    return all_digits


def extract_first_and_last(line):
    all_digits_array = extract_digits(line)
    if len(all_digits_array) == 1:
        return [all_digits_array[0], all_digits_array[0]]
    else:
        length = len(all_digits_array) - 1
        return [all_digits_array[0], all_digits_array[length]]


def add_digits(digits_array):
    if len(digits_array) != 2:
        raise Exception("Digits array has wrong size")

    first = str(digits_array[0])
    last = str(digits_array[1])
    concatenated = first + last
    return int(concatenated)


def get_total(sum_array):
    total = 0
    for i in sum_array:
        total += i

    return total


def main():
    lines = load_document()
    sum_array = []
    for line in lines:
        first_and_last_digit = extract_first_and_last(line)
        sum_together = add_digits(first_and_last_digit)
        sum_array.append(sum_together)

    print(sum_array)
    total = get_total(sum_array)
    print(total)


if __name__ == "__main__":
    main()
