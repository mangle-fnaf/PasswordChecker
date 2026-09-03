import secrets
import string
from patterns import pattern_detected
from wordlists.common_passwords import load_wordlist

wordlist = load_wordlist()

def Secure_generator(length=15, Lower_Letters=True, Upper_Letters=True, digits=True, symbols=True):

    if length < 9:
        raise ValueError("Password too short. It must be a minimum of 9 characters.")
    
    char_sets = [
        (Lower_Letters, string.ascii_lowercase),
        (Upper_Letters, string.ascii_uppercase),
        (symbols, string.punctuation),
        (digits, string.digits)
    ]
    
    Correct_Set = [chars for enabled, chars in char_sets if enabled]

    if not Correct_Set:
        raise ValueError("The password must contain at least one character")
    
    password = [secrets.choice(chars) for chars in Correct_Set]

    all_chars = ''.join(Correct_Set)

    while len(password) < length:
        password.append(secrets.choice(all_chars))

    secrets.SystemRandom().shuffle(password)

    password = ''.join(password)

    detected, issues = pattern_detected(password, wordlist)

    while detected > 0:
        password = Secure_generator(length, Lower_Letters, Upper_Letters, digits, symbols)
        detected, issues = pattern_detected(password, wordlist)

    return password
