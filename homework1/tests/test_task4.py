from tasks.task4 import calculate_discount

def test_duck_int():
    ## Validate integer return type
    assert isinstance(calculate_discount(100, 20), int)
    assert calculate_discount(100, 20) == 80

def test_duck_float():
    ## Validate float
    assert isinstance(calculate_discount(100.0, 20.0), float)
    assert calculate_discount(100.0, 20.0) == 80.0

def test_duck_mixed():
    ## Validate mixed (this is moot because any "non-int" type will always return float.)
    assert isinstance(calculate_discount(100, 20.0), float)
    assert calculate_discount(100.0, 20) == 80.0