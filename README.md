# Django Library Management System
This Django project implements a library management system with the following features:

## Setup Instructions
1. Clone the repository
```
git clone https://github.com/thami-nirmal/Ramailo-Tech-project.git
```

2. Activate the virtual environment
On Windows:
    ```
    env\Scripts\activate
    ```
On macOS and Linux
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

