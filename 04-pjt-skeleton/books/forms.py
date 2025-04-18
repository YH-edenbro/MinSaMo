from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = [
            "author_info",
            "author_profile_img",
            "author_works",
            "audio_file",
        ]
