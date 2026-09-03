#getpass is python's built in module for password security
#Imports calculate_entropy function from entropy.py
import getpass
from entropy import calculate_entropy, crack_time_estimate
from Secure_generator import Secure_generator
from patterns import repeated_characters
from patterns import pattern_detected

from wordlists.common_passwords import load_wordlist
wordlist = load_wordlist()

def strength_level(entropy):
    if entropy < 30:
        return "Extremely weak", "red"
    elif entropy < 50:
        return "weak", "orange"
    elif entropy < 70:
        return "moderate", "yellow"
    elif entropy < 90:
        return "strong", "green"
    elif entropy < 110:
        return "very strong", "blue"
    else: 
        return "perfect", "purple"

def main():
    print("Password Security Checker")

    choice = input("Enter 1 to check the security of a password, 2 to generate a secure password, or 3 to generate an NCSC passphrase.")

    if choice == '1':
        password = getpass.getpass("Enter your password:")
        length = len(password)
        print(f"\npassword length: {length}")
    
        entropy = calculate_entropy(password)
        detected, issues = pattern_detected(password, wordlist)
        entropy -= detected

        for issue in issues:
            print(f"Pattern is too weak: {issue}")

        if length < 12:
            print("NCSC guidance: Passwords should be at least 12 characters long.")

        if password.lower() in wordlist:
            print("NCSC guidance: This password is commonly used and should not be used.")

        if entropy < 50:
            print("NCSC recommendation: Use a passphrase made of three random words.")

        crack_time = crack_time_estimate(entropy)
        print(f"The estimated crack time: {crack_time}")

        strength_text, strength_color = strength_level(entropy)
        print(f"Password strength: {strength_text} ({strength_color})")

    elif choice == '2':
        try:
            length = int(input("Please enter your preffered password length. It must be a minimum of 9 characters.").strip())
            Lower_Letters = input("Would you like to include lowercase letters? (y/n)").strip().lower() == 'y'
            Upper_Letters = input("Would you like to include uppercase letters? (y/n)").strip().lower() == 'y'
            symbols = input("Woukd you like symbols? (y/n)").strip().lower() == 'y'
            digits = input("Would you like to include digits? (y/n)").strip().lower() == 'y'

            password = Secure_generator(length, Lower_Letters, Upper_Letters, symbols, digits)

            entropy = calculate_entropy(password)
            detected, issues = pattern_detected(password, wordlist) 
            entropy -= detected 

            for issue in issues:
                print(f"Pattern is too weak: {issue}")

            crack_time = crack_time_estimate(entropy)
            strength_text, strength_color = strength_level(entropy)

            print(f"\nGenerated secure password: {password}")
            print(f"Password entropy: {entropy} bits")
            print(f"Estimated crack-time: {crack_time}\n")
            print(f"password strength: {strength_text} ({strength_color})")
            print("This password can now be copied to use.")

        except ValueError as E:
            print(f"\nError: {E}\n")

    elif choice == '3':
        from Secure_passphrase import generate_passphrase
        passphrase = generate_passphrase()
        entropy = calculate_entropy(passphrase)
        print(f"\nGenerated NCSC passphrase: {passphrase}")
        print(f"Entropy: {entropy} bits")

    else:
        print("\nInvalid answer. Run the program again if desired.\n")

if __name__ == "__main__":
    main()
