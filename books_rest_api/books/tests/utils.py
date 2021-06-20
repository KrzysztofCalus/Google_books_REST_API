from books.models import Book


def create_book():
    """
    Create data for Book
    """
    Book.objects.create(book_id="test_id",
                        title="test_title",
                        authors="test_author",
                        published_date="2021",
                        categories=["test_category"],
                        average_rating=5,
                        ratings_count=5,
                        thumbnail="http://books.google.com/books/test"
                        )
