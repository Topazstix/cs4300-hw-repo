from tasks.task7 import fetch_and_count_words

def test_requests_word_count():
    URL = "https://www.gutenberg.org/files/11/11-0.txt"
    word_count = fetch_and_count_words(URL)
    assert word_count == 26543