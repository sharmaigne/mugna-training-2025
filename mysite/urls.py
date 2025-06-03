"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from mysite.views import (
    index,
    current_datetime,
    datetime_offset,
    calculate,
    is_valid_date,
)

from books.views import list_books, book_detail, author_detail, classification_list, classification_detail

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/", index, name="index"),
    path("time/", current_datetime, name="current_datetime"),
    path("time/plus/<int:offset>/", datetime_offset),
    path("math/<path:numbers>/", calculate, name="calculate_multiple"),
    path("valid-date/<int:year>/<int:month>/<int:day>", is_valid_date),

    path("books/", list_books, name="list_books"),
    path("books/<int:book_pk>/", book_detail, name="book_detail"),
    path("books/authors/<int:author_pk>/", author_detail, name="author_detail"),
    path("books/classifications", classification_list, name="classification_list"),
    path("books/classifications/<int:classification_pk>/", classification_detail, name="classification_detail"),
]
