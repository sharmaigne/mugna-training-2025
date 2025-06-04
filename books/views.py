from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from books.forms import BookForm, PublisherForm, SearchForm
from books.models import Author, Classification, Book, Publisher
from django.db.models import Q

RESOURCE_MAP = {
    "book": {
        "model": Book,
        "form": BookForm,
    },
    "publisher": {
        "model": Publisher,
        "form": PublisherForm,
    },
}

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
    return render(
        request, "classification_list.html", {"classifications": classifications}
    )


def classification_detail(request, classification_pk):
    """
    View to display details of a specific classification.
    """
    classification = Classification.objects.get(pk=classification_pk)
    return render(
        request, "classification_detail.html", {"classification": classification}
    )


def search(request):
    errors = []
    context = {}

    if "q_publishers" in request.GET:
        query = request.GET["q_publishers"]
        if query:
            from books.models import Publisher

            publishers = Publisher.objects.filter(name__icontains=query)
            context = {"resource_type": "publishers", "rows": publishers}
    else:
        query = request.GET["q_authors"]
        if query:
            authors = Author.objects.filter(
                Q(first_name__icontains=query) | Q(last_name__icontains=query)
            )
            context = {"resource_type": "authors", "rows": authors}

    if not context:
        errors.append("Enter a search term.")

    return render(
        request,
        "command_base.html",
        {
            "errors": errors,
            **context,
        },
    )


def authors(request):
    errors = []
    search_form = SearchForm()
    if request.method == "GET":
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            authors = Author.objects.filter(
                Q(first_name__icontains=query) | Q(last_name__icontains=query)
            )
            return render(
                request,
                "command_base.html",
                {
                    "search_form": search_form,
                    "rows": authors,
                    "resource_type": "authors",
                },
            )
        else:
            errors.append("Please enter a valid search term.")

    authors = Author.objects.all()
    return render(
        request,
        "command_base.html",
        {
            "search_form": search_form,
            "errors": errors,
            "rows": authors,
            "resource_type": "authors",
        },
    )


def publishers(request):
    errors = []
    search_form = SearchForm()
    if request.method == "GET":
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            publishers = Publisher.objects.filter(name__icontains=query)
            return render(
                request,
                "command_base.html",
                {
                    "search_form": search_form,
                    "rows": publishers,
                    "resource_type": "publishers",
                },
            )
        else:
            errors.append("Please enter a valid search term.")

    publishers = Publisher.objects.all()
    return render(
        request,
        "command_base.html",
        {
            "search_form": search_form,
            "errors": errors,
            "rows": publishers,
            "resource_type": "publishers",
        },
    )


def create_resource(request, resource_type):
    resource_config = RESOURCE_MAP.get(resource_type)
    if not resource_config:
        return HttpResponseNotFound("Resource type not supported")

    form_class = resource_config["form"]

    if request.method == "POST":
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_books")
    else:
        form = form_class()

    return render(request, "create_or_update_resource.html", {
        "form": form,
        "resource_type": resource_type
    })

def update_resource(request, resource_type, pk):
    resource_config = RESOURCE_MAP.get(resource_type)
    if not resource_config:
        return HttpResponseNotFound("Resource type not supported")

    model = resource_config["model"]
    form_class = resource_config["form"]
    resource = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = form_class(request.POST, instance=resource)
        if form.is_valid():
            form.save()
            return redirect("list_books")
    else:
        form = form_class(instance=resource)

    return render(request, "create_or_update_resource.html", {
        "form": form,
        "resource_type": resource_type,
        "resource": resource
    })

def delete_resource(request, resource_type, pk):
    resource_config = RESOURCE_MAP.get(resource_type)
    if not resource_config:
        return HttpResponseNotFound("Resource type not supported")

    model = resource_config["model"]
    resource = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        resource.delete()
        return redirect("list_books")

    return render(request, "delete_resource.html", {
        "resource_type": resource_type,
        "resource": resource
    })