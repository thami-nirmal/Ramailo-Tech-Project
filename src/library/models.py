from django.db import models

# Create your models here.

class User(models.Model):
    user_id              = models.AutoField(primary_key=True)
    name                 = models.CharField(max_length=100)
    email                = models.EmailField(max_length=254, unique=True)
    membership_date      = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    book_id              = models.AutoField(primary_key=True)
    title                = models.CharField(max_length=100)
    isbn                 = models.CharField(max_length=13, unique=True)
    published_date       = models.DateField()
    genre                = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
class BookDetails(models.Model):
    details_id          = models.AutoField(primary_key=True)
    book_id             = models.OneToOneField(Book, related_name='bookDetails_book',on_delete=models.CASCADE)
    number_of_pages     = models.IntegerField()
    publisher           = models.CharField(max_length=100)
    language            = models.CharField(max_length=50)

    def __str__(self):
        return str(self.details_id)
    
class BorrowedBooks(models.Model):
    user_id             = models.ForeignKey(User, related_name='borrowedBooks_user',on_delete=models.CASCADE)
    book_id             = models.ForeignKey(Book, related_name='borrowedBooks_book',on_delete=models.CASCADE)
    borrow_date         = models.DateField()
    return_date         = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.user_id)
    