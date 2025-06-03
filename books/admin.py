from django.contrib import admin
from books.models import Publisher, Author, Book, Classification

# Register your models here.
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Classification)