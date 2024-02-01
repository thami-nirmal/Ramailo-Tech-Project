from django.db import models

# Create the models here.

class User(models.Model):
    """
    Represents a user in the library system with specific attributes.
    """
    user_id                     = models.AutoField(primary_key=True)
    name                        = models.CharField(max_length=100)
    email                       = models.EmailField(max_length=254, unique=True)
    membership_date             = models.DateField()

    def __str__(self):
        """
        :return: the name of User
        """
        return self.name

    
class Book(models.Model):
    """
    Represents a book in the library system with specific attributes.
    """
    book_id                     = models.AutoField(primary_key=True)
    title                       = models.CharField(max_length=100)
    isbn                        = models.CharField(max_length=13, unique=True)
    published_date              = models.DateField()
    genre                       = models.CharField(max_length=50)

    def __str__(self):
        """
        :return: the title of the Book
        """
        return self.title
    
class BookDetails(models.Model):
    """
    Represents additional details of a book.
    """
    details_id                  = models.AutoField(primary_key=True)
    book_id                     = models.OneToOneField(Book, related_name='bookDetails_book',on_delete=models.CASCADE)
    number_of_pages             = models.IntegerField()
    publisher                   = models.CharField(max_length=100)
    language                    = models.CharField(max_length=50)

    def __str__(self):
        """
        :return: the ID of BookDetails
        """
        return str(self.details_id)
    
class BorrowedBooks(models.Model):
    """
    Represents a borrowed book by a user.
    """
    user_id                     = models.ForeignKey(User, related_name='borrowedBooks_user',on_delete=models.CASCADE)
    book_id                     = models.ForeignKey(Book, related_name='borrowedBooks_book',on_delete=models.CASCADE)
    borrow_date                 = models.DateField()
    return_date                 = models.DateField(null=True, blank=True)

    def __str__(self):
        """
        :return: the ID of the user who borrowed the book
        """
        return str(self.user_id)
    