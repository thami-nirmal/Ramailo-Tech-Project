# Django Library Management System
This Django project implements a library management system with the following features:

## Setup Instructions
1. Clone the repository
```
git clone https://github.com/thami-nirmal/Ramailo-Tech-project.git
```

2. Activate the virtual environment

    2.1 On Windows:
    ```
    env\Scripts\activate
    ```
    2.2 On macOS and Linux
    ```
    source env/bin/activate
    ```

3. Install dependencies using pip:
```
pip install -r requirements.txt
```

4. Navigate to the project directory:
```
cd src
```

5. Apply database migrations:
```
python manage.py migrate
```

6. Create a superuser for accessing the admin panel:
```
python manage.py createsuperuser
```

7. Start the development server:
```
python manage.py runserver
```

8. Access the admin panel at http://localhost:8000/admin/ and the API endpoints at http://localhost:8000/api/.

## Project Structure
The project consists of the following components:

-library/:           Django app containing the library models, serializers, and API views.
-library.api/:       Django app containing API endpoints for managing users, books, and borrowed books.
-README.md:          This file, provides setup instructions and a project overview.
-requirements.txt:   List of Python dependencies required for the project.
-manage.py:          Django project management script.
-settings.py:        Django project settings file.
-urls.py:            Django project URL configuration. 
