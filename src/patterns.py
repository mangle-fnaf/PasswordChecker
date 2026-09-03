import re

def repeated_characters(password: str, threshold: int = 4) -> bool:
    pattern = rf"(.)\1{{{threshold - 1},}}"
    return bool(re.search(pattern,password))

Keyboard_pattern = [
    "qwertyuiop", "asdfghjkl", "zxcvbnm", "12345", "54321", "asdf"
]

def has_sequential_letters(password: str) -> bool:
    """Detect sequences like abc, def, xyz."""
    for i in range(len(password) - 2):
        if password[i].isalpha() and password[i+1].isalpha() and password[i+2].isalpha():
            if ord(password[i].lower()) + 1 == ord(password[i+1].lower()) and \
               ord(password[i+1].lower()) + 1 == ord(password[i+2].lower()):
                return True
    return False

def has_sequential_digits(password: str) -> bool:
    """Detect sequences like 123, 456."""
    for i in range(len(password) - 2):
        if password[i].isdigit() and password[i+1].isdigit() and password[i+2].isdigit():
            if int(password[i]) + 1 == int(password[i+1]) and \
               int(password[i+1]) + 1 == int(password[i+2]):
                return True
    return False

def has_keyboard_pattern(password: str) -> bool:
    """Detect keyboard patterns like qwerty, asdf."""
    lower = password.lower()
    return any(pattern in lower for pattern in Keyboard_pattern)

def dictionary_match(password: str, wordlist: list) -> bool:
    """Detect dictionary words or reversed dictionary words."""
    lower = password.lower()
    reversed_pw = lower[::-1]
    return any(word in lower or word in reversed_pw for word in wordlist)

def has_repeated_sequence(password: str) -> bool:
    """Detect repeated chunks like abcabc or 123123."""
    return bool(re.search(r"(..+)\1", password))


def pattern_detected(password: str, wordlist: list = None) -> tuple[int, list[str]]:
    detected = 0
    issues = []

    # repeated characters
    if repeated_characters(password):
        detected += 10
        issues.append("Consecutive characters repeated.")

    # sequential digits
    if has_sequential_digits(password):
        detected += 10
        issues.append("sequential digits detected.")

    # sequential letters
    if has_sequential_letters(password):
        detected += 10
        issues.append("sequential letters detected.")

    # keyboard pattern
    if has_keyboard_pattern(password):
        detected += 10
        issues.append("Keyboard pattern detected.")

    # repeated sequences
    if has_repeated_sequence(password):
        detected += 10
        issues.append("Repeated sequence detected.")

    # dictionary words
    if wordlist:
        if dictionary_match(password, wordlist):
            detected += 10
            issues.append("Dictionary word or reversed dictionary word detected.")

    return detected, issues
