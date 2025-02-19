def favorite_books() -> list:
    books = [
        "title: Alice in Wonderland, author: Lewis Carroll",
        "title: 1984, author: George Orwell",
        "title: Altered Carbon, author: Richard K. Morgan",
        "title: Valis, author: Phillip K. Dick",
        "title: Dune, author: Frank Herbert"
    ]
    return books[:3]

def student_database() -> dict:
    students = {
        "Jennie No": "11-0101-12",
        "Craig Jenkins": "13-0101-10",
        "Todd Howard": "12-0101-11"
    }
    return students