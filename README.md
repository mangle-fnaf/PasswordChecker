# Password Strength Checker

This project is a password strength evaluation tool designed to analyse user‑provided passwords and provide clear feedback on their security. It demonstrates practical cybersecurity concepts such as entropy calculation, pattern detection, crack‑time estimation, and secure password generation.

## Overview
The tool evaluates password strength using entropy, common pattern detection, and estimated crack time. It also includes a secure password generator that allows users to customise character sets and length. This project reflects real-world password security practices and highlights how weak patterns reduce overall strength.

## Features
- Entropy-based password strength calculation  
- Detection of weak patterns (repeated characters, common passwords, predictable sequences)  
- Estimated crack time based on entropy  
- Customisable secure password generator  
- Colour-coded strength levels (from extremely weak to perfect)  
- Wordlist integration for identifying common or compromised passwords  

## Why I Built This
I created this tool to deepen my understanding of password security, entropy, and how attackers evaluate password strength. It allowed me to explore secure generation techniques, pattern analysis, and practical methods for improving password hygiene. This project also supports my interest in secure coding and user‑focused security tools.

## How It Works
1. User chooses whether to analyse a password or generate one  
2. For analysis:
   - Password length is calculated  
   - Entropy is computed  
   - Weak patterns are detected  
   - Crack time is estimated  
   - Strength level is displayed  
3. For generation:
   - User selects character types  
   - A secure password is generated  
   - Entropy and crack time are shown  

## Example Output
Password length: 12
Pattern is too weak: repeated characters
Estimated crack time: 3 years
Password strength: strong (green)


## How to Run
1. Clone the repository  
2. Open the project folder  
3. Run the script using Python  
4. Follow the on-screen prompts to analyse or generate a password  

## Tech Stack
- Python  
- Custom entropy calculation  
- Wordlist pattern detection  
- CLI interface  

## What I Learned
- How entropy affects password strength  
- How attackers estimate crack time  
- How to detect weak password patterns  
- How to design secure password generation logic  
- How to integrate wordlists for security analysis  

## Future Improvements
- Add more pattern detection (keyboard sequences, dates, names)  
- Add a GUI version for easier use  
- Add export options for generated passwords  
- Add multi-language wordlists  
- Add strength visualisation charts  


