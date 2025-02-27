from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def book_list(request):
    title = request.GET.get('title')
    author = request.GET.get('author')

    filters = Q()

    if title:
        filters |= Q(title__icontains=title)
    if author:
        filters |= Q(author__icontains=author)

    books = Book.objects.filter(filters) if filters else Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})

@login_required(login_url='login')
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

@login_required(login_url='login')
def change_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', pk=pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'change_book.html', {'form': form})

@login_required(login_url='login')
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')