import secrets

def generate_passphrase(wordlist_path="wordlists/common_passwords.txt", num_words=3):
    with open(wordlist_path, "r", encoding="utf-8") as f:
        words = [w.strip() for w in f if w.strip()]

    return " ".join(secrets.choice(words) for _ in range(num_words))
