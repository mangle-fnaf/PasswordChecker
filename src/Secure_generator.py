import secrets
import string

def Secure_generator(length=15, Lower_Letters=True, Upper_Letters=True, digits=True,symbols=True):

    if length < 9:
        raise ValueError("Password too short. It must be a minimum of 9 characters.")
    
    charset = ""
    if Lower_Letters:
        charset += string.ascii_lowercase
    if Upper_Letters:
        charset += string.ascii_uppercase
    if digits:
        charset += string.digits
    if symbols:
        charset += string.punctuation
    if not charset:
        raise ValueError("The password must contain at least one character")
    
    password = []

    if Lower_Letters:
        password.append(secrets.choice(string.ascii_lowercase))
    if Upper_Letters:
        password.append(secrets.choice(string.ascii_uppercase))
    if symbols:
        password.append(secrets.choice(string.punctuation))
    if digits:
        password.append(secrets.choice(string.digits))

    while len(password) < length:
        password.append(secrets.choice(charset))

    secrets.SystemRandom().shuffle(password)

    return ''.join(password)
    