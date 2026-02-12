#getpass is python's built in module for password security
#Imports calculate_entropy function from entropy.py
import getpass
from entropy import calculate_entropy, crack_time_estimate

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

if __name__ == "__main__":
    main()
