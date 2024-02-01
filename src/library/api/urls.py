# Import necessary modules
from rest_framework import serializers
from library.models import ( 
                            User,
                            Book,
                            BookDetails,
                            BorrowedBooks
                            )

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model
    """
    class Meta:
        """
        Meta class for configuring the UserSerializer.
        """
        model           = User
        fields          = ['user_id','name','email','membership_date']


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    """
    class Meta:
        """
        Meta class for configuring the BookSerializer.
        """
        model           = Book
        fields          = ['book_id','title','isbn','published_date','genre']


class BookDetailsSerializer(serializers.ModelSerializer):
    """
    Serializer for the BookDetails model.
    """
    class Meta:
        """
        Meta class for configuring the BookDetailsSerializer.
        """
        model           = BookDetails
        fields          = ['details_id','book_id','number_of_pages','publisher','language']


class BorrowedBooksSerializer(serializers.ModelSerializer):
    """
    Serializer for the BorrowedBooks model.
    """
    class Meta:
        """
        Meta class for configuring the BorrowedBooksSerializer.
        """
        model           = BorrowedBooks
        fields          = ['user_id','book_id','borrow_date','return_date']

        
