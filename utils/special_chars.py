def check_for_special_chars(word):
    if word is '':
        return False
    for char in word:
        if not char.isdigit() and not char.isalpha():
            return False
    return True
