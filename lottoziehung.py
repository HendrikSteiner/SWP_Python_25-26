import random

# Simulates a lottery draw: draws 6 random numbers from 1 to 45
def lotto_draw():
    numbers = list(range(1, 46))
    n = 45
    drawn_numbers = []

    for _ in range(6):
        random_index = random.randint(0, n - 1)
        drawn_number = numbers[random_index]
        drawn_numbers.append(drawn_number)

        temp = numbers[random_index]  # temp temporarily stores the number
        numbers[random_index] = numbers[n - 1]
        numbers[n - 1] = temp

        n -= 1

    return drawn_numbers

# Generates statistics of how often each number is drawn over many draws
def lotto_statistics(draws=1000):
    stats = {}  # Dictionary

    for number in range(1, 46):
        stats[number] = 0

    for _ in range(draws):
        drawn_numbers = lotto_draw()
        for number in drawn_numbers:
            stats[number] += 1

    return stats

def main():
    # Draw and display one set of lotto numbers
    print("Drawn Lotto Numbers:", lotto_draw())

    # Generate and display statistics
    stats = lotto_statistics()
    print("\nNumber    Times Drawn")
    for number in sorted(stats.keys()):
        print(f"{number:2d}        {stats[number]}")

if __name__ == "__main__":
    main()
