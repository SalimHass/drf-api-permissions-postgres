from rest_framework.generics import (
                                        ListCreateAPIView,
                                        RetrieveUpdateAPIView
                                    )


from book.models import Book
from .serializers import BookSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated



class BookListView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsOwnerOrReadOnly,IsAuthenticated )
   


class BookDetailView(RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsOwnerOrReadOnly,IsAuthenticated )
    