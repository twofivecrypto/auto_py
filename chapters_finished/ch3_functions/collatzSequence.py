def collatz(number):
    sequence = []

    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = (number * 3) + 1
        sequence.append(number)
    return sequence

try:
    starting_number = int(input("Enter a starting number."))
    sequence = collatz(starting_number)
    print(sequence)
except ValueError:
    print("Invalid input. Please enter a valid integer.")

