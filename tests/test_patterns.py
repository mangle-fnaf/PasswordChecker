from src.patterns import repeated_characters 

def test_repeated_characters_present():
    assert has_repeated_characters("mmmmm") is True
    assert has_repeated_characters("5555") is True
    assert has_repeated_characters("catttt") is True

def test_repeated_characters_not_present():
    assert has_repeated_characters("4297") is False
    assert has_repeated_characters("121212") is False
    assert has_repeated_characters("meowow") is False
