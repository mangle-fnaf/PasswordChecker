# PasswordChecker
An MVP for a password checker

The chosen formula:
Entropy=length×log2​(character set size)

This formula is also, known as Brute-Force search space entropy.
This formula was chosen after extensive research into different entropy calculations and formulae. 
I concluded that this formula is the most appropriate for checking passwords as it calculates the maxmimum possible entropy for passwords (length and charset).

This calculation is not perfect but it felt appropriate to use as it is an MVP.

This formula assumes:
- No patterns exist
- Each character is random
- All characters detected are equally as likely

Keyboard patterns:
research suggests some keyboard patterns are most commonly used such as 'asdf' or 'qwertyuiop'. Keys that are closer together are more commonly used for passwords as they are easier to remember.

