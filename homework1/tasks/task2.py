def task_two(selection: str) -> None:
    """function to return various data types based on user selection from valid strings

    Args:
        selection (str): user selected datatype choice to return. For invalid choice, raise assertion error
        Valid selections:
                        ["int",
                        "float",
                        "str",
                        "bool"]

    Raises:
        AssertionError: return assertion error for invalid selection

    Returns:
        int|float|str|bool|AssertionError: Various return types for user selected data type
    """
    
    try:
        if selection == "int":
            return 69
        elif selection == "float":
            return 420.69
        elif selection == "str":
            return "some string"
        elif selection == "bool":
            return False
        else:
            raise AssertionError
    except AssertionError:
        return AssertionError(f'Invalid parameter input: "{selection}"')