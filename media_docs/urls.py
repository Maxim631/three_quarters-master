from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html")),
    path("books/<slug:book_slug>", views.DetailBookView.as_view(), name="show-book"),
    path("books/", views.BooksView.as_view(), name="books"),
    path("books/append/", views.BookAppend.as_view(), name="book-append"),
    path("books/<slug:book_slug>/delete/", views.BookDelete.as_view(), name="book-delete"),
    path("books/<slug:book_slug>/edit", views.BookEdit.as_view(), name="book-edit"),

    path("journal/<slug:journal_slug>", views.DetailJournalView.as_view(), name="show-journal"),
    path("journal/", views.JournalView.as_view(), name="journal"),
    path("journal/append/", views.JournalAppend.as_view(), name="journal-append"),
    path("journal/<slug:journal_slug>/delete/", views.JournalDelete.as_view(), name="journal-delete"),
    path("journal/<slug:journal_slug>/edit", views.JournalEdit.as_view(), name="journal-edit"),

    path("comics/<slug:comics_slug>", views.DetailComicsView.as_view(), name="show-comics"),
    path("comics/", views.ComicsView.as_view(), name="comics"),
    path("comics/append/", views.ComicsAppend.as_view(), name="comics-append"),
    path("comics/<slug:comics_slug>/delete/", views.ComicsDelete.as_view(), name="comics-delete"),
    path("comics/<slug:comics_slug>/edit", views.ComicsEdit.as_view(), name="comics-edit")
]
