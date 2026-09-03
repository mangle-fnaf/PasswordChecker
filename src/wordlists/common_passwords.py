def load_wordlist():
    with open("wordlists/common_passwords.txt", "r", encoding="utf-8") as f:
        return [line.strip().lower() for line in f]
