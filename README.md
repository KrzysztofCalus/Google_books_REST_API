## Books_REST_API

Django REST API application for getting and saving information from Google Books API.
***
## API Endpoints
#### GET "/books/add" - populate data base with initial books from https://www.googleapis.com/books/v1/volumes?q=Hobbit
#### GET "/books/" - return list of all books
#### GET "/books/{id}" - return book with given {id}
#### GET "/books/?published_date={year}" - return list of books with given publication {year}
#### GET "/books/?sort={+/-}published_date" - return list of all books in "-" descending published date order, "+" ascending published date order
#### GET "/books/?author={full name}" - return list of all books with given author {full name}
#### POST "/db/" - populate data base with books from https://www.googleapis.com/books/v1/volumes?q=war
