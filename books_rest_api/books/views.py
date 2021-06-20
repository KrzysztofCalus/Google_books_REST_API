import requests

from django.http import HttpResponse, Http404
from django.views import View
from rest_framework import status, generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer


class GoogleBooksAddView(View):
    def get(self, request):
        """
        Add data from given Google Books URL to database
        """
        google_books = requests.get("https://www.googleapis.com/books/v1/volumes?q=Hobbit")
        json_response = google_books.json()
        books = json_response['items']
        for book in books:
            Book.objects.create(
                book_id=book['id'],
                title=book['volumeInfo'].get('title'),
                authors=book['volumeInfo'].get('authors')[0],
                published_date=book['volumeInfo'].get('publishedDate')[:4],
                categories=book['volumeInfo'].get('categories', []),
                average_rating=book['volumeInfo'].get('averageRating'),
                ratings_count=book['volumeInfo'].get('ratingsCount'),
                thumbnail=book['volumeInfo'].get('imageLinks', {}).get('thumbnail')
            )
        return HttpResponse("Books added to database")


class BookDetailsView(APIView):
    def get_object(self, book_id, format=None):
        """
        Check if given id is in database
        :param book_id:
        """
        try:
            return Book.objects.get(book_id=book_id)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, book_id):
        """
        Return details about book with given id
        """
        book = self.get_object(book_id)
        serializer = BookSerializer(book)
        return Response(serializer.data)


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['published_date']

    def get_queryset(self):
        """
        Sort published_date filed and search in authors field
        """
        queryset = Book.objects.all()
        published_date = self.request.query_params.get('published_date')
        authors = self.request.query_params.getlist('author')
        if authors:
            queryset = queryset.filter(authors__in=authors).distinct()
        if published_date is not None:
            queryset = queryset.filter(published_date=published_date)
        return queryset


class BooksSaveView(APIView):
    def get(self, request, format=None):
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Insert data from given Google Books URL to update database
        """
        google_books = requests.get("https://www.googleapis.com/books/v1/volumes?q=war")
        json_response = google_books.json()
        books = json_response['items']
        for book in books:
            book_id = book['id']
            title = book['volumeInfo'].get('title')
            authors = book['volumeInfo'].get('authors')
            published_date = book['volumeInfo'].get('publishedDate')[:4]
            categories = book['volumeInfo'].get('categories', [])
            average_rating = book['volumeInfo'].get('averageRating', 0)
            ratings_count = book['volumeInfo'].get('ratingsCount', 0)
            thumbnail = book['volumeInfo'].get('imageLinks', {}).get('thumbnail')

            b = Book(book_id=book_id,
                     title=title,
                     authors=authors,
                     published_date=published_date,
                     categories=categories,
                     average_rating=average_rating,
                     ratings_count=ratings_count,
                     thumbnail=thumbnail)
            b.save()
        return Response(status=status.HTTP_200_OK)
