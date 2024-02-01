# Import necessary modules
from rest_framework.generics import (
                                    ListCreateAPIView,
                                    RetrieveAPIView,
                                    RetrieveUpdateAPIView
                                    )
from library.models import (
                            User,
                            Book,
                            BookDetails,
                            BorrowedBooks
                            )
from .serializers import (
                          UserSerializer,
                          BookSerializer,
                          BookDetailsSerializer,
                          BorrowedBooksSerializer,
                         )

from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAdminUser

# region User APIs
class UserListCreateAPIView(ListCreateAPIView):
    """
    Allows creating new users and listing existing ones.
    """
    queryset                        = User.objects.all()
    serializer_class                = UserSerializer
    permission_classes              = [IsAdminUser]


class UserRetrieveAPIView(RetrieveAPIView):
    """
    Retrieves details of a specific user by their user ID.
    """
    queryset                        = User.objects.all()
    serializer_class                = UserSerializer
    permission_classes              = [IsAdminUser]
    lookup_field                    = 'user_id'


    def get_object(self):
        """
        Retrieve the user object by ID and handle NotFound exception.
        """
        try:
            # Get the user object from the queryset based on the user_id provided in the URL kwargs
            user_obj                = self.get_queryset().get(pk=self.kwargs.get('user_id'))
        
        except User.DoesNotExist:
            # Raise a NotFound exception if the user with the provided ID does not exist
            raise NotFound("Sorry, the user you are looking for does not exist.")
        
        # Check permissions for the retrieved user object
        self.check_object_permissions(self.request, user_obj)

        # Return the retrieved user object
        return user_obj
# endregion


# region Book APIs
class BookListCreateAPIView(ListCreateAPIView):
    """
    Allows adding new books and listing existing ones.
    """
    queryset                        = Book.objects.all()
    serializer_class                = BookSerializer
    permission_classes              = [IsAdminUser]


class BookRetrieveAPIView(RetrieveAPIView):
    """
    Retrieves details of a specific book by its book ID.
    """
    queryset                        = Book.objects.all()
    serializer_class                = BookSerializer
    permission_classes              = [IsAdminUser]
    lookup_field                    = 'book_id'

    def get_object(self):
        """
        Retrieve the book object by ID and handle NotFound exception.
        """
        try:
            # Get the book object from the queryset based on the book_id provided in the URL kwargs
            book_obj                = self.get_queryset().get(pk=self.kwargs.get('book_id'))
        
        except Book.DoesNotExist:
            # Raise a NotFound exception if the book with the provided ID does not exist
            raise NotFound("Sorry, the book you are looking for does not exist.")
        
        # Check permissions for the retrieved book object
        self.check_object_permissions(self.request, book_obj)

        # Return the retrieved book object
        return book_obj


class AssignBookDetailsAPIView(ListCreateAPIView):
    """
    Assigns details to a book.
    """
    queryset                        = BookDetails.objects.all()
    serializer_class                = BookDetailsSerializer
    permission_classes              = [IsAdminUser]


class UpdateBookDetailsAPIView(RetrieveUpdateAPIView):
    """
    Updates book details by book ID.
    """
    queryset                        = BookDetails.objects.all()
    serializer_class                = BookDetailsSerializer
    permission_classes              = [IsAdminUser]
    lookup_field                    = 'book_id'

    def get_object(self):
        """
        Retrieve the book details object by ID and handle NotFound exception.
        """
        try:
            # Get the book details object from the queryset based on the book_id provided in the URL kwargs
            book_details_obj        = self.get_queryset().get(pk=self.kwargs.get('book_id'))
        
        except BookDetails.DoesNotExist:
            # Raise a NotFound exception if the book details with the provided ID do not exist
            raise NotFound("Sorry, the book details you are looking for does not exist.")
        
        # Check permissions for the retrieved book details object
        self.check_object_permissions(self.request, book_details_obj)

        # Return the retrieved book details object
        return book_details_obj
#endregion


# region BorrowedBooks APIs
class BorrowedBooksListCreateAPIView(ListCreateAPIView):
    """
    Allows recording the borrowing of a book and listing all borrowed books.
    """
    queryset                        = BorrowedBooks.objects.all()
    serializer_class                = BorrowedBooksSerializer
    permission_classes              = [IsAdminUser]


class BorrowedBooksReturnAPIView(RetrieveUpdateAPIView):
    """
    Updates the system when a borrowed book is returned.
    """
    queryset                        = BorrowedBooks.objects.all()
    serializer_class                = BorrowedBooksSerializer
    permission_classes              = [IsAdminUser]
    lookup_field                    = 'borrowed_book_id'

    def get_object(self):
        """
        Retrieve the borrowed book object by ID and handle NotFound exception.
        """
        try:
            # Get the borrowed book object from the queryset based on the borrowed_book_id provided in the URL kwargs
            borrowed_book_obj       = self.get_queryset().get(pk=self.kwargs.get('borrowed_book_id'))
        
        except BorrowedBooks.DoesNotExist:
            # Raise a NotFound exception if the borrowed book with the provided ID does not exist
            raise NotFound("Sorry, the book you are looking for has not been borrowed.")
        
        # Check permissions for the retrieved borrowed book object
        self.check_object_permissions(self.request, borrowed_book_obj)

        # Return the retrieved borrowed book object
        return borrowed_book_obj

#endregion







   