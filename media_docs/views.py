import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Book, Journal, Comics






class BooksView(View):
    def get(self, request):
        return render(
            request,
            "items_list.html",
            {
                "items": Book.objects.all().select_related("uploaded_by"),
                "image": "img/books.png",
                "category": "Книги",
            },
        )


class DetailBookView(View):
    def get(self, request, book_slug: str):
        book = get_object_or_404(Book, slug=book_slug)
        return render(
            request,
            "show_item.html",
            {
                "item": book,
                "category": "Книги",
            },
        )


class BookAppend(View):

    category = Book()
    def get(self, request):
        return render(request, "append_file.html", {"category": "Книги"})

    def post(self, request):
        name = self.category
        name.title = request.POST.get("title")
        name.about = request.POST.get("about")
        name.author = request.POST.get("author")
        name.year = request.POST.get("year")
        name.uploaded_by = request.user
        name.image = request.FILES["image"]
        name.file = request.FILES["file"]
        name.save()
        return redirect("/")


class BookEdit(View):
    def get(self, request, book_slug):
        book: Book = get_object_or_404(Book, slug=book_slug)
        return render(request, "edit_item.html", {"title": book.title,
                                                    "about": book.about,
                                                    "author": book.author,
                                                    "year": book.year,
                                                    "image": book.image,
                                                    "file": book.file,
                                                    }
                      )
#

    def post(self, request, book_slug):
        book: Book = get_object_or_404(Book, slug=book_slug)
        book.title = request.POST.get("title")
        book.about = request.POST.get("about")
        book.author = request.POST.get("author")
        book.year = request.POST.get("year")
        book.uploaded_by = request.user
        book.image = request.FILES["image"]
        book.file = request.FILES["file"]
        Book.objects.filter(slug=book_slug).update(title=book.title,
                                                   about=book.about,
                                                   author=book.author,
                                                   year=book.year,
                                                   image=book.image,
                                                   file=book.file,
                                                   )
        return redirect('/', book_slug)


class BookDelete(View):
    category = Book()
    def post(self, request, book_slug):
        Book.objects.filter(slug=book_slug).delete()
        return redirect("/")


class JournalView(View):
    def get(self, request):
        return render(
            request,
            "items_list.html",
            {
                "items": Journal.objects.all().select_related("uploaded_by"),
                "image": "img/journal.png",
                "category": "Статьи"
            },
        )


class DetailJournalView(View):
    def get(self, request, journal_slug: str):
        journal = get_object_or_404(Journal, slug=journal_slug)
        return render(
            request,
            "show_item.html",
            {
                "item": journal,
                "category": "Статьи"
            },
        )


class JournalAppend(BookAppend):

    category = Journal()
    def get(self, request):
        return render(request, "append_file.html", {"category": "Статьи"})



class JournalEdit(BookEdit):
    def get(self, request, journal_slug):
        journal: Journal = get_object_or_404(Journal, slug=journal_slug)
        return render(request, "edit_item.html", {"title": journal.title,
                                                    "about": journal.about,
                                                    "author": journal.author,
                                                    "year": journal.year,
                                                    "image": journal.image,
                                                    "file": journal.file,
                                                    }
                      )
#

    def post(self, request, journal_slug):
        journal: Journal = get_object_or_404(Journal, slug=journal_slug)
        journal.title = request.POST.get("title")
        journal.about = request.POST.get("about")
        journal.author = request.POST.get("author")
        journal.year = request.POST.get("year")
        journal.uploaded_by = request.user
        journal.image = request.FILES["image"]
        journal.file = request.FILES["file"]
        Journal.objects.filter(slug=journal_slug).update(title=journal.title,
                                                   about=journal.about,
                                                   author=journal.author,
                                                   year=journal.year,
                                                   image=journal.image,
                                                   file=journal.file)
        return redirect('/')


class JournalDelete(View):
    def post(self, request, journal_slug: int):
        Journal.objects.filter(slug=journal_slug).delete()
        return redirect("/")


class ComicsView(View):
    def get(self, request):
        return render(
            request,
            "items_list.html",
            {
                "items": Comics.objects.all().select_related("uploaded_by"),
                "image": "img/comics.png",
                "category": "Комиксы"
            },
        )


class DetailComicsView(View):
    def get(self, request, comics_slug: str):
        comics = get_object_or_404(Comics, slug=comics_slug)
        return render(
            request,
            "show_item.html",
            {
                "item": comics,
                "category": "Комиксы",
            },
        )


class ComicsAppend(BookAppend):
    category = Comics()
    def get(self, request):
        return render(request, "append_file.html", {"category": "Комиксы"})



class ComicsEdit(View):
    def get(self, request, comics_slug):
        comics: Comics = get_object_or_404(Comics, slug=comics_slug)
        return render(request, "edit_item.html", {"title": comics.title,
                                                    "about": comics.about,
                                                    "author": comics.author,
                                                    "year": comics.year,
                                                    "image": comics.image,
                                                    "file": comics.file,
                                                    }
                      )
#

    def post(self, request, comics_slug):
        comics: Comics = get_object_or_404(Comics, slug=comics_slug)

        comics.title = request.POST.get("title")
        comics.about = request.POST.get("about")
        comics.author = request.POST.get("author")
        comics.year = request.POST.get("year")
        comics.uploaded_by = request.user
        comics.image = request.FILES["image"]
        comics.file = request.FILES["file"]
        Journal.objects.filter(slug=comics_slug).update(title=comics.title,
                                                   about=comics.about,
                                                   author=comics.author,
                                                   year=comics.year,
                                                   image=comics.image,
                                                   file=comics.file)
        return redirect('/', comics_slug)


class ComicsDelete(View):
    def post(self, request, comics_slug):
        Comics.objects.filter(slug=comics_slug).delete()
        return redirect("/")



