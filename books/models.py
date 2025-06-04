from django.db import models
from django.utils.translation import gettext_lazy as _

class Publisher(models.Model):
    name = models.CharField(_("Name"), max_length=30, help_text=_("The name of the publisher."))
    address = models.CharField(_("Address"), max_length=50, help_text=_("The address of the publisher."))
    city = models.CharField(_("City"), max_length=60, help_text=_("The city where the publisher is located."))
    state_province = models.CharField(_("State or Province"), max_length=30, help_text=_("The state or province of the publisher."))
    country = models.CharField(_("Country"), max_length=50, help_text=_("The country of the publisher."))
    website = models.URLField(_("Website"), help_text=_("The publisher's website URL."))

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(_("First Name"), max_length=30)
    last_name = models.CharField(_("Last Name"), max_length=40)
    email = models.EmailField(_(" e-mail"))

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.get_full_name()
    

class Book(models.Model):
    title = models.CharField(_("Title"), max_length=100)
    authors = models.ManyToManyField("books.Author", related_name="books")
    publisher = models.ForeignKey(
        "books.Publisher", on_delete=models.CASCADE, related_name="books"
    )
    classification = models.ForeignKey(
        "books.Classification", on_delete=models.SET_NULL, null=True, blank=True, related_name="books"
    )
    publication_date = models.DateField(_("Publication Date"))

    def __str__(self):
        return self.title


class Classification(models.Model):
    code = models.CharField(_("Code"), max_length=3, help_text=_("3-digit classification code"))
    name = models.CharField(_("Name"), max_length=50)
    description = models.TextField(_("Description"))

    def __str__(self):
        return self.name