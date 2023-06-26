import sys


def factorize_number(number):
    factors = []
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            factors.append((i, number // i))
    return factors


def factorize_numbers(file_path):
    with open(file_path, "r") as file:
        for line in file:
            number = int(line.strip())
            factors = factorize_number(number)
            for factor in factors:
                print("{}={}*{}".format(number, factor[0], factor[1]))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    factorize_numbers(file_path)
