from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        title = self.request.GET.get('title')
        author = self.request.GET.get('author')

        filters = Q()

        if title:
            filters |= Q(title__icontains=title)
        if author:
            filters |= Q(author__icontains=author)

        return Book.objects.filter(filters) if filters else Book.objects.all()


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'


@method_decorator(login_required(login_url='login'), name='dispatch')
class AddBookView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'add_book.html'
    success_url = '/books/'


@method_decorator(login_required(login_url='login'), name='dispatch')
class ChangeBookView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'change_book.html'
    success_url = '/books/'


@method_decorator(login_required(login_url='login'), name='dispatch')
class DeleteBookView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = '/books/'