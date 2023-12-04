import re

path_to_input = "input.txt"

def load_document():
    with open(path_to_input) as f:
        lines = f.read().splitlines()
        return lines


import re

def process_line(line):
    split_line = re.split(r"(Card *\d*:)((?:\s*\d+)+)(?: \|)((?:\s*\d+)+)", line)
    if len(split_line) < 4:
        return 0  # If the line doesn't match the pattern, return 0 matches

    winning_numbers = set(filter(None, split_line[2].split(" ")))
    my_numbers = set(filter(None, split_line[3].split(" ")))

    matches = len(winning_numbers.intersection(my_numbers))
    return matches

def update_dict(cards, index, matches):
    # Add copies of the next 'matches' cards
    for i in range(1, matches + 1):
        if index + i in cards:
            cards[index + i] += 1
        else:
            cards[index + i] = 1

def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()

    cards = {i+1: 1 for i in range(len(lines))}  # Initialize all cards with 1 copy

    index = 1
    while index <= len(lines):
        current_copies = cards[index]
        for _ in range(current_copies):
            matches = process_line(lines[index - 1])
            update_dict(cards, index, matches)
        index += 1

    total_cards = sum(cards.values())
    print(f"Total scratchcards: {total_cards}")

if __name__ == "__main__":
    main()



