from django.contrib import admin
from django.db import models
from books.models import Publisher, Author, Book, Classification
from django.utils.translation import gettext_lazy as _


class BookAdmin(admin.ModelAdmin):
    fields = ["title", "authors", "classification", "publisher", "publication_date"]


class PublisherAdmin(admin.ModelAdmin):
    fields = ["name", "country", "state_province", "city", "address", "website"]
    search_fields = ["name", "city", "country", "website"]
    list_display = ["name", "city", "country", "website"]


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ["first_name", "last_name"]


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Classification)
