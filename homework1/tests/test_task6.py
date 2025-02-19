from tasks.task6 import count_words

def register_pytest_decorator(filename: str, expected_count:int) -> callable:
    """custom pytest decorator function to make dynamic word counting in a given file for tests

    Args:
        filename (str): the string/path of the file
        expected_count (int): the expected total word count of the file

    Returns:
        callable: the decorator function that will be executed by pytest
    """
    
    def decorator(funct: callable) -> callable:
        """decorator method for pytest to use for test cases

        Args:
            funct (callable): the function to test, in our case `count_words()`

        Returns:
            callable: return the function after setting decorator and global vars for pytest
        """
        
        ## This is the test which gets run via pytest
        def test_funct():
            result = funct(filename)
            assert result == expected_count
        
        ## Make the pytest test name `test_filename`
        test_name = f'test_{filename.split('.')[0]}'
        test_funct.__name__ = test_name
        
        ## Register the decorator name for pytest to execute
        globals()[test_name] = test_funct
        
        return funct
    
    return decorator

## Lorem ipsum test case
@register_pytest_decorator("tasks/task6_read_me.txt", 127)
def count_words_pytest_wrapper(filename: str) -> int:
    return count_words(filename)

## Test case for alice in wonderland chapter/book
@register_pytest_decorator("tasks/task6_alice.txt", 26543)
def count_words_pytest_wrapper(filename: str) -> int:
    return count_words(filename)