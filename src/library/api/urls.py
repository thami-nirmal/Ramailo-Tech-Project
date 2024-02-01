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
    path('users/', UserListCreateAPIView.as_view(), name='user_list_create'),
    
    # Endpoint to retrieve a user by ID
    path('users/<int:user_id>', UserRetrieveAPIView.as_view(), name='user_retrieve'),

    # Endpoint to create and list books
    path('books/', BookListCreateAPIView.as_view(), name='book_list_create'),
    
    # Endpoint to retrieve a book by ID
    path('books/<int:book_id>', BookRetrieveAPIView.as_view(), name='book_retrieve'),
    
    # Endpoint to assign book details
    path('assign-book-details/', AssignBookDetailsAPIView.as_view(), name='assign_book_details'),
    
    # Endpoint to update book details
    path('update-book-details/<int:book_id>/', UpdateBookDetailsAPIView.as_view(), name='update_book_details'),

    # Endpoint to create and list borrowed books
    path('borrowed-books/', BorrowedBooksListCreateAPIView.as_view(), name='borrowed_books_list-create'),
    
    # Endpoint to return a borrowed book
    path('borrowed-books-return/<int:borrowed_book_id>/', BorrowedBooksReturnAPIView.as_view(), name='borrowed_books_return'),

]
