from django import forms

from .models import Author, Book


class BookForm(forms.ModelForm):

    author = forms.ModelChoiceField(queryset=Author.objects.all(), required=True)

    class Meta:
        model = Book
        fields = [
            "author",
            "name",
        ]
