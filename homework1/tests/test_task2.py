from tasks.task2 import task_two

def test_integer():
    assert isinstance(task_two("int"), int)

def test_float():
    assert isinstance(task_two("float"), float)

def test_string():
    assert isinstance(task_two("str"), str)

def test_boolean():
    assert isinstance(task_two("bool"), bool)

def test_assert_error():
    assert isinstance(task_two("wrong"), AssertionError)