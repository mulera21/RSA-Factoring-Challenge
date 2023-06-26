import sys
import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def factorize_number(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if is_prime(i) and is_prime(n // i):
                return i, n // i
    return None, None


def factorize_file(file_path):
    with open(file_path, "r") as file:
        for line in file:
            number = int(line.strip())
            p, q = factorize_number(number)
            if p is not None and q is not None:
                print("{}={}*{}".format(number, p, q))
            else:
                print("No prime factors found for {}".format(number))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: rsa <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    factorize_file(file_path)
