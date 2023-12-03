import csv

if __name__ == '__main__':
    text_numeric_values = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    with open('puzzle_input.csv', 'r') as csv_file:
        reader = list(csv.reader(csv_file))

        total = 0
        first_digit = 0
        last_digit = 0
        first_index = 0
        last_index = 0
        for row in reader:
            index = -1
            for digit in row[0]:
                index += 1
                if digit.isnumeric():
                    first_digit = digit
                    first_index = index
                    break
            index = len(row[0])
            for digit in reversed(row[0]):
                index -= 1
                if digit.isnumeric():
                    last_digit = digit
                    last_index = index
                    break
            if any(text_value in row[0] for text_value in text_numeric_values):
                for text_value in text_numeric_values:
                    if text_value in row[0]:
                        if row[0].index(text_value) < first_index:
                            first_digit = str((text_numeric_values.index(text_value) + 1))
                            first_index = row[0].index(text_value)
                        if row[0].rindex(text_value) > last_index:
                            last_digit = str((text_numeric_values.index(text_value) + 1))
                            last_index = row[0].rindex(text_value)
            total += int(first_digit + last_digit)
    print(total)
