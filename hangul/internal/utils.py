def exclude_last_element(array):
    """
    Exclude the last element of the array and return the rest of the array along with the last element.
    Returns a tuple with the list without the last element and the last element itself.
    """
    if array:
        return array[:-1], array[-1]
    return [], ""


def join_string(*args):
    """
    Joins all provided string arguments into a single string.
    """
    return "".join(args)


def is_blank(character):
    """
    Check if the given character is a whitespace.
    """
    import re

    return bool(re.match(r"^\s$", character))
