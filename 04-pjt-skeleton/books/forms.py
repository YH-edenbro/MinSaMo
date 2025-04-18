from django import forms
from .models import Book, Thread


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = [
            "user",
            "author_info",
            "author_profile_img",
            "author_works",
            "audio_file",
        ]

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        exclude = [
            "user",
            "book",
            "like_users",
            "cover_img",
            "created_at",
            "updated_at",
        ]