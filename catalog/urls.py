from django.urls import path
from django.urls import path, include
from django.shortcuts import render

from .import views
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('auhtors/<int:pk>', views.AuthorDetailView.as_view(),name='author-detail'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),


]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]



