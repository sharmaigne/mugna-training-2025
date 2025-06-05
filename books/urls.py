
from django.urls import path

from . import views

urlpatterns = [
    path("", views.list_books, name="list_books"),
    path("<int:book_pk>/", views.book_detail, name="book_detail"),
    path("authors/<int:author_pk>/", views.author_detail, name="author_detail"),
    path("classifications", views.classification_list, name="classification_list"),
    path("classifications/<int:classification_pk>/", views.classification_detail, name="classification_detail"),

    path("authors/", views.authors),
    path("publishers/", views.publishers),

    # for books and publishers
    path("<str:resource_type>/create/", views.create_resource, name="create_resource"),
    path("<str:resource_type>/update/<int:pk>/", views.update_resource, name="update_resource"),
    path("<str:resource_type>/delete/<int:pk>/", views.delete_resource, name="delete_resource"),
]