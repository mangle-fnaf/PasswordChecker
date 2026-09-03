from src.patterns import repeated_characters 
from patterns import pattern_detected

def test_repeated_characters_present():
    assert has_repeated_characters("mmmmm") is True
    assert has_repeated_characters("5555") is True
    assert has_repeated_characters("catttt") is True

def test_repeated_characters_not_present():
    assert has_repeated_characters("4297") is False
    assert has_repeated_characters("121212") is False
    assert has_repeated_characters("meowow") is False

def test_keyboard_pattern():
    score, issues = pattern_detected("mypasswordqwerty")
    assert "Keyboard pattern detected." in issues

def test_sequential_letters():
    score, issues = pattern_detected("abc123")
    assert "sequential letters detected." in issues