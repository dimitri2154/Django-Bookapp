from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('books/add/', views.AddBookView.as_view(), name='add_book'),
    path('books/<int:pk>/edit/', views.ChangeBookView.as_view(), name='change_book'),
    path('books/<int:pk>/delete/', views.DeleteBookView.as_view(), name='delete_book'),
]