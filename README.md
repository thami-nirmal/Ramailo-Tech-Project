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

4. Configure the database in the `settings.py` file:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'library_db',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
Ensure that you have PostgreSQL and create a database named `library_db` with provided username and password

5. Navigate to the project directory:
```
cd src
```

6. Apply database migrations:
```
python manage.py migrate
```

7. Create a superuser for accessing the admin panel:
```
python manage.py createsuperuser
```

8. Start the development server:
```
python manage.py runserver
```

9. Access the admin panel at http://localhost:8000/admin/ and the API endpoints at http://localhost:8000/api/.


## Project Structure
The project consists of the following components:

- library/:           Django app containing the library models, serializers, and API views.

- library.api/:       Django app containing API endpoints for managing users, books, and borrowed books.

- README.md:          This file, provides setup instructions and a project overview.

- requirements.txt:   List of Python dependencies required for the project.

- manage.py:          Django project management script.

- settings.py:        Django project settings file.

- urls.py:            Django project URL configuration. 


## Features

- Allows creating, listing, and updating users.

- Allows creating, listing, and updating books.

- Allows assigning and updating book details.

- Allows recording the borrowing and returning of books.

- Provides API endpoints for user authentication.

## Technologies Used

- Django

- Django REST Framework

- Python


# Library Management API Documentation

## Base URL

All API endpoints are relative to the base URL: `/api/`

## Authentication

- Endpoint: /auth/

- Description: API endpoints are protected and require authentication. Use this endpoint to obtain an authentication token.


## Users APIs

List/Create Users

- Endpoint: `/api/users/`

- Method: GET (List), POST (Create)

- Description: Get a list of users or create a new user.

- Authentication: Required (Admin)

- Permissions: Admin only


Retrieve User

- Endpoint: `/api/users/{user_id}/`

- Method: GET

- Description: Retrieve details of a specific user by ID.

- Authentication: Required (Admin)

- Permissions: Admin only


## Books APIs

List/Create Books

- Endpoint: `/api/books/`

- Method: GET (List), POST (Create)

- Description: Get a list of books or create a new book.

- Authentication: Required (Admin)

- Permissions: Admin only


Retrieve Books

- Endpoint: `/api/books/{book_id}`

- Method: GET

- Description: Retrieve details of a specific book by its book ID.

- Authentication: Required (Admin)

- Permissions: Admin only


Assign Book Details

- Endpoint: `/api/assign-book-details/`

- Methods: POST (Create)

- Description: Assigns details to a book.

- Authentication: Required (Admin)

- Permissions: Admin only


Update Book Details

- Endpoint: `/api/update-book-details/{book_id}/`

- Method: PUT

- Description: Updates book details by book ID.

- Authentication: Required

- Permissions: Admin only


## BorrowedBooks APIs

List/Create Borrowed Books

- Endpoint: `/api/borrowed-books/`

- Methods: GET (List), POST (Create)

- Description: Allows recording the borrowing of a book and listing all borrowed books.

- Authentication: Required

- Permissions: Admin only


Return Borrowed Book

- Endpoint: `/api/borrowed-books-return/{borrowed_book_id}/`

- Method: PUT

- Description: Updates the system when a borrowed book is returned.

- Authentication: Required

- Permissions: Admin only
