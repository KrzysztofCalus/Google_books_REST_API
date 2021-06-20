import pytest

from books.models import Book


@pytest.mark.django_db
def test_book_list(client, set_up):
    response = client.get("/books/", {}, format='json')
    assert response.status_code == 200
    assert Book.objects.count() == len(response.data)


@pytest.mark.django_db
def test_book_id(client, set_up):
    book = Book.objects.first()
    response = client.get(f"/books/{book.book_id}", {}, format='json')
    assert response.status_code == 200
    for field in ("book_id", "title", "authors", "published_date", "categories", "average_rating", "ratings_count",
                  "thumbnail"):
        assert field in response.data
