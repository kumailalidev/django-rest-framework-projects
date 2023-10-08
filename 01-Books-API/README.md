# 📕 Books REST API

## Description:

A Books REST API is a web-based service that provides read-only access to a collection of books and their associated authors. This API restricts HTTP methods to only allow `GET` requests on specific endpoints

## Endpoints

| Endpoint            | Description                                                                                                                                      | Allowed HTTP Method | Permissions |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------- | ----------- |
| `api/`              | This endpoint allows users to retrieve a list of all available books.                                                                            | GET                 | Any         |
| `api/book/<int:pk>` | The API provides a detailed view of individual books. Users can request specific book details by sending a GET request to the book's unique URL. | GET                 | Any         |
| `api/authors/ `     | This endpoint allows users to retrieve a list of all authors.                                                                                    | GET                 | Any         |
