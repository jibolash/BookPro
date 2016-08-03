# BookPro

MVP for a flask assesment. A simple app to search for books based on title or category.

### To run app
  - Clone the repo
  - Install a virtual environment using the command ```virtualenv venv```
  - Start the virtual environment using the command ```source venv/bin/activate ``` on your terminal
  - Install app requirements using the command ```pip install requirements.txt```
  - Create database migrations with the following commands ```source venv/bin/activate```, ```python manage.py db init```, ```python manage.py db upgrade```
  - Create the data tables by running the commands ```source venv/bin/activate```, ```python manage.py db shell``` then ```db.create_all()```
  - Add data to your database based on the model structure inside app/models.py
  - Run the app with the command ```python manage.py runserver```

### To run tests
  - Run tests with the command ```python manage.py test```