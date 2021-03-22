def check_for_special_chars(word):
    for char in word:
        if not char.isdigit() and not char.isalpha():
            return False
    return True
