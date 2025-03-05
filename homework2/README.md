# Movie Bookings Application

## Notes

Project utilizes `python==3.12.9` via anaconda environment. Other versions of python have not been tested, however python >=~3.12.x should suffice.

AI was utilized in getting direction on configuring django projects at large, as well as help with serialization and CI/CD pipeline. [chat log available here](https://chatgpt.com/share/67c7bf92-7034-800a-b6e3-a6def1899d8c)

The remainder of code/html/etc was referenced from CS3300 project available on my [github](https://github.com/Topazstix/CompetitionTracker)

## Installation

1. clone repository
2. `python -m pip install -r requirements.txt`
3. `python manage.py makemigrations`
4. `python manage.py migrate`

## Running the Application

1. `python manage.py runserver $IP:$PORT`
   1. where `$IP` and `$PORT` are the preferred interfaces for accessing the application like `127.0.0.1:8000`
