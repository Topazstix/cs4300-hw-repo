import requests

def fetch_text(url: str) -> str:
    
    try:
        response = requests.get(url)
        if response.raise_for_status():
            raise Exception
    except:
        return f'ERROR: Fetch failed, status code: {response.status_code()}'
    
    return response.text

def count_words_from_request(text: str) -> int:
    
    return len(text.split())

def fetch_and_count_words(url: str) -> int:
    
    text = fetch_text(url)
    return count_words_from_request(text)