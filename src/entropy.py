import string
import math

def calculate_entropy(password):
    charset_size = 0

    if any(c.islower() for c in password):
        charset_size +=26
    if any(c.isupper() for c in password):
        charset_size +=20
    if any(c.isdigit() for c in password):
        charset_size +=10  
    if any(c in string.punctuation for c in password):
        charset_size += len(string.punctuation)

    if charset_size == 0:
        return 0
    
    entropy = len(password) * math.log2(charset_size)
    return round(entropy, 2)

def crack_time_estimate(entropy, guesses_per_second=500):
    seconds = 2 ** entropy / guesses_per_second

    if seconds < 60:
        return f"{seconds:.2f} seconds"
    elif seconds < 3600:
        minutes = seconds /60
        return f"{minutes:.2f} minutes"
    elif seconds < 86400:
        hours = seconds /60
        return f"{hours:.2f} hours"
    elif seconds < 315360000:
        days = seconds /86400
        return f"{days:.2f} days"
    else:
        years = seconds / 315360000
        return f"{years:.2f} years"
    
    