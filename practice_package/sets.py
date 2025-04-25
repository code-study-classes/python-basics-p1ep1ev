def find_common_elements(set1, set2):
    common_elements = set()
    for element in set1:
        if element in set2:
            common_elements.add(element)
    return common_elements


def is_superset(set_a, set_b):
    for element in set_b:
        if element not in set_a:
            return False
    return True


def remove_duplicates(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def count_unique_words(text):
    pass
    words = text.lower().split()
    unique_words = set(words)
    return len(unique_words)


def find_shared_items(*sets):
    pass
    if not sets:
        return set()
    return set.intersection(*sets)