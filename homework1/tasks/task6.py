def count_words(filename: str) -> int:
    
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()
        return len(words)