import re
from tasks.task5 import favorite_books, student_database
    
def test_favorite_books():
    books = favorite_books()
    pattern = re.compile(r"^title: .+, author: .+$")
    assert pattern.match(books[0])
    
def test_student_database():
    db = student_database()
    assert isinstance(db, dict)
    pattern = re.compile(r"^[A-Za-z]+\s[A-Za-z]+\s\d{2}-\d{4}-\d{2}$")
    for name, id in db.items():
        assert pattern.match(f"{name} {id}")