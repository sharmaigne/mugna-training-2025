from django.shortcuts import render

from books.models import Book


def list_books(request):
    """
    View to list all books. When book is clicked, it redirects to the book detail page.
    """

    books = Book.objects.all()
    return render(request, "list_books.html", {"books": books})

def book_detail(request, book_pk):
    """
    View to display details of a specific book.
    """

    book = Book.objects.get(pk=book_pk)
    return render(request, "book_detail.html", {"book": book})

def author_detail(request, author_pk):
    """
    View to display details of a specific author.
    """

    from books.models import Author

    author = Author.objects.get(pk=author_pk)
    return render(request, "author_detail.html", {"author": author})

def classification_list(request):
    """
    View to list all classifications.
    """

    from books.models import Classification

    classifications = Classification.objects.all()
    return render(request, "classification_list.html", {"classifications": classifications})

def classification_detail(request, classification_pk):
    """
    View to display details of a specific classification.
    """

    from books.models import Classification

    classification = Classification.objects.get(pk=classification_pk)
    return render(request, "classification_detail.html", {"classification": classification})