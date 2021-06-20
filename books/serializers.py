from .models import Book
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('book_id', 'title', 'authors', 'published_date', 'categories', 'average_rating', 'ratings_count',
                  'thumbnail')
