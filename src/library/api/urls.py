# Import necessary modules and classes
from django.urls import path
from .views import (
                    UserListCreateAPIView,
                    UserRetrieveAPIView,
                    BookListCreateAPIView,
                    BookRetrieveAPIView,
                    AssignBookDetailsAPIView,
                    UpdateBookDetailsAPIView,
                    BorrowedBooksListCreateAPIView,
                    BorrowedBooksReturnAPIView
                    )

# Define URL patterns for API endpoints
urlpatterns     = [
    # Endpoint to create and list users
    path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    
    # Endpoint to retrieve a user by ID
    path('users/<int:user_id>', UserRetrieveAPIView.as_view(), name='user-retrieve'),

    # Endpoint to create and list books
    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    
    # Endpoint to retrieve a book by ID
    path('books/<int:book_id>', BookRetrieveAPIView.as_view(), name='book-retrieve'),
    
    # Endpoint to assign book details
    path('book-details-assign/', AssignBookDetailsAPIView.as_view(), name='assign-book-details'),
    
    # Endpoint to update book details
    path('book-details-update/<int:book_id>/', UpdateBookDetailsAPIView.as_view(), name='update-book-details'),

    # Endpoint to create and list borrowed books
    path('borrowed-books/', BorrowedBooksListCreateAPIView.as_view(), name='borrowed-books-list-create'),
    
    # Endpoint to return a borrowed book
    path('borrowed-books-return/<int:borrowed_book_id>/', BorrowedBooksReturnAPIView.as_view(), name='borrowed-books-return'),

]
