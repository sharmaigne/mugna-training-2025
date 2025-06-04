from django.forms import ModelForm
from django import forms
from books.models import Author, Book, Publisher


class SearchForm(forms.Form):
    query = forms.CharField(
        label="Search",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Search..."}),
    )

    def clean_query(self):
        query = self.cleaned_data.get("query")
        if not query:
            raise forms.ValidationError("Search query cannot be empty.")
        return query


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        fields = "__all__"