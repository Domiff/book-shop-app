from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from .forms import CreateBookForm, UpdateBookForm
from .mixins import AdminRequiredMixin
from .models import Book


class ListBookView(ListView):
    template_name = "book_app/list_books.html"
    queryset = Book.objects.prefetch_related("author").all()
    context_object_name = "books"


class DetailBookView(DetailView):
    template_name = "book_app/detail_book.html"
    context_object_name = "book"

    def get_object(self, queryset = None):
        return Book.objects.prefetch_related("author").get(pk=self.kwargs["pk"])


class CreateBookView(AdminRequiredMixin, CreateView):
    template_name = "book_app/create_book.html"
    model = Book
    form_class = CreateBookForm
    success_url = reverse_lazy("book_app:books")


class UpdateBookView(AdminRequiredMixin, UpdateView):
    template_name = "book_app/update_book.html"
    model = Book
    form_class = UpdateBookForm
    context_object_name = "book"
    success_url = reverse_lazy("book_app:books")


class DeleteBookView(AdminRequiredMixin, DeleteView):
    template_name = "book_app/delete_book.html"
    model = Book
    success_url = reverse_lazy("book_app:books")


class BookSearchView(ListView):
    model = Book
    template_name = 'book_app/main.html'
    context_object_name = 'books'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('query')

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('query', '')
        return context
