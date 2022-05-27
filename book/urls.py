from django.urls import path
from book.api.viewsets import (
                            BookDetailView,
                            BookListView
                        )
urlpatterns=[
    path('books-list',BookListView.as_view(), name='books_list'),
    path('book-detail/<int:pk>',BookDetailView.as_view(), name='detail')
]