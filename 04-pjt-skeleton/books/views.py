from django.shortcuts import render, redirect
from .models import Book, Thread
from .forms import BookForm, ThreadForm
from .utils import (
    process_wikipedia_info,
    generate_author_gpt_info,
    generate_audio_script,
    create_tts_audio,
)
from django.contrib.auth.decorators import login_required

def index(request):
    books = Book.objects.all()
    context = {
        "books": books,
    }
    return render(request, "books/index.html", context)

@login_required
def create(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user

            wiki_summary = process_wikipedia_info(book)

            author_info, author_works = generate_author_gpt_info(
                book, wiki_summary
            )

            book.author_info = author_info
            book.author_works = author_works
            book.save()

            audio_script = generate_audio_script(book, wiki_summary)

            audio_file_path = create_tts_audio(book, audio_script)
            if audio_file_path:
                book.audio_file = audio_file_path
                book.save()

            return redirect("books:detail", book.pk)
    else:
        form = BookForm()
    context = {"form": form}
    return render(request, "books/create.html", context)


def detail(request, pk):
    book = Book.objects.get(pk=pk)
    threads = Thread.objects.all()
    thread_form = ThreadForm()

    context = {
        "book": book,
        "threads" : threads,
        "thread_form" : thread_form,
    }
    return render(request, "books/detail.html", context)

@login_required
def update(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect("books:detail", pk)
    else:
        form = BookForm(instance=book)
    context = {
        "form": form,
        "book": book,
    }
    return render(request, "books/update.html", context)

@login_required
def delete(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect("books:index")


@login_required
def thread_create(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        thread_form = ThreadForm(request.POST)
        if thread_form.is_valid():
            thread = thread_form.save(commit=False)
            thread.user = request.user
            thread.book = book
            thread.save()
            return redirect('books:detail', pk)
    else:
        thread_form = ThreadForm()
    context = {
        "book" : book,
        "thread_form" : thread_form,
    }
    return render(request, 'books/thread_create.html', context)


def thread_detail(request, pk, thread_pk):
    book = Book.objects.get(pk=pk)
    thread = Thread.objects.get(pk=thread_pk)
    context = {
        'book' : book,
        'thread' : thread,
    }
    return render(request, 'books/thread_detail.html', context)


@login_required
def thread_update(request, pk, thread_pk):
    book = Book.objects.get(pk=pk)
    thread = Thread.objects.get(pk=thread_pk)
    if request.method == 'POST':
        thread_form = ThreadForm(request.POST, request.FILES, instance=thread)
        if thread_form.is_valid():
            thread_form.save()
            return redirect('books:thread_detail', pk, thread_pk)
    else:
        thread_form = ThreadForm(instance=thread)
    context = {
        "book" : book,
        "thread" : thread,
        "thread_form" : thread_form,
    }
    return render(request, 'books/thread_update.html', context)


@login_required
def thread_delete(request, pk, thread_pk):
    thread = Thread.objects.get(pk=thread_pk)
    if request.method == 'POST':
        thread.delete()
    return redirect('books:detail', pk)


@login_required
def thread_likes(request, pk, thread_pk):
    thread = Thread.objects.get(pk=thread_pk)
    if request.user in thread.like_users.all():
        thread.like_users.remove(request.user)
    else:
        thread.like_users.add(request.user)
    return redirect('books:thread_detail', pk, thread_pk)