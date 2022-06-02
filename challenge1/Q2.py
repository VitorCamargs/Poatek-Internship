import unicodedata


def is_palindrome(string: str) -> bool:
    """
    Compare a string with its inverse to check if its a palindrome

    :param string:
    :return:
    """
    # Normalize the string, lower all the characters and substitute the combined ones (á = a)
    normalized_string = unicodedata.normalize('NFD', string)
    normalized_string = ''.join([c for c in normalized_string if not unicodedata.combining(c)]).casefold()
    # Create a string equals to the inverse of the normalized original
    inverse = normalized_string[::-1]
    return inverse == normalized_string


if __name__ == '__main__':
    examples = ['Madam', 'Arara', 'Civic', 'Radar', 'Blue', 'aá']

    for string in examples:
        if is_palindrome(string):
            print(f"{string}, it's a palindrome\n")
        else:
            print(f"{string}, it's not a palindrome\n")
