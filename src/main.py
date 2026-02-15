#getpass is python's built in module for password security
#Imports calculate_entropy function from entropy.py
import getpass
from entropy import calculate_entropy, crack_time_estimate

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
    password = getpass.getpass("Enter your password:")
    #calculates length of password
    print(f"password length: {len(password)}")
    #more bits means a stronger password
    entropy = calculate_entropy(password)
    print(f"password entropy: {entropy} bits")

    crack_time = crack_time_estimate(entropy)
    print(f"The estimated crack time: {crack_time}")

    strength_text, strength_color = strength_level(entropy)
    print(f"Password strength: {strength_text} ({strength_color})")
if __name__ == "__main__":
    main()
