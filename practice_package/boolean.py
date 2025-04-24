check_between_numbers = lambda A, B, C: A < B < C or C < B < A # noqa: E731

check_odd_three = lambda num: 100 <= abs(num) <= 999 and num % 2 != 0 # noqa: E731

check_unique_digits = lambda num: 100 <= abs(num) <= 999 and len(set(str(abs(num)))) == 3 # noqa: E731

def check_palindrome_number(n):
    return str(abs(n))[::-1] == str(abs(n))

def check_ascending_digits(number):
    if not (100 <= abs(number) <= 999):
        return False
    digits = list(map(int, str(abs(number))))
    return digits[0] < digits[1] < digits[2]