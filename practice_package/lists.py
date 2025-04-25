def square_odds(numbers):
    result = []
    for num in numbers:
        if num % 2 != 0:
            result.append(num * num)
    return result


def normalize_names(names):
    return [name.capitalize() for name in names]


def remove_invalid_emails(emails):
    valid_emails = []
    for email in emails:
        if (
            email.count('@') == 1 and
            len(email) >= 5 and
            not email.startswith('@') and
            not email.endswith('@')
        ):
            valid_emails.append(email)
    return valid_emails


def filter_palindromes(words):
    return [word for word in words if word.lower() == word.lower()[::-1]]


def calculate_factorial(n):
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


def find_common_prefix(strings):
    if not strings:
        return ""
    prefix = strings[0]
    for string in strings[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix