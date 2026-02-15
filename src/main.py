#getpass is python's built in module for password security
#Imports calculate_entropy function from entropy.py
import getpass
from entropy import calculate_entropy, crack_time_estimate
from Secure_generator import Secure_generator

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

    choice = input("Enter 1 to check the security of a password and 2 to generate a secure password.")

    if choice == '1':
        password = getpass.getpass("Enter your password:")
    #calculates length of password
        length = len(password)
        print(f"\npassword length: {length}")
    #more bits means a stronger password
        entropy = calculate_entropy(password)
        print(f"password entropy: {entropy} bits")

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
            print(f"\nGenerated secure password: {password}")
            print("This password can now be copied to use.")

        except ValueError as E:
            print(f"\nError: {E}\n")
        
    else:
        print("\nInvalid answer. Run the program again if desired.\n")
        
if __name__ == "__main__":
    main()

