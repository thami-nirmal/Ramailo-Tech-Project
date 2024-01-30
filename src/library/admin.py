from django.contrib import admin
from .models import User, Book, BookDetails, BorrowedBooks

# Register the models with Django admin site
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # Customize the display of User model in the admin site
    list_display = ['user_id','name','email','membership_date']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Customize the display of Book model in the admin site
    list_display = ['book_id','title','isbn','published_date','genre']


@admin.register(BookDetails)
class BookDetailsAdmin(admin.ModelAdmin):
    # Cutomize the display of BookDetails model in the admin site
    list_display = ['details_id','book_id','number_of_pages','publisher','language']


@admin.register(BorrowedBooks)
class BorrowedBooksrAdmin(admin.ModelAdmin):
    # Cutomize the display of BorrowedBooks model in the admin site
    list_display = ['user_id','book_id','borrow_date','return_date']


