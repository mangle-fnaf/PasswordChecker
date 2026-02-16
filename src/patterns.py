import re

def repeated_characters(password: str, threshold: int = 4) -> bool:
    pattern = rf"(.)\1{{{threshold - 1},}}"
    return bool(re.search(pattern,password))

def pattern_detected(password: str) -> tuple[int,list[str]]:
    detected = 0
    issues = []

    if repeated_characters(password):
        detected += 10
        issues.append("Consecutive characters repeated.")
        
    return detected, issues